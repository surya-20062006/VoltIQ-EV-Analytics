import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🗺️ State Analysis")

df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

top_states = (
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_states,
    x="EV_Sales_Quantity",
    y="State",
    orientation="h",
    title="Top 10 EV States"
)

st.plotly_chart(fig, use_container_width=True)