# The purpose of this script is to clean sales data for analysis. 

import pandas as pd

import pathlib # Importing pathlib to handle file paths

def load_data(file_path: str):
    return pd.read_csv(file_path)  # Loading data from the specified file path so we can clean it 

# Clean data 

# 1. Standardizes column names (lowercase, no spaces) for consistency
def clean_column_names(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


# 2. Removes leading/trailing whitespace from product and category names to ensure data consistency.
def strip_text_columns(df, columns):
    df = df.copy()
    for col in columns:
        df[col] = df[col].astype(str).str.strip()
    return df


# 3. Handles missing prices and quantities to avoid calculation errors for analysis.
def handle_missing_values(df):
    df = df.copy()

    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["price"].fillna(df["price"].median(), inplace=True)

    if "quantity" in df.columns:
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
        df["quantity"].fillna(0, inplace=True)

    return df


# 4. Removes rows with negative prices or quantities since they are invalid for analysis.
def remove_invalid_rows(df):
    df = df.copy()

    condition = pd.Series(True, index=df.index)

    if "price" in df.columns:
        condition = condition & (df["price"] >= 0)

    if "quantity" in df.columns:
        condition = condition & (df["quantity"] >= 0)

    df = df[condition]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())