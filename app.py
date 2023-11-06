"""Small example streamlit application."""
import streamlit as st
import plotter 

def app():
    """Define main application entry point."""
    ### SIDEBAR ###
    use_API = st.sidebar.checkbox('Use API?', value=False)

    st.title("Stock Picker")
    st.markdown("Enter a stock ticker to see its closing price data for the last 100 days.")
    stock_ticker = st.text_input('Stock Ticker (e.g. $IBM)', '$IBM')

    st.markdown(f'The stock you entered was {stock_ticker}')
    plot = plotter.get_stock_plot(stock_ticker, use_API=use_API)
    st.pyplot(plot.get_figure())
    

    #st.sidebar.markdown("""You can put things in the sidebar:
# * Like lists
# * Or other things""")

if __name__ == '__main__':
    app()
