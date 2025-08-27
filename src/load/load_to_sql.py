from src.utils.db_connector import get_db_engine
from src.transform.data_cleaning import clean_data
from src.extract.api_extract import extract_api
from src.utils.logger import logger

# Função principal para executar o processo ETL completo
def load_to_db():
    logger.info("Iniciando processo de ETL completo")
    df = extract_api()
    df_clean = clean_data(df)
    
    engine = get_db_engine()
    df_clean.to_sql("etl_demo", engine, if_exists="replace", index=False)
    logger.info("Carregamento concluído no banco de dados")

if __name__ == "__main__":
    load_to_db()
