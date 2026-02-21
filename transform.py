import pandas as pd
import logging

def transform_data(df_api, df_customers):
    logging.info("Starting transformation")

    # Rename columns (schema mapping)
    df_api = df_api.rename(columns={
        "userId": "customer_id",
        "id": "order_id",
        "title": "product"
    })

    df_api = df_api[["order_id", "customer_id", "product"]]

    # Type validation
    df_api["order_id"] = pd.to_numeric(df_api["order_id"], errors="coerce")
    df_api["customer_id"] = pd.to_numeric(df_api["customer_id"], errors="coerce")

    # Remove invalid rows
    df_api = df_api.dropna(subset=["order_id", "customer_id"])

    # Remove duplicates
    df_api = df_api.drop_duplicates()

    # Merge (data enrichment)
    df_final = pd.merge(df_api, df_customers, on="customer_id", how="left")

    # Handle missing values
    df_final["name"] = df_final["name"].fillna("Unknown")
    df_final["city"] = df_final["city"].fillna("Unknown")

    logging.info(f"Transformation complete. Records: {len(df_final)}")

    return df_final