import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📈 Sales Analysis")

df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

year_sales = (
    df.groupby("Year")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig = px.line(
    year_sales,
    x="Year",
    y="EV_Sales_Quantity",
    markers=True,
    title="Year-wise EV Sales"
)

st.plotly_chart(fig, use_container_width=True)