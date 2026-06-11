import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

# ---------------------------------
# PAGE TITLE
# ---------------------------------

st.title("🗺️ State Analysis")

# ---------------------------------
# KPI CARDS
# ---------------------------------

total_states = df["State"].nunique()

top_state = (
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .idxmax()
)

avg_sales = int(
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .mean()
)

col1, col2, col3 = st.columns(3)

col1.metric("🗺️ Total States", total_states)
col2.metric("🏆 Top State", top_state)
col3.metric("⚡ Avg EV Sales", f"{avg_sales:,}")

st.markdown("---")

# Top 10 States

top_states = (
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_top = px.bar(
    top_states,
    x="EV_Sales_Quantity",
    y="State",
    orientation="h",
    title="Top 10 EV States"
)

# Bottom 10 States

bottom_states = (
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .sort_values()
    .head(10)
    .reset_index()
)

fig_bottom = px.bar(
    bottom_states,
    x="EV_Sales_Quantity",
    y="State",
    orientation="h",
    title="Bottom 10 EV States"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig_top, use_container_width=True)

with right:
    st.plotly_chart(fig_bottom, use_container_width=True)

st.markdown("---")

st.subheader("📋 State Ranking")

ranking = (
    df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

ranking.index = ranking.index + 1

st.dataframe(ranking)

st.markdown("---")

st.subheader("🔍 Search State")

search = st.text_input("Enter State Name")

if search:
    result = df[
        df["State"].str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(result)