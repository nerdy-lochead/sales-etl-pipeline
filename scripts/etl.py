import pandas as pd
from sqlalchemy import create_engine

# Load data
df = pd.read_csv('/Users/oluwapelumisanusi/Desktop/sales-etl-pipeline/data/sales_data.csv')

# Transform data
df['total_price'] = df['quantity'] * df['price']
df['order_date'] = pd.to_datetime(df['order_date'])

# PostgreSQL connection
username = 'postgres'
password = 'yourpassword'
host = 'localhost'
port = '5432'
database = 'sales_db'

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load into PostgreSQL
df.to_sql('sales', engine, if_exists='replace', index=False)

print("ETL process completed successfully!")
