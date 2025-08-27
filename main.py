"""
Module: main
Entry point for executing ETL pipelines for API and Bot data sources.

This script loads environment variables, initializes the SQL database connection,
and orchestrates the execution of multiple ETL processes (API ETL and Bot ETL)
using structured logging and error handling.

Dependencies:
    - python-dotenv: For loading environment variables from a .env file.
    - loguru: For structured logging.
    - pandas: For data handling in ETL pipelines.
"""

import os
from dotenv import load_dotenv
from loguru import logger
import sys

from src.api.extract.api_extract import extract_api
from src.api.transform.api_transform import transform_api
from src.api.saver.api_saver import save_api

from src.bot.extract.bot_extract import extract_bot
from src.bot.transform.bot_transform import transform_bot
from src.bot.saver.bot_saver import save_bot

from db.db_connector import SQLDatabaseConnector


def run_api_etl(sql_connector: SQLDatabaseConnector) -> None:
    """
    Execute the ETL pipeline for API data source.

    Args:
        sql_connector (SQLDatabaseConnector): Connected SQLDatabaseConnector instance.
    """
    logger.info("==== Starting API ETL ====")
    try:
        df_api = extract_api()
        df_api_clean = transform_api(df_api)

        for _, row in df_api_clean.iterrows():
            sql_connector.execute_query_from_file("db/queries/insert.sql", params=list(row))

        logger.success("==== API ETL completed successfully ====")
    except Exception as e:
        logger.exception(f"API ETL failed: {e}")
        raise


def run_bot_etl(sql_connector: SQLDatabaseConnector) -> None:
    """
    Execute the ETL pipeline for Bot/RPA data source.

    Args:
        sql_connector (SQLDatabaseConnector): Connected SQLDatabaseConnector instance.
    """
    logger.info("==== Starting Bot ETL ====")
    try:
        # Uncomment and implement when Bot ETL is ready
        # df_bot = extract_bot()
        # df_bot_clean = transform_bot(df_bot)
        # for _, row in df_bot_clean.iterrows():
        #     sql_connector.execute_query_from_file("db/queries/insert.sql", params=list(row))

        logger.success("==== Bot ETL completed successfully ====")
    except Exception as e:
        logger.exception(f"Bot ETL failed: {e}")
        raise


def main() -> None:
    """
    Main function to initialize the SQL connector and run ETL pipelines.

    Steps:
        1. Load environment variables from .env.
        2. Initialize SQLDatabaseConnector with credentials.
        3. Connect to the database.
        4. Run API ETL and Bot ETL pipelines.
        5. Disconnect from the database.
    """
    load_dotenv()

    try:
        sql_connector = SQLDatabaseConnector(
            server=os.getenv("SQL_SERVER"),
            database=os.getenv("SQL_DATABASE"),
            use_windows_auth=False,
            username=os.getenv("SQL_USERNAME"),
            password=os.getenv("SQL_PASSWORD"),
        )
        sql_connector.connect()
    except Exception as e:
        logger.critical(f"Failed to initialize database connection: {e}")
        sys.exit(1)

    try:
        run_api_etl(sql_connector)
        run_bot_etl(sql_connector)
    except Exception as e:
        logger.error(f"ETL execution halted due to error: {e}")
    finally:
        sql_connector.disconnect()
        logger.info("Database connection closed.")


if __name__ == "__main__":
    main()
