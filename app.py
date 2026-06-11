import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VoltIQ",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ VoltIQ - EV Market Analysis")
st.subheader("Analyzing the EV market trends and insights")

df = pd.read_csv("data/proceed/cleaned_ev_sales.csv")

# KPI Calculations
total_sales = df["EV_Sales_Quantity"].sum()
total_states = df["State"].nunique()
total_categories = df["Vehicle_Category"].nunique()
total_vehicle_types = df["Vehicle_Type"].nunique()
total_years = df["Year"].nunique()

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("⚡ Total EV Sales", f"{total_sales:,}")
col2.metric("🗺️ States", total_states)
col3.metric("🚗 Categories", total_categories)
col4.metric("🏭 Vehicle Types", total_vehicle_types)
col5.metric("📅 Years", total_years)

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("🔍 Filters")

# Year Filter
selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

# State Filter
selected_state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["State"].unique().tolist())
)

# Vehicle Category Filter
selected_category = st.sidebar.selectbox(
    "Select Vehicle Category",
    ["All"] + sorted(df["Vehicle_Category"].unique().tolist())
)

filtered_df = df.copy()

# Filter Year
filtered_df = filtered_df[
    filtered_df["Year"] == selected_year
]

# Filter State
if selected_state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]

# Filter Category
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Vehicle_Category"] == selected_category
    ]
