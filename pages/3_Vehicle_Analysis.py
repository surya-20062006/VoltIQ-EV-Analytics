import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Vehicle Analysis",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Vehicle Analysis")
st.markdown("Analyze EV vehicle categories and types.")

# Load Data
df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

# Sidebar Filter
st.sidebar.header("Filters")

selected_category = st.sidebar.multiselect(
    "Select Vehicle Category",
    options=df["Vehicle_Category"].unique(),
    default=df["Vehicle_Category"].unique()
)

filtered_df = df[
    df["Vehicle_Category"].isin(selected_category)
]

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"{filtered_df['EV_Sales_Quantity'].sum():,}"
    )

with col2:
    st.metric(
        "Vehicle Categories",
        filtered_df["Vehicle_Category"].nunique()
    )

with col3:
    st.metric(
        "Vehicle Types",
        filtered_df["Vehicle_Type"].nunique()
    )

st.divider()

# Vehicle Category Distribution
st.subheader("📊 Vehicle Category Distribution")

category_sales = (
    filtered_df
    .groupby("Vehicle_Category")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_sales,
    names="Vehicle_Category",
    values="EV_Sales_Quantity",
    hole=0.5,
    title="Vehicle Category Share"
)

st.plotly_chart(
    fig_category,
    use_container_width=True,
    key="vehicle_category"
)

# Vehicle Type Analysis
st.subheader("🚙 Vehicle Type Analysis")

type_sales = (
    filtered_df
    .groupby("Vehicle_Type")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

type_sales = type_sales.sort_values(
    by="EV_Sales_Quantity",
    ascending=False
)

fig_type = px.bar(
    type_sales,
    x="EV_Sales_Quantity",
    y="Vehicle_Type",
    orientation="h",
    title="Vehicle Type Sales"
)

st.plotly_chart(
    fig_type,
    use_container_width=True,
    key="vehicle_type"
)

# Category vs Type
st.subheader("📈 Category vs Vehicle Type")

fig_scatter = px.scatter(
    filtered_df,
    x="Vehicle_Category",
    y="EV_Sales_Quantity",
    color="Vehicle_Type",
    title="Vehicle Category vs Sales"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True,
    key="vehicle_scatter"
)

# Data Table
st.subheader("📋 Vehicle Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Vehicle Data",
    csv,
    file_name="vehicle_analysis.csv",
    mime="text/csv"
)