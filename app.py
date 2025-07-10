import streamlit as st
import pandas as pd
import base64
import request

st.title("Read CSV from GitHub")

url = "https://raw.githubusercontent.com/limfw/temp/main/data.csv"

def load_data():
  return pd.read.csv(url)

try:
  df = load_data()
  st.success("Data loaded successfully!")
  st.dataframe(df)
except Exception as e:
  st.error("Data Failed to Load!")
