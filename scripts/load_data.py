import sqlite3
import pandas as pd

def load(**kwargs):
    print("Loading data into SQLite")
    # Load transformed data
    df = pd.read_csv('data/cleaned_transactions.csv')
    # Connect to SQLite database
    conn = sqlite3.connect('ecommerce.db')
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    conn.close()

