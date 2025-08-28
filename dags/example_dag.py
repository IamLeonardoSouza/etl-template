"""
ETL Demo DAG
------------

This DAG executes the ETL pipeline using Airflow. It supports
both API and Bot (RPA) sources, leveraging the modular ETL template.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.core.base_etl import run_api_etl, run_bot_etl
from src.db.db_connector import SQLDatabaseConnector
import os
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env
load_dotenv()

# Default DAG arguments
default_args = {
    "owner": "Leonardo Souza",
    "depends_on_past": False,
    "email_on_failure": True,
    "email": [os.getenv("ALERT_EMAIL", "you@example.com")],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2025, 8, 27),
}

# Function to initialize DB connector
def get_db_connector() -> SQLDatabaseConnector:
    """
    Initialize the SQLDatabaseConnector using environment variables.
    Returns:
        SQLDatabaseConnector: Connected database instance
    """
    connector = SQLDatabaseConnector(
        server=os.getenv("SQL_SERVER"),
        database=os.getenv("SQL_DATABASE"),
        use_windows_auth=False,
        username=os.getenv("SQL_USERNAME"),
        password=os.getenv("SQL_PASSWORD"),
    )
    connector.connect()
    return connector

# Python callable to run the full ETL
def run_full_etl():
    """
    Execute the ETL pipeline for both API and Bot sources.
    """
    sql_connector = get_db_connector()
    try:
        logger.info("==== Starting ETL pipeline ====")
        # Run API ETL
        run_api_etl(sql_connector)
        # Run Bot ETL
        run_bot_etl(sql_connector)
        logger.info("==== ETL pipeline completed successfully ====")
    finally:
        sql_connector.disconnect()

# Define the DAG
with DAG(
    dag_id="etl_demo_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="DAG to run the professional ETL template for API and Bot sources",
    tags=["etl", "template", "portfolio"],
) as dag:

    run_etl_task = PythonOperator(
        task_id="run_full_etl",
        python_callable=run_full_etl,
        dag=dag,
    )
