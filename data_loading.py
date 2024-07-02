import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('AB_NYC_2019.csv')

engine = create_engine('postgresql://postgres:post@localhost:5432/postgres')

df.to_sql('airbnb_nyc', engine, if_exists='replace', index=False)
query = 'SELECT * FROM airbnb_nyc'
df = pd.read_sql(query, engine)

df['last_review'] = pd.to_datetime(df['last_review'])
df['last_review_date'] = df['last_review'].dt.date
df['last_review_time'] = df['last_review'].dt.time

average_price_per_neighborhood = df.groupby('neighbourhood')['price'].mean().reset_index()
average_price_per_neighborhood.columns = ['neighbourhood', 'average_price']

df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

df.to_sql('airbnb_nyc_transformed', engine, if_exists='replace', index=False)
