import pandas as pd
from src.utils.logger import logger

# Função para limpar e transformar os dados
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando limpeza de dados")
    df = df.drop_duplicates()
    df = df.dropna(subset=["API", "Description"])
    logger.info(f"Limpeza concluída: {len(df)} registros válidos")
    return df

if __name__ == "__main__":
    from src.extract.api_extract import extract_api
    df = extract_api()
    df_clean = clean_data(df)
    print(df_clean.head())
