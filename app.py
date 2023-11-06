"""Small example streamlit application."""
import streamlit as st
import plotter 

def app():
    """Define main application entry point."""
    ### SIDEBAR ###
    use_API = st.sidebar.checkbox('Use API?', value=False)

    st.title("Stock Picker")
    st.markdown("Enter a stock ticker to see its closing price data for the last 100 days.")
    st.markdown("Sample data for IBM is shown below. API calls are limited to 25 per day. Please check the box in the sidebar on the left to make an API call.")
    stock_ticker = st.text_input('Stock Ticker (e.g. $IBM)', '$IBM')

    st.markdown(f'The stock you entered was {stock_ticker}')
    plot = plotter.get_stock_plot(stock_ticker, use_API=use_API)
    st.pyplot(plot.get_figure())
    

    #st.sidebar.markdown("""You can put things in the sidebar:
# * Like lists
# * Or other things""")

if __name__ == '__main__':
    app()
