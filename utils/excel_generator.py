import pandas as pd
from io import BytesIO


def generate_excel(df):
    """
    Convert filtered dataframe to an Excel file in memory.
    """

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Business Data")

    output.seek(0)

    return output
