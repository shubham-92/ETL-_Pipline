import logging
from config.config import OUTPUT_ORDERS, OUTPUT_CUSTOMERS

def load_data(df):
    logging.info("Loading data")

    # Customers table
    customers = df[["customer_id", "name", "city"]].drop_duplicates()

    # Orders table
    orders = df[["order_id", "customer_id", "product"]]

    customers.to_csv(OUTPUT_CUSTOMERS, index=False)
    orders.to_csv(OUTPUT_ORDERS, index=False)

    logging.info("Data saved as relational CSV tables")
    print("Data saved successfully")