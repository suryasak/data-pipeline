import pandas as pd

def transform(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(task_ids='extract_data')
    print("Transforming data")
    # Convert data into a DataFrame
    data = [line.strip().split(',') for line in raw_data[1:]]  # Skip header
    df = pd.DataFrame(data, columns=raw_data[0].strip().split(','))
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])
    # Save cleaned data
    df.to_csv('data/cleaned_transactions.csv', index=False)

