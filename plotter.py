import seaborn as sns
import matplotlib.pyplot as plt
import stockpicker

def get_stock_plot(ticker: str):
    """
    Takes a stock ticker `ticker` and returns a SeaBorn plot
    of its closing price over the last 100 days.
    """
    #df = stockpicker.fetch_stock_data(ticker)
    df = stockpicker.fetch_stock_data(ticker)
    plot = sns.scatterplot(data=df, x='Date', y='Close').get
    return plot.get_figure()

# KEY = 'LDPU7YT97H89MWHQ'
# SYMBOL = 'IBM'

# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=60min&apikey={KEY}'
# # r = requests.get(url)
# # data = r.json()

# with open('IBM.json') as f:
#     data = json.load(f)
#     # df = pd.json_normalize(data)
#     df = pd.DataFrame(columns=['Date', 'Close'])
    
#     dates = list(data['Time Series (60min)'].keys())
#     closing_prices = [float(data['Time Series (60min)'][t]['4. close']) for t in dates]
#     dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

#     df.Date, df.Close = dates, closing_prices

#     sns.scatterplot(data=df, x='Date', y='Close')
#     plt.show()

#     print(df)

# df = pd.read_csv('question5.csv')
# print(df.head)

# plt.yscale('log')
# plot = sns.scatterplot(data=df.query('`Job created` <= 50'), x='Job created', y='Total Savings')