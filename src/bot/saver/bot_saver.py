from src.db.db_connector import get_db_connection
from src.utils.logger import logger
import pandas as pd

# Função para salvar dados do bot no banco de dados
def save_bot(df: pd.DataFrame, table_name="bot_demo"):
    """
    Salva os dados extraídos do bot no SQL Server via pyodbc.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    columns = ", ".join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
    cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}")
    cursor.execute(f"CREATE TABLE {table_name} ({columns})")
    
    for _, row in df.iterrows():
        placeholders = ", ".join("?" for _ in df.columns)
        cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(row))
    
    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"Dados do bot salvos com sucesso na tabela {table_name}")
