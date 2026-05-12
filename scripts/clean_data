import pandas as pd

# load original file
df = pd.read_csv("data/orders.csv")
print(df['status'].str.lower().value_counts())

# Clean and standardize status column
def normalize_status(status):
    status = str(status).strip().lower()

    # Success variations
    if status in ['success', 'suc']:
        return 'success'

    # Failed variations
    elif status in ['failed', 'fail']:
        return 'failed'

    # Refunded variations
    elif status in ['refunded','refunded ','ref']:
        return 'refunded'

    # Unknown values
    else:
        return 'unknown'

# Apply normalization and replace column values
df['status'] = df['status'].apply(normalize_status)

# View results
print(df['status'].value_counts())

df.to_csv("data/orders_fixed.csv", index=False)

