import streamlit as st
import pandas as pd
import requests
from sqlalchemy import create_engine
from config import DB_URL
from datetime import datetime

# -----------------------
# Database Connection
# -----------------------
engine = create_engine(
    DB_URL,
    connect_args={"sslmode": "require"}
)

st.title("Data Ingestion & ETL Tool")

# -----------------------
# Input Source Selection
# -----------------------
source = st.radio("Select Data Source", ["Upload CSV", "API URL"])

df = None

# CSV Upload
if source == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

# API Input
elif source == "API URL":
    api_url = st.text_input("Enter API URL")
    if st.button("Fetch Data"):
        try:
            response = requests.get(api_url)
            data = response.json()
            df = pd.DataFrame(data)
        except:
            st.error("Invalid API or data format")

# -----------------------
# Process Data (only if data exists)
# -----------------------
if df is not None:

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    # Cleaning
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    df = df.drop_duplicates()

    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head())

    # -----------------------
    # Save Section
    # -----------------------
    st.subheader("Save Data")
    st.info(
        "Enter a base name. The system will create a timestamped table automatically to avoid overwriting previous uploads."
    )

    base_table_name = st.text_input("Base table name (example: insurance_data)")

    if st.button("Save to Neon"):
        if base_table_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_table_name = f"{base_table_name}_{timestamp}"

            df.to_sql(
                final_table_name,
                engine,
                if_exists="replace",
                index=False
            )

            st.success(f"Data saved as table: {final_table_name}")
        else:
            st.warning("Please enter a base table name")

    # -----------------------
    # Download Cleaned Data
    # -----------------------
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

# -----------------------
# Query Section
# -----------------------
st.markdown("---")
st.header("Query Data from Neon")

# Show tables
if st.button("Show Tables"):
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    tables = pd.read_sql(query, engine)
    st.dataframe(tables)

# SQL Query box
st.subheader("Run SQL Query")

user_query = st.text_area(
    "Enter SQL Query",
    placeholder="Example: SELECT * FROM your_table LIMIT 10"
)

if st.button("Run Query"):
    if user_query.strip() != "":
        try:
            result_df = pd.read_sql(user_query, engine)
            st.success("Query executed successfully")
            st.dataframe(result_df)

            # Download query result
            csv_result = result_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Query Result",
                data=csv_result,
                file_name="query_result.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Query failed: {e}")
    else:
        st.warning("Please enter a SQL query")