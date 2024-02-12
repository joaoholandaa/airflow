from airflow import DAG
from datetime import datetime

from airflow.operators.python import PythonOperator

def hello():
    print("Hello World")

with DAG('test', start_date = datetime(2024, 1, 12),
        schedule_interval = '30 * * * *', catchup = False) as dag:

    helloWorld = PythonOperator(
        task_id = 'Hello_World',
        python_callable = hello
    )  

    helloWorld