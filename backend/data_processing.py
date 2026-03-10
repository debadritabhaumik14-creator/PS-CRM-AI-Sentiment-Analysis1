import pandas as pd
from sentiment_model import analyze_sentiment

def process_data(file_path):
    df = pd.read_csv(file_path)
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    return df
