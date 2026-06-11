import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Sales Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 EV Sales Analysis")
st.markdown("Analyze yearly and monthly EV sales trends.")

# Load Data
df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

# Sidebar Filters
st.sidebar.header("Filters")

selected_year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

filtered_df = df[df["Year"].isin(selected_year)]

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total EV Sales",
        f"{filtered_df['EV_Sales_Quantity'].sum():,}"
    )

with col2:
    st.metric(
        "Average Sales",
        f"{filtered_df['EV_Sales_Quantity'].mean():.0f}"
    )

with col3:
    st.metric(
        "Years",
        filtered_df["Year"].nunique()
    )

st.divider()

# Yearly Sales Trend
st.subheader("📊 Year-wise EV Sales Trend")

yearly_sales = (
    filtered_df
    .groupby("Year")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig_year = px.line(
    yearly_sales,
    x="Year",
    y="EV_Sales_Quantity",
    markers=True,
    title="Year-wise EV Sales"
)

st.plotly_chart(
    fig_year,
    use_container_width=True,
    key="year_sales"
)

# Monthly Sales Trend
st.subheader("📅 Month-wise EV Sales")

monthly_sales = (
    filtered_df
    .groupby("Month_Name")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

month_order = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

monthly_sales["Month_Name"] = pd.Categorical(
    monthly_sales["Month_Name"],
    categories=month_order,
    ordered=True
)

monthly_sales = monthly_sales.sort_values("Month_Name")

fig_month = px.bar(
    monthly_sales,
    x="Month_Name",
    y="EV_Sales_Quantity",
    title="Monthly EV Sales"
)

st.plotly_chart(
    fig_month,
    use_container_width=True,
    key="month_sales"
)

# Data Table
st.subheader("📋 Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download Button
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Sales Data",
    csv,
    file_name="ev_sales_analysis.csv",
    mime="text/csv"
)