# src/data_collection.py

import pandas as pd

def collect_data(source):
    """Collect data from a CSV file."""
    df = pd.read_excel(source)
    return df

def save_data(df, path):
    """Save the collected DataFrame to a specified path."""
    df.to_csv(path, index=False)

if __name__ == "__main__":
    # Example usage
    data_source = 'data/raw/data.csv'
    collected_data = collect_data(data_source)
    save_data(collected_data, 'data/processed/collected_data.csv')
