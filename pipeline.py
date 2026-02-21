import logging
from extract import extract_api, extract_customers
from transform import transform_data
from load import load_data
from config.config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    try:
        logging.info("Pipeline started")

        df_api = extract_api()
        df_customers = extract_customers()

        df_final = transform_data(df_api, df_customers)

        load_data(df_final)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        print(e)

if __name__ == "__main__":
    run_pipeline()