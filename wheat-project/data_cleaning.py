# src/data_cleaning.py

def clean_data(df):
    """Clean the DataFrame by removing missing values and duplicates."""
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    # Add more cleaning steps as necessary
    return df

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('data/processed/collected_data.csv')
    cleaned_data = clean_data(df)
    cleaned_data.to_csv('data/processed/cleaned_data.csv', index=False)
