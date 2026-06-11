import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Business Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Insights")
st.markdown("Key insights from the Indian EV Market.")

# Load Data
df = pd.read_csv("data/processed/cleaned_ev_sales.csv")

# Calculate Insights
top_state = (
    df.groupby("State")["EV_Sales_Quantity"]
    .sum()
    .idxmax()
)

top_state_sales = (
    df.groupby("State")["EV_Sales_Quantity"]
    .sum()
    .max()
)

top_category = (
    df.groupby("Vehicle_Category")["EV_Sales_Quantity"]
    .sum()
    .idxmax()
)

top_category_sales = (
    df.groupby("Vehicle_Category")["EV_Sales_Quantity"]
    .sum()
    .max()
)

top_vehicle = (
    df.groupby("Vehicle_Type")["EV_Sales_Quantity"]
    .sum()
    .idxmax()
)

top_vehicle_sales = (
    df.groupby("Vehicle_Type")["EV_Sales_Quantity"]
    .sum()
    .max()
)

total_sales = df["EV_Sales_Quantity"].sum()

total_states = df["State"].nunique()

total_categories = df["Vehicle_Category"].nunique()

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total EV Sales",
        f"{total_sales:,}"
    )

with col2:
    st.metric(
        "States Covered",
        total_states
    )

with col3:
    st.metric(
        "Vehicle Categories",
        total_categories
    )

st.divider()

# Business Insights

st.success(
    f"🏆 {top_state} has the highest EV registrations with {top_state_sales:,} units."
)

st.info(
    f"🚗 {top_category} is the leading EV category with {top_category_sales:,} registrations."
)

st.warning(
    f"⚡ {top_vehicle} is the most popular vehicle type with {top_vehicle_sales:,} sales."
)

# Top 10 States

st.subheader("🏅 Top 10 States")

top_states = (
    df.groupby("State")["EV_Sales_Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.table(top_states)

# Recommendations

st.subheader("📌 Business Recommendations")

st.markdown("""
### 1. Expand Infrastructure
- Focus charging stations in high-growth states.

### 2. Promote Leading Categories
- Increase investments in the fastest-growing EV segments.

### 3. Support Low Adoption States
- Launch awareness campaigns and subsidies.

### 4. Manufacturer Opportunities
- Target regions with increasing EV demand.

### 5. Future Growth
- Strengthen policies for sustainable transportation.
""")

# Raw Data

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)