import streamlit as st
import pandas as pd
import base64
import requests

st.title("Read CSV from GitHub")

url = "https://raw.githubusercontent.com/JeffLau-byte/MachineLearning/main/grades.csv"

def load_data():
  return pd.read.csv(url)

try:
  df = load_data()
  st.success("Data loaded successfully!")
  st.dataframe(df)
except Exception as e:
  st.error(" Failed to Load Data")

">> https://github.com/settings/personal-access-tokens "
a = st.text_input("Enter a")
b = st.text_input("Enter b")
c = st.text_input("Enter c")
