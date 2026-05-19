import pandas as pd

# load original file
df = pd.read_csv("ecommerce-data-project/data/clickstream_events.csv", sep=None, engine='python')

# take a subset (e.g. 100k rows)
df_sample = df.sample(n=100000, random_state=42)

# save smaller file
df_sample.to_csv("ecommerce-data-project/data/clickstream_events_sample.csv", index=False,encoding='utf-8')
print("Sample file created!")
print(df_sample.columns)
