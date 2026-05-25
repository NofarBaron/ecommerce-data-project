from pathlib import Path
from google.cloud import bigquery
import pandas as pd
import os
from config import PROJECT_ID, DATASET

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Credentials path
credentials_path = (
    BASE_DIR /
    "credentials" /
    "service_account.json"
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credentials_path)

# BigQuery client
client = bigquery.Client()

def upload_csv(file_path, table_name):

    table_id = f"{PROJECT_ID}.{DATASET}.{table_name}"

    print(f"Loading {file_path}")

    df = pd.read_csv(file_path)

    job = client.load_table_from_dataframe(
        df,
        table_id
    )

    job.result()

    print(
        f"Loaded {len(df)} rows into {table_name}"
    )