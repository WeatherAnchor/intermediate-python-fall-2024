import yfinance as yf
import pandas as pd
import streamlit as st
import datetime

msft = yf.Ticker("MSFT")

st.sidebar.title("MSFT DASHBOARD")

start_date = st.sidebar.date_input("Select Start Date", min_value=datetime.date(2000, 1, 1), max_value=datetime.date.today(), value=datetime.date(2012, 1, 1))

end_date = st.sidebar.date_input("Select End Date", min_value=datetime.date(2000, 1, 1), max_value=datetime.date.today(), value=datetime.date.today())

st.sidebar.button("DONE")
    
