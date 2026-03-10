import streamlit as st
import pandas as pd

st.title("PS‑CRM Sentiment Dashboard")

data = pd.read_csv("../data/sample_data.csv")

st.write(data)
