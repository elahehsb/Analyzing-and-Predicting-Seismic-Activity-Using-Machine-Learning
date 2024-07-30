import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://user:password@localhost:5432/seismic_data')

def process_seismic_data(file_path):
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'])
    return df

def store_data_to_db(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Process and store data
seismic_data = process_seismic_data('data/seismic_data.csv')
store_data_to_db(seismic_data, 'seismic_data')
