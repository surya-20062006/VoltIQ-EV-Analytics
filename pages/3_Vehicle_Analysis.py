import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚗 Vehicle Analysis")

df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

category = (
    df.groupby("Vehicle_Category")
    ["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig = px.pie(
    category,
    names="Vehicle_Category",
    values="EV_Sales_Quantity",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)