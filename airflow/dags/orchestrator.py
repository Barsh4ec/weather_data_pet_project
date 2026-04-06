from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

def example_task():
    print("This is an example task")

default_args = {
    "description": "A DAG to orchestrate data",
    "start_date": datetime(2026, 4, 6),
    "catchup": False
}

dag = DAG(
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=2)
)

with dag:
    task1 = PythonOperator(
        task_id="first_task",
        python_callable=example_task
    )