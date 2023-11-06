import pandas as pd
import requests 
import datetime
import json
from dotenv import load_dotenv
import os 

load_dotenv() # loads environment variables
KEY = os.environ['API_KEY']

def parse_json(json_data):
    """
    Parses JSON string into Pandas DataFrame.
    """
    dates = list(json_data['Time Series (60min)'].keys())
    closing_prices = [float(json_data['Time Series (60min)'][t]['4. close']) for t in dates]
    dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

    df = pd.DataFrame(columns=['Date', 'Close'])
    df.Date, df.Close = dates, closing_prices
    return df 
        

def fetch_stock_data(ticker: str, use_API: bool = True):
    """
    Takes a stock ticker `ticker` and returns a DataFrame
    with the `Date` and `Close` price of the ticker.
    """
    if ticker[0] == '$':
        ticker = ticker[1:]

    if(use_API):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=60min&apikey={KEY}'
        r = requests.get(url)
        data = r.json()
        print(data)

        dates = list(data['Time Series (60min)'].keys())
        closing_prices = [float(data['Time Series (60min)'][t]['4. close']) for t in dates]
        dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

        df = pd.DataFrame(columns=['Date', 'Close'])
        df.Date, df.Close = dates, closing_prices

        return df
    
    else:
        with open('IBM.json') as f:
            data = json.load(f)
            return parse_json(data)


if __name__ == '__main__':
    print(fetch_stock_data('IBM', use_API=False))