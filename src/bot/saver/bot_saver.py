"""
Module: bot_saver
Provides functions to save bot-extracted data into a SQL Server database using pyodbc.

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


def save_bot(
    df: pd.DataFrame,
    sql_connector: SQLDatabaseConnector,
    table_name: str = "bot_demo"
) -> None:
    """
    Save bot-extracted data from a pandas DataFrame into a SQL Server table.

    Args:
        df (pd.DataFrame): DataFrame containing the bot-extracted data.
        sql_connector (SQLDatabaseConnector): Connected database connector instance.
        table_name (str): Name of the target table in SQL Server. Defaults to "bot_demo".

    Raises:
        ValueError: If DataFrame is empty.
        RuntimeError: If any database operation fails.
    """
    if df.empty:
        logger.warning(f"No bot data to save for table {table_name}. Operation skipped.")
        return

    try:
        logger.info(f"Starting to save bot data to table: {table_name}")

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
        logger.success(f"Bot data saved successfully to table {table_name}")

    except Exception as e:
        logger.exception(f"Failed to save bot data to table {table_name}: {e}")
        raise RuntimeError(f"Failed to save bot data to table {table_name}") from e
