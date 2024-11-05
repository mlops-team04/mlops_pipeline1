import pandas as pd

df = pd.read_parquet('/home/ubuntu/app/jupyter/api_call_table.parquet')
print(df.head())