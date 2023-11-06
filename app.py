"""Small example streamlit application."""
import streamlit as st
import plotter 

def app():
    """Define main application entry point."""
    st.title("Stock Picker")
    # And write the rest of the app inside this function!
    st.markdown("Enter a stock ticker to see its closing price data for the last 100 days.")
#     st.markdown("""Streamlit works more on the basis of 
# \"insert things and let Streamlit figure out how to render 
# them\".  If you want more flexibility for how to render
# the markdown and other elements on your webpage, 
# you may want to consider
# [Flask](https://flask.palletsprojects.com/).""")
    # st.markdown("Here's another line of text")
    stock_ticker = st.text_input('Stock Ticker (e.g. $APPL)', '$APPL')
    st.markdown(f'The stock you entered was {stock_ticker}')

    st.pyplot(plotter.plot.get_figure())

    st.sidebar.markdown("""You can put things in the sidebar:
* Like lists
* Or other things""")

if __name__ == '__main__':
    app()
