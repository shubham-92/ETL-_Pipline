import pandas as pd
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
CUSTOMER_FILE = "data/customers.csv"

def extract_api():
    print("Extracting orders from API...")
    response = requests.get(API_URL)
    data = response.json()
    df_api = pd.DataFrame(data)
    return df_api

def extract_customers():
    print("Extracting customers from CSV...")
    df_customers = pd.read_csv(CUSTOMER_FILE)
    return df_customers