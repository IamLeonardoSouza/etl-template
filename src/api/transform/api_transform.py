import pandas as pd
from src.utils.logger import logger

# Função para transformar e limpar os dados
def transform_api(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transformação e limpeza de dados da API.
    """
    logger.info("Iniciando transformação de dados da API")
    df = df.drop_duplicates()
    df = df.dropna(subset=["API", "Description"])
    logger.info(f"Transformação concluída: {len(df)} registros válidos")
    return df
