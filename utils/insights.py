import pandas as pd

def calculate_kpis(df):
    """
    Calculate business KPIs from the uploaded dataset.
    """

    kpis = {
        "Total Revenue": df["Total Revenue"].sum(),
        "Total Cost": df["Total Cost"].sum(),
        "Units Sold": df["Units Sold"].sum(),
        "Countries": df["Country"].nunique(),
        "Categories": df["Item Type"].nunique()
    }

    return kpis


# We're creating a function named calculate_kpis().
#
# It receives the uploaded dataset (df) and returns a dictionary containing important business metrics