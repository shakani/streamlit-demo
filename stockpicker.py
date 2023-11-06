import pandas as pd
import requests 
import datetime

KEY = 'LDPU7YT97H89MWHQ'

def fetch_stock_data(ticker: str):
    """
    Takes a stock ticker `ticker` and returns a DataFrame
    with the `Date` and `Close` price of the ticker.
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=60min&apikey={KEY}'
    r = requests.get(url)
    data = clean_json(r.json())

    dates = list(data['Time Series (60min)'].keys())
    closing_prices = [float(data['Time Series (60min)'][t]['4. close']) for t in dates]
    dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

    df = pd.DataFrame(columns=['Date', 'Close'])
    df.Date, df.Close = dates, closing_prices

    return df