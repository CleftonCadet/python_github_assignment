# The purpose of this script is to clean sales data for analysis. 

import pandas as pd

import pathlib # Importing pathlib to handle file paths

def load_data(file_path: str):
    return pd.read_csv(file_path)  # Loading data from the specified file path so we can clean it 

# Clean data 

# 1. Standardizes column names (lowercase, no spaces) for consistency
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

# 2. Removes leading/trailing whitespace from product and category names to ensure data consistency.
def strip_text_columns(df, columns):
    df = df.copy()
    for col in columns:
        df[col] = df[col].astype(str).str.strip()
    return df

df_clean = strip_text_columns(df_clean, ["product_name", "category"])


# 3. Handles missing prices and quantities to avoid calculation errors for analysis.
 def handle_missing_values(df):
    df['price'].fillna(df['price'].median(), inplace=True)
    df['quantity'].fillna(0, inplace=True)
    return df

# 4. Removes rows with negative prices or quantities since they are invalid for analysis.
def remove_invalid_rows(df):
    df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]
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