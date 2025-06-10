import pandas as pd
from database import sqlite_connection

conn, cursor_obj = sqlite_connection()

# Read the CSV files
orders_df = pd.read_csv("data/orders.csv")
aisles_df = pd.read_csv("data/aisles.csv")
products_df = pd.read_csv("data/products.csv")
departments_df = pd.read_csv("data/departments.csv")


def ingest_to_sqlite(df, table_name):
    try:
        df.to_sql(name=table_name, con=conn, if_exists='replace')
        print(f"The Dataframe of {df.head()} load to '{table_name}' ")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

ingest_to_sqlite(df=departments_df, table_name="departments")