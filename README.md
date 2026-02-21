# Self-Service Data Ingestion & ETL Platform

A web-based data ingestion tool that allows users to upload CSV files or fetch data from REST APIs, automatically clean and process the data, store it in cloud-hosted PostgreSQL (Neon), and perform SQL queries with download support.

---

## Overview

Organizations often receive raw data from multiple sources such as CSV files and APIs. Managing, cleaning, and making this data analysis-ready manually is time-consuming and error-prone.

This project provides a simple **self-service ETL platform** where users can:

* Upload CSV files or provide API endpoints
* Automatically clean and standardize data
* Store processed data in cloud PostgreSQL
* Maintain versioned datasets (timestamp-based tables)
* Preview and download cleaned data
* Execute SQL queries directly from the interface

---

## Features

### Data Ingestion

* Upload CSV files
* Fetch data from REST APIs
* Convert all input into structured Pandas DataFrames

### Data Processing

* Column name standardization (lowercase, underscore format)
* Duplicate removal
* Basic schema normalization

### Cloud Storage

* Stores processed data in **Neon PostgreSQL**
* Automatic timestamp-based table creation
  Example:
  `insurance_data_20260221_184512`
* Prevents overwriting and maintains historical versions

### Data Access & Querying

* View available tables
* Run custom SQL queries
* Preview query results
* Download query output as CSV

### Export

* Download cleaned dataset before or after storage

---

## Tech Stack

* Python
* Streamlit (Web UI)
* Pandas (Data Processing)
* SQLAlchemy (Database ORM)
* Neon PostgreSQL (Cloud Database)
* Requests (API Integration)
* python-dotenv (Environment variable management)

---

## Project Structure

```
project/
│
├── app.py            # Streamlit application
├── config.py         # Loads environment variables
├── .env              # Database credentials (not pushed to GitHub)
├── requirements.txt
├── .gitignore
├── data/
└── logs/
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-link>
cd <project-folder>
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
DB_URL=postgresql+psycopg2://username:password@host/neondb
```

This keeps database credentials secure.

---

### 5. Run the Application

```
streamlit run app.py
```

The app will open in your browser.

---

## How It Works

1. Select data source (CSV or API)
2. Preview raw data
3. System performs cleaning and normalization
4. Enter base table name
5. Data saved as timestamped table in Neon
6. Optionally download cleaned data
7. Run SQL queries and export results

---

## Example Use Cases

* Data analysts uploading raw datasets for quick processing
* Centralizing data from multiple CSV files
* Preparing API data for SQL analysis
* Maintaining versioned historical datasets
* Quick exploratory data analysis via SQL

---

## Security Practices

* Database credentials stored using `.env`
* `.env` excluded via `.gitignore`
* SSL-enabled connection to Neon PostgreSQL

---

## Future Improvements

* Data type validation and schema inference
* Large file chunk processing
* User authentication
* Query history
* Deployment on Streamlit Cloud

---

## License

This project is for educational and demonstration purposes.
