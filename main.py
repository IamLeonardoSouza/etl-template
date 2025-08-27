"""
Ponto de entrada do projeto ETL.
Orquestra a execução de API e Bot ETL.
"""

from src.api.extract.api_extract import extract_api
from src.api.transform.api_transform import transform_api
from src.api.saver.api_saver import save_api

from src.bot.extract.bot_extract import extract_bot
from src.bot.transform.bot_transform import transform_bot
from src.bot.saver.bot_saver import save_bot

from src.utils.logger import logger

def run_api_etl():
    logger.info("==== Iniciando ETL da API ====")
    df = extract_api()
    df_clean = transform_api(df)
    save_api(df_clean)
    logger.info("==== ETL da API concluído ====")

def run_bot_etl():
    logger.info("==== Iniciando ETL do Bot ====")
    # df = extract_bot()  # descomente quando tiver dados
    # df_clean = transform_bot(df)
    # save_bot(df_clean)
    logger.info("==== ETL do Bot concluído ====")

def main():
    run_api_etl()
    run_bot_etl()

if __name__ == "__main__":
    main()
