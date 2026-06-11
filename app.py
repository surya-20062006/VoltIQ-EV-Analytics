import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="VoltIQ",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_ev_sales.csv")

df = load_data()

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("⚡ VoltIQ - EV Market Analysis")
st.subheader("Analyzing the Indian EV market trends and insights")

st.markdown("---")

# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

total_sales = int(df["EV_Sales_Quantity"].sum())
total_states = df["State"].nunique()
total_categories = df["Vehicle_Category"].nunique()
total_vehicle_types = df["Vehicle_Type"].nunique()
total_years = df["Year"].nunique()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("⚡ Total EV Registrations", f"{total_sales:,}")
col2.metric("🗺️ States", total_states)
col3.metric("🚗 Categories", total_categories)
col4.metric("🏭 Vehicle Types", total_vehicle_types)
col5.metric("📅 Years", total_years)

st.markdown("---")

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("🔍 Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

selected_state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["State"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Select Vehicle Category",
    ["All"] + sorted(df["Vehicle_Category"].unique().tolist())
)

filtered_df = df.copy()

# Year Filter
filtered_df = filtered_df[
    filtered_df["Year"] == selected_year
]

# State Filter
if selected_state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]

# Category Filter
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Vehicle_Category"] == selected_category
    ]

st.write(selected_year)
st.write(selected_state)
st.write(selected_category)

st.write(filtered_df.head())
# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_ev_data.csv",
    mime="text/csv"
)

st.markdown("---")

# ---------------------------------------------------
# YEAR-WISE SALES TREND
# ---------------------------------------------------

year_sales = (
    df.groupby("Year")["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig_year = px.line(
    year_sales,
    x="Year",
    y="EV_Sales_Quantity",
    markers=True,
    title="📈 Year-wise EV Sales Trend"
)

st.plotly_chart(fig_year, use_container_width=True)

# ---------------------------------------------------
# TOP STATES
# ---------------------------------------------------
top_states = (
    filtered_df.groupby("State")
    ["EV_Sales_Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_state = px.bar(
    top_states,
    x="EV_Sales_Quantity",
    y="State",
    orientation="h",
    title="🗺️ Top 10 EV States"
)

fig_state.update_layout(height=450)

# ---------------------------------------------------
# VEHICLE CATEGORY
# ---------------------------------------------------

category_sales = (
    filtered_df.groupby("Vehicle_Category")
    ["EV_Sales_Quantity"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_sales,
    names="Vehicle_Category",
    values="EV_Sales_Quantity",
    title="🚗 Vehicle Category Distribution",
    hole=0.4
)

fig_category.update_layout(
    height=450,
    legend_title="Category"
)
# ---------------------------------------------------
# TWO COLUMN LAYOUT
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        fig_state,
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.markdown("---")

st.subheader("📌 Business Insights")

if not filtered_df.empty:

    top_state = (
        filtered_df.groupby("State")
        ["EV_Sales_Quantity"]
        .sum()
        .idxmax()
    )

    top_category = (
        filtered_df.groupby("Vehicle_Category")
        ["EV_Sales_Quantity"]
        .sum()
        .idxmax()
    )

    st.success(
        f"🏆 {top_state} has the highest EV registrations."
    )

    st.info(
        f"🚗 {top_category} dominates the EV market."
    )

    st.warning(
        "📈 The Indian EV market shows strong growth potential."
    )

else:
    st.error(
        "No data available for the selected filters."
    )

# ---------------------------------------------------
# SHOW FILTERED DATA
# ---------------------------------------------------

with st.expander("📋 View Filtered Dataset"):
    st.dataframe(filtered_df)

fig_year.update_layout(height=500)

fig_state.update_layout(height=450)

fig_category.update_layout(height=450)