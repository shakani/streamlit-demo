import seaborn as sns
import matplotlib.pyplot as plt
import stockpicker

def get_stock_plot(ticker: str, use_API: bool = True):
    """
    Takes a stock ticker `ticker` and returns a SeaBorn plot
    of its closing price over the last 100 days.
    """
    df = stockpicker.fetch_stock_data(ticker, use_API=use_API)
    plot = sns.scatterplot(data=df, x='Date', y='Close')
    return plot

if __name__ == '__main__':
    plot = get_stock_plot('IBM', use_API=False)
    plt.show()