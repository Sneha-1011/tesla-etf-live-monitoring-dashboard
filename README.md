<h1>📊 Tesla ETF Monitoring & Analytics Dashboard</h1>

<p>This project is a real-time data pipeline and visualization system for tracking Tesla's ETF (Exchange Traded Fund) performance at a high frequency using the Twelve Data API. It extracts, transforms, and loads ETF time-series data into Google BigQuery, and displays insights via Power BI dashboards.</p>

<hr>

<h2>🚀 Project Overview</h2>
<ul>
  <li>Tracks <strong>minute-level ETF data</strong> for Tesla (TSLA) using Twelve Data API</li>
  <li>Handles <strong>5 years of historical data</strong> from April 1st of each financial year</li>
  <li>Automatically <strong>deletes duplicate or overlapping entries</strong> from BigQuery</li>
  <li>Provides structured schema: <code>fact_table</code>, <code>price_info</code>, <code>volume_info</code>, <code>date</code></li>
  <li>Feeds data to <strong>interactive Power BI dashboard</strong> for visualization and decision-making</li>
</ul>

<hr>

<h2>⚙️ Tech Stack</h2>
<ul>
  <li><strong>Python Flask:</strong> Web framework to trigger data fetch operations</li>
  <li><strong>Google BigQuery:</strong> Scalable cloud data warehouse for storing structured ETF data</li>
  <li><strong>Twelve Data API:</strong> High-frequency financial data source</li>
  <li><strong>Pandas:</strong> Data transformation and formatting before upload</li>
  <li><strong>Power BI:</strong> Real-time dashboard and insights generation</li>
</ul>

<hr>

<h2>📈 Data Architecture</h2>
<p>Data is normalized into four tables:</p>
<ol>
  <li><strong>Fact_table:</strong> data_id, date_id, close price</li>
  <li><strong>Price_info:</strong> low, high, open, close values per minute</li>
  <li><strong>Volume_info:</strong> trading volume per minute</li>
  <li><strong>Date:</strong> datetime breakdown (year, month, day, hour, minute, second)</li>
</ol>

<hr>

<h2>📦 Features</h2>
<ul>
  <li>🚀 <strong>Automated ETL:</strong> Fetches and cleans ETF data programmatically</li>
  <li>📉 <strong>Duplicate Handling:</strong> Deletes existing rows within the selected date range before reloading</li>
  <li>⏱ <strong>Time-zone aligned:</strong> Adjusts for US market hours (UTC 14:30–21:00)</li>
  <li>📊 <strong>BI-Ready:</strong> Cleaned data model suitable for Power BI dashboards and time-series analytics</li>
</ul>

<hr>

<h2>🧑‍💼 Who Is This For?</h2>
<ul>
  <li>📈 <strong>Investors & Analysts</strong> tracking Tesla ETF trends</li>
  <li>📊 <strong>Financial Engineers</strong> building real-time dashboards</li>
  <li>📡 <strong>Data Engineers</strong> implementing cloud pipelines for financial analytics</li>
</ul>

<hr>

<h2>📌 Example Use Cases</h2>
<ul>
  <li>Compare Tesla’s ETF closing prices and volumes across years</li>
  <li>Identify high-volatility minutes and price spikes using high-frequency data</li>
  <li>Trigger alerts or insights based on live ETF activity</li>
</ul>

<hr>

<h2>🛠️ How to Use</h2>
<ol>
  <li>Set up your Twelve Data API key and Google BigQuery credentials</li>
  <li>Run the Flask app: <code>python app.py</code></li>
  <li>Access route: <code>http://localhost:5000/fetch_store</code></li>
  <li>Connect Power BI to BigQuery and visualize the schema</li>
</ol>

<hr>

<h2>📄 License</h2>
<p>This project is for educational and academic use only. Always check data provider terms (Twelve Data API) before using in production.</p>
