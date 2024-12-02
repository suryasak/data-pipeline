from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.transform_data import transform
from scripts.load_data import load

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 1),
    'retries': 1,
}

dag = DAG(
    'ecommerce_etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline for processing e-commerce data',
    schedule_interval='@daily',
)

def extract():
    print("Extracting data from raw_transactions.csv")
    with open('data/raw_transactions.csv', 'r') as file:
        data = file.readlines()
    return data

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
