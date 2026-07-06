import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df
