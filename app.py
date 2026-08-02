
from utils.charts import (
    revenue_by_region_chart,
    revenue_by_item_chart,
    top_countries_chart,
    monthly_revenue_chart,
    sales_channel_chart,
    units_sold_chart,
    order_priority_chart,
    revenue_world_map,
    profit_by_region_chart,
    top_profit_countries_chart
)

from utils.insights import calculate_kpis
from utils.ai import generate_ai_insights
from utils.report_generator import generate_pdf_report
from utils.excel_generator import generate_excel

import streamlit as st
import pandas as pd

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="AI Business Insights Generator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#0E1117;
}

/* KPI Cards */
div[data-testid="stMetric"]{
    background: linear-gradient(135deg,#1E293B,#111827);
    padding:20px;
    border-radius:15px;
    border:1px solid #374151;
    box-shadow:0px 4px 15px rgba(0,0,0,0.25);
    transition:0.3s ease;
}

div[data-testid="stMetric"]:hover{
    transform:translateY(-5px);
    border:1px solid #00C2FF;
    box-shadow:0px 8px 25px rgba(0,194,255,0.35);
}

/* Metric Label */
div[data-testid="stMetricLabel"]{
    font-size:18px;
    font-weight:600;
}

/* Metric Value */
div[data-testid="stMetricValue"]{
    font-size:32px;
    color:#00E5FF;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# Title
# ------------------------------
st.markdown("""
<h1 style='text-align:center;
color:#00E5FF;
font-size:55px;
margin-bottom:0px;'>
📊 AI Business Insights
</h1>

<h3 style='text-align:center;
color:#D1D5DB;
margin-top:0px;'>
AI Powered Business Intelligence Dashboard
</h3>

<p style='text-align:center;
font-size:18px;
color:#9CA3AF;'>

Analyze 📊 | Visualize 📈 | Discover Insights 🤖 | Make Better Decisions 💼

</p>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1E3A8A,#2563EB);
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">
        <h1>📊</h1>
        <h4>10 Charts</h4>
        <p>Interactive Visualizations</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#065F46,#10B981);
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">
        <h1>🤖</h1>
        <h4>AI Insights</h4>
        <p>Powered by Llama 3.3</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#7C2D12,#EA580C);
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">
        <h1>🌍</h1>
        <h4>Global Analysis</h4>
        <p>76 Countries Supported</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#581C87,#A855F7);
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">
        <h1>⚡</h1>
        <h4>Real-Time</h4>
        <p>Instant AI Analytics</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()




# ------------------------------
# File Upload
# ------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Business Dataset",
    type=["csv"],
    help="Upload any business CSV dataset"
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # ==========================
        # Sidebar Filters
        # ==========================
        st.sidebar.title("📊 AI Business Insights")

        st.sidebar.header("🎛 Dashboard Filters")

        if st.sidebar.button("🔄 Reset Filters"):
            st.rerun()

        st.sidebar.markdown("---")

        st.sidebar.subheader("📊 Dashboard Summary")

        st.sidebar.write(f"**Rows:** {len(df)}")
        st.sidebar.write(f"**Columns:** {df.shape[1]}")
        st.sidebar.write(f"**Countries:** {df['Country'].nunique()}")
        st.sidebar.write(f"**Regions:** {df['Region'].nunique()}")

        selected_region = st.sidebar.multiselect(
            "🌍 Select Region",
            options=sorted(df["Region"].unique())
        )

        if not selected_region:
            selected_region = sorted(df["Region"].unique())

        selected_country = st.sidebar.multiselect(
            "🏳️ Select Country",
            options=sorted(df["Country"].unique()),

        )
        # If no country is selected, use all countries
        if not selected_country:
            selected_country = sorted(df["Country"].unique())

        selected_item = st.sidebar.multiselect(
            "📦 Select Item Type",
            options=sorted(df["Item Type"].unique())
        )

        if not selected_item:
            selected_item = sorted(df["Item Type"].unique())

        selected_channel = st.sidebar.multiselect(
            "🛒 Sales Channel",
            options=sorted(df["Sales Channel"].unique())
        )

        if not selected_channel:
            selected_channel = sorted(df["Sales Channel"].unique())

        selected_priority = st.sidebar.multiselect(
            "🎯 Order Priority",
            options=sorted(df["Order Priority"].unique())
        )

        if not selected_priority:
            selected_priority = sorted(df["Order Priority"].unique())

        df = df[
             (df["Region"].isin(selected_region)) &
             (df["Country"].isin(selected_country)) &
             (df["Item Type"].isin(selected_item)) &
             (df["Sales Channel"].isin(selected_channel)) &
             (df["Order Priority"].isin(selected_priority))
        ]

        st.success("✅ Dataset Uploaded Successfully!")

        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

        st.subheader("📊 Dataset Statistics")

        kpis = calculate_kpis(df)

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("💰 Revenue", f"${kpis['Total Revenue']:,.2f}")
        col2.metric("💸 Cost", f"${kpis['Total Cost']:,.2f}")
        col3.metric("📦 Units Sold", f"{kpis['Units Sold']:,}")
        col4.metric("🌍 Countries", kpis["Countries"])
        col5.metric("📦 Categories", kpis["Categories"])

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📈 Revenue by Region")
            fig = revenue_by_region_chart(df)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("🥧 Revenue by Item Type")
            fig2 = revenue_by_item_chart(df)
            st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("🌍 Top 10 Countries")
            fig3 = top_countries_chart(df)
            st.plotly_chart(fig3, use_container_width=True)

        with col4:
            st.subheader("📈 Monthly Revenue Trend")
            fig4 = monthly_revenue_chart(df)
            st.plotly_chart(fig4, use_container_width=True)

        st.divider()

        col5, col6 = st.columns(2)

        with col5:
            st.subheader("🍩 Sales Channel Distribution")
            fig5 = sales_channel_chart(df)
            st.plotly_chart(fig5, use_container_width=True)

        with col6:
            st.subheader("📦 Units Sold by Item Type")
            fig6 = units_sold_chart(df)
            st.plotly_chart(fig6, use_container_width=True)

        st.divider()

        col7, col8 = st.columns(2)

        with col7:
            st.subheader("🎯 Order Priority Distribution")
            fig7 = order_priority_chart(df)
            st.plotly_chart(fig7, use_container_width=True)

        with col8:
            st.subheader("💹 Profit by Region")
            fig8 = profit_by_region_chart(df)
            st.plotly_chart(fig8, use_container_width=True)

        st.divider()

        col9, col10 = st.columns(2)

        with col9:
            st.subheader("🌍 Revenue by Country (World Map)")
            fig9 = revenue_world_map(df)
            st.plotly_chart(fig9, use_container_width=True)

        with col10:
            st.subheader("🏆 Top 10 Most Profitable Countries")
            fig10 = top_profit_countries_chart(df)
            st.plotly_chart(fig10, use_container_width=True)

        st.divider()

        st.subheader("🤖 AI Business Insights")

        if st.button("✨ Generate AI Insights"):
            with st.spinner("🤖 AI is analyzing your business data..."):
                insights = generate_ai_insights(df)

            st.success("✅ AI Analysis Completed!")

            st.markdown(insights)

            pdf_file = generate_pdf_report(kpis, insights)

            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="📥 Download Business Report (PDF)",
                    data=file,
                    file_name="Business_Report.pdf",
                    mime="application/pdf"
                )

            excel_file = generate_excel(df)

            st.download_button(
                label="📊 Download Filtered Dataset (Excel)",
                data=excel_file,
                file_name="Filtered_Business_Data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")













