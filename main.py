from scripts.load_to_bigquery import upload_csv

def run():
    tables = {
        "data/orders.csv": "orders",
        "data/product_catalog.csv": "product_catalog",
        "data/clickstream_events_sample.csv": "events_sample",
        "data/customers.csv": "customers"
    }

    for file_path, table_name in tables.items():

        upload_csv(
            file_path,
            table_name
        )

    print("All tables uploaded successfully")

if __name__ == "__main__":
    run()