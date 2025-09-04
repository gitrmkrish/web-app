import yfinance as yf
import streamlit as st

st.header("Stock Market Analysis by Murali")
st.write('')

import datetime

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter the start_date", datetime.date(2019, 7, 6))
with col2:
    end_date = st.date_input("Enter the end_date", datetime.date(2019, 7, 6))

#text input

title = st.text_input("Name of stock you want to see, (e.g AAPL , GOOGL)")
#st.write("The Stock Price Data of", title)

if title:
    data = yf.Ticker(title)

    ticker_df = data.history(start = start_date , end = end_date)

    st.write('showing details of')


    st.dataframe(ticker_df)

    st.line_chart(ticker_df['Close'])