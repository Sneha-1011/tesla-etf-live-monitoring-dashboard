from flask import Flask, jsonify
from google.cloud import bigquery
from twelvedata import TDClient
import pandas as pd
import uuid  
from datetime import datetime

app = Flask(__name__)

PROJECT_ID = "bi-project-455605"
DATASET_ID = "T_ETF"

client = bigquery.Client()
td = TDClient(apikey="f0a2ff9249504563bd21d0bbfc93ea65")

def generate_id():
    return int(uuid.uuid4().int % 1e9)  

def create_tables(): 
    tables = {
        "Fact_table": f"""
            CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_ID}.Fact_table` (
                data_id INT64 NOT NULL,
                date_id INT64 NOT NULL,
                close FLOAT64
            )
        """,
        "price_info": f"""
            CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_ID}.price_info` (
                data_id INT64 NOT NULL,
                low FLOAT64,
                high FLOAT64,
                open FLOAT64,
                close FLOAT64
            )
        """,
        "volume_info": f"""
            CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_ID}.volume_info` (
                data_id INT64 NOT NULL,
                volume INT64
            )
        """,
        "date": f"""
            CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_ID}.date` (
                date_id INT64 NOT NULL,
                Date STRING,
                Day INT64,
                Month INT64,
                Year INT64,
                Hour INT64,
                Minute INT64,
                Second INT64
            )
        """
    }

    for table, query in tables.items():
        client.query(query).result()

def push_data_to_bigquery(data):
    fact_data = []
    price_data = []
    volume_data = []
    date_data = []

    for entry in data:
        data_id = generate_id()
        date_id = generate_id()

        dt_string = entry['datetime'].replace(" UTC", "")  
        dt = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")  

        fact_data.append((data_id, date_id, float(entry['close'])))
        price_data.append((data_id, float(entry['low']), float(entry['high']), float(entry['open']), float(entry['close'])))
        volume_data.append((data_id, int(entry['volume'])))
        date_data.append((date_id, dt_string, dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second))
    
    tables_data = {
        "Fact_table": (fact_data, ["data_id", "date_id", "close"]),
        "price_info": (price_data, ["data_id", "low", "high", "open", "close"]),
        "volume_info": (volume_data, ["data_id", "volume"]),
        "date": (date_data, ["date_id", "Date", "Day", "Month", "Year", "Hour", "Minute", "Second"]),
    }

    for table, (data_list, columns) in tables_data.items():
        df = pd.DataFrame(data_list, columns=columns)
        df.to_gbq(destination_table=f"{DATASET_ID}.{table}", project_id=PROJECT_ID, if_exists="append")

@app.route('/fetch_store', methods=['GET'])
def fetch_store():
    try:
        ts = td.time_series(
            symbol="TSLA",
            interval="1min",
            start_date="2025-04-25 00:09:30",
            end_date="2025-04-25 15:59:59",
            timezone="America/New_York",
            outputsize=2500
        )
        data = ts.as_json()

        create_tables()
        push_data_to_bigquery(data)

        return jsonify({"status": "success", "message": "Data stored in BigQuery!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
