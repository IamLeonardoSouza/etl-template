import pandas as pd
from src.utils.logger import logger

# Função para extrair dados simulando um bot (RPA)
def extract_bot(file_path="data/bot_data.xlsx"):
    """
    Extração de dados simulando um bot (RPA).
    """
    logger.info(f"Iniciando extração de dados do bot: {file_path}")
    df = pd.read_excel(file_path)
    logger.info(f"Extração concluída: {len(df)} registros")
    return df
