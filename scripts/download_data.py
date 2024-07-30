import requests
import os
import pandas as pd

def download_seismic_data():
    # Example URL for seismic data from USGS
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
    response = requests.get(url)
    with open('data/seismic_data.csv', 'wb') as file:
        file.write(response.content)

os.makedirs('data', exist_ok=True)
download_seismic_data()
