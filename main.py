import time
import os
from dotenv import load_dotenv
from loguru import logger

from src.api.extract.api_extract import extract_api
from src.api.transform.api_transform import transform_api
from src.api.saver.api_saver import save_api

from src.bot.extract.bot_extract import extract_bot
from src.bot.transform.bot_transform import transform_bot
from src.bot.saver.bot_saver import save_bot

from db.db_connector import SQLDatabaseConnector

# Load environment variables
load_dotenv()

def run_api_etl(sql_connector):
    logger.info("==== Starting API ETL ====")
    df_api = extract_api()
    df_api_clean = transform_api(df_api)
    # Inserção no banco usando SQLDatabaseConnector
    for _, row in df_api_clean.iterrows():
        sql_connector.execute_query_from_file("db/queries/insert.sql", params=list(row))
    logger.info("==== API ETL completed ====")

def run_bot_etl(sql_connector):
    logger.info("==== Starting Bot ETL ====")
    # df_bot = extract_bot()  # colocar arquivo Excel de teste
    # df_bot_clean = transform_bot(df_bot)
    # for _, row in df_bot_clean.iterrows():
    #     sql_connector.execute_query_from_file("db/queries/insert.sql", params=list(row))
    logger.info("==== Bot ETL completed ====")

def main():
    # Inicializa conector usando variáveis do .env
    sql_connector = SQLDatabaseConnector(
        server=os.getenv("SQL_SERVER"),
        database=os.getenv("SQL_DATABASE"),
        use_windows_auth=False,
        username=os.getenv("SQL_USERNAME"),
        password=os.getenv("SQL_PASSWORD")
    )
    sql_connector.connect()

    # Rodar cada fluxo ETL
    run_api_etl(sql_connector)
    run_bot_etl(sql_connector)

    sql_connector.disconnect()

if __name__ == "__main__":
    main()
