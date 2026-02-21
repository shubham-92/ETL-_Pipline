
import pandas as pd
import requests
import argparse
import logging
from sqlalchemy import create_engine

# Neon DB URL
from config import DB_URL

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------
# Extract from API
# -----------------------
def extract_api(api_url):
    print("Extracting from API...")
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

# -----------------------
# Extract from CSV
# -----------------------
def extract_csv(file_path):
    print("Extracting from CSV...")
    df = pd.read_csv(file_path)
    return df

# -----------------------
# Clean column names
# -----------------------
def clean_dataframe(df):
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    df = df.drop_duplicates()
    return df

# -----------------------
# Load to Neon
# -----------------------
def load_to_db(df, table_name):
    print(f"Loading data to table: {table_name}")

    engine = create_engine(DB_URL, connect_args={"sslmode": "require"})

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",   # creates new table every time
        index=False
    )

    print("Data loaded successfully")
    logging.info(f"Data loaded into table {table_name}")


# -----------------------
# Main Tool
# -----------------------
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--api", help="API URL")
    parser.add_argument("--csv", help="CSV file path")
    parser.add_argument("--table", required=True, help="Table name")

    args = parser.parse_args()

    try:
        if args.api:
            df = extract_api(args.api)
        elif args.csv:
            df = extract_csv(args.csv)
        else:
            print("Provide either --api or --csv")
            return

        df = clean_dataframe(df)
        load_to_db(df, args.table)

    except Exception as e:
        logging.error(str(e))
        print("Error:", e)


if __name__ == "__main__":
    main()