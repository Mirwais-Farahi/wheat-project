# src/data_quality.py

def check_missing_values(df):
    """Check for missing values in the DataFrame."""
    return df.isnull().sum()

def check_duplicates(df):
    """Check for duplicate rows in the DataFrame."""
    return df.duplicated().sum()

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('data/processed/collected_data.csv')
    print("Missing Values:\n", check_missing_values(df))
    print("Duplicate Rows:", check_duplicates(df))
