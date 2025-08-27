import pandas as pd
from src.utils.logger import logger

# Função para transformar dados do bot
def transform_bot(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transformação de dados do bot.
    """
    logger.info("Iniciando transformação de dados do bot")
    df = df.drop_duplicates()
    df = df.fillna("N/A")
    logger.info(f"Transformação concluída: {len(df)} registros")
    return df
