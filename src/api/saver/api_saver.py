"""
Module: api_saver
Provides functions to save API data into a SQL Server database using pyodbc.

This module uses SQLDatabaseConnector for database interactions.
It can create tables dynamically (simple template) and insert data from pandas DataFrames.

Dependencies:
    - pandas: For data handling.
    - loguru: For structured logging.
"""

from typing import Optional
import pandas as pd
from src.db.db_connector import SQLDatabaseConnector
from src.utils.logger import logger


def save_api(
    df: pd.DataFrame,
    sql_connector: SQLDatabaseConnector,
    table_name: str = "api_demo"
) -> None:
    """
    Save a pandas DataFrame into a SQL Server table.

    Args:
        df (pd.DataFrame): DataFrame containing the data to save.
        sql_connector (SQLDatabaseConnector): Connected database connector instance.
        table_name (str): Name of the target table in SQL Server. Defaults to "api_demo".

    Raises:
        ValueError: If DataFrame is empty.
        RuntimeError: If any database operation fails.
    """
    if df.empty:
        logger.warning(f"No data to save for table {table_name}. Operation skipped.")
        return

    try:
        logger.info(f"Starting to save data to table: {table_name}")

        # Create table dynamically (simple template)
        columns = ", ".join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
        create_table_sql = (
            f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name};"
            f"CREATE TABLE {table_name} ({columns});"
        )
        sql_connector.execute_query(create_table_sql)
        logger.debug(f"Table {table_name} created successfully.")

        # Insert rows
        insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(df.columns))})"
        for _, row in df.iterrows():
            sql_connector.execute_query(insert_sql, params=list(row))
        logger.success(f"Data saved successfully to table {table_name}")

    except Exception as e:
        logger.exception(f"Failed to save data to table {table_name}: {e}")
        raise RuntimeError(f"Failed to save data to table {table_name}") from e
