from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}


def hello_world():
    print("Hello world")


with DAG(
        default_args=default_args,
        dag_id='our_dag_with_python_operator_v01',
        description='DAG with PythonOperator',
        start_date=datetime(2021, 10, 6),
        schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=hello_world
    )


task1