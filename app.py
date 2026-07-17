import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------
# Page Configuration
# --------------------
st.set_page_config(
    page_title="Amazon Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --------------------
# Load Data
# --------------------
df = pd.read_csv("dataset/amazon_sales.csv")

# --------------------
# Sidebar
# --------------------
st.sidebar.title("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Filter data
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# --------------------
# Dashboard Title
# --------------------
st.title("🛒 Amazon Sales Dashboard")

# --------------------
# KPI Cards
# --------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("📦 Total Orders", len(filtered_df))
col3.metric("🛍️ Products Sold", filtered_df["Quantity"].sum())
col4.metric("📈 Average Sale", f"${filtered_df['Sales'].mean():,.2f}")
st.markdown("---")

st.subheader("📊 Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    text_auto=True
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
st.subheader("🏆 Top 10 Best-Selling Products")

top_products = (
    filtered_df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x="Product",
    y="Sales",
    color="Product",
    text_auto=True
)

st.plotly_chart(fig4, use_container_width=True)
st.subheader("🥧 Sales by Region")

region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.pie(
    region_sales,
    values="Sales",
    names="Region",
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)
st.markdown("---")
st.subheader("📈 Monthly Sales Trend")

# Convert Order_Date to datetime
filtered_df["Order_Date"] = pd.to_datetime(filtered_df["Order_Date"])

# Create Month-Year column
filtered_df["Month"] = filtered_df["Order_Date"].dt.strftime("%b-%Y")

# Monthly sales
monthly_sales = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)
st.markdown("---")
st.subheader("💳 Payment Method Analysis")

payment_sales = (
    filtered_df.groupby("Payment_Method")["Sales"]
    .sum()
    .reset_index()
)

fig5 = px.pie(
    payment_sales,
    values="Sales",
    names="Payment_Method",
    hole=0.5
)

st.plotly_chart(fig5, use_container_width=True)
st.markdown("---")
st.subheader("🌍 Region-wise Performance")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig6 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    text_auto=True
)

st.plotly_chart(fig6, use_container_width=True)
st.markdown("""
<style>
.big-font{
    font-size:35px;
    font-weight:bold;
    color:#FF9900;
}

div[data-testid="stMetric"]{
    background-color:#f7f7f7;
    padding:15px;
    border-radius:10px;
    border:1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🛒 Amazon Sales Dashboard</p>', unsafe_allow_html=True)
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)