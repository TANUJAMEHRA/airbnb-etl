import pandas as pd
from metaflow import FlowSpec, step
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:post@localhost:5432/postgres')


class AirbnbETLFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.extract)

    @step
    def extract(self):
        self.df = pd.read_sql('SELECT * FROM airbnb_nyc', engine)
        self.next(self.transform)

    @step
    def transform(self):
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])
        self.df['last_review_date'] = self.df['last_review'].dt.date
        self.df['last_review_time'] = self.df['last_review'].dt.time
        self.average_price_per_neighborhood = self.df.groupby('neighbourhood')['price'].mean().reset_index()
        self.average_price_per_neighborhood.columns = ['neighbourhood', 'average_price']
        self.df['reviews_per_month'] = self.df['reviews_per_month'].fillna(0)
        self.next(self.load)

    @step
    def load(self):
        self.df.to_sql('airbnb_nyc_transformed', engine, if_exists='replace', index=False)
        self.next(self.end)

    @step
    def end(self):
        print("ETL process completed successfully")


if __name__ == '__main__':
    AirbnbETLFlow()
