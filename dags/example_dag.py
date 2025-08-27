from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from src.load.load_to_sql import load_to_db

# Define the DAG
with DAG(
    "etl_demo_dag",
    start_date=datetime(2025, 8, 27),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    run_etl = BashOperator(
        task_id="run_etl",
        python_callable=load_to_db
    )
