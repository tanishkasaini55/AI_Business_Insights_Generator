import pandas as pd
import plotly.express as px


def revenue_by_region_chart(df):
    """
    Creates a bar chart showing revenue by region.
    """

    revenue = (
        df.groupby("Region")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        revenue,
        x="Region",
        y="Total Revenue",
        color="Region",
        title="📈 Revenue by Region"
    )

    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Revenue ($)",
        template="plotly_dark"
    )

    return fig


# df.groupby("Region")["Total Revenue"].sum()
# Group all rows by Region and calculate the total revenue for each region."

def revenue_by_item_chart(df):

    revenue = (
        df.groupby("Item Type")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        revenue,
        names="Item Type",
        values="Total Revenue",
        title="🥧 Revenue by Item Type"
    )

    fig.update_layout(template="plotly_dark")

    return fig



def top_countries_chart(df):

    revenue = (
        df.groupby("Country")["Total Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        revenue,
        x="Country",
        y="Total Revenue",
        color="Country",
        title="🌍 Top 10 Countries by Revenue"
    )

    fig.update_layout(
        template="plotly_dark",
        showlegend=False
    )

    return fig

def monthly_revenue_chart(df):

    temp_df = df.copy()

    temp_df["Order Date"] = pd.to_datetime(
        temp_df["Order Date"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["Order Date"])

    temp_df["Month"] = temp_df["Order Date"].dt.strftime("%b-%Y")

    revenue = (
        temp_df.groupby("Month")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue,
        x="Month",
        y="Total Revenue",
        markers=True,
        title="📈 Monthly Revenue Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Month",
        yaxis_title="Revenue ($)"
    )

    return fig

def sales_channel_chart(df):

    revenue = (
        df.groupby("Sales Channel")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        revenue,
        names="Sales Channel",
        values="Total Revenue",
        hole=0.5,
        title="🍩 Revenue by Sales Channel"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig

def units_sold_chart(df):

    units = (
        df.groupby("Item Type")["Units Sold"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        units,
        x="Item Type",
        y="Units Sold",
        color="Item Type",
        title="📦 Units Sold by Item Type"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Item Type",
        yaxis_title="Units Sold",
        showlegend=False
    )

    return fig

def order_priority_chart(df):

    priority = (
        df.groupby("Order Priority")
        .size()
        .reset_index(name="Orders")
    )

    fig = px.pie(
        priority,
        names="Order Priority",
        values="Orders",
        hole=0.45,
        title="🎯 Order Priority Distribution"
    )

    fig.update_layout(template="plotly_dark")

    return fig

def revenue_world_map(df):

    revenue = (
        df.groupby("Country")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.choropleth(
        revenue,
        locations="Country",
        locationmode="country names",
        color="Total Revenue",
        hover_name="Country",
        color_continuous_scale="Viridis",
        title="🌍 Revenue by Country"
    )

    fig.update_layout(
        template="plotly_dark",
        geo=dict(showframe=False, showcoastlines=True)
    )

    return fig

def profit_by_region_chart(df):

    # Create Profit column
    df["Profit"] = df["Total Revenue"] - df["Total Cost"]

    profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Region",
        y="Profit",
        color="Region",
        title="💹 Profit by Region"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Region",
        yaxis_title="Profit ($)",
        showlegend=False
    )

    return fig

def top_profit_countries_chart(df):

    # Create Profit column
    df["Profit"] = df["Total Revenue"] - df["Total Cost"]

    profit = (
        df.groupby("Country")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Country",
        y="Profit",
        color="Country",
        title="🏆 Top 10 Most Profitable Countries"
    )

    fig.update_layout(
        template="plotly_dark",
        showlegend=False,
        xaxis_title="Country",
        yaxis_title="Profit ($)"
    )

    return fig

