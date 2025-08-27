from src.db.db_connector import get_db_connection
import pandas as pd
from src.utils.logger import logger

# Função para salvar dados no banco de dados
def save_api(df: pd.DataFrame, table_name="api_demo"):
    """
    Salva o DataFrame no SQL Server via pyodbc.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Criação da tabela (simples para template)
    columns = ", ".join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
    cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}")
    cursor.execute(f"CREATE TABLE {table_name} ({columns})")
    
    # Inserção dos dados
    for _, row in df.iterrows():
        placeholders = ", ".join("?" for _ in df.columns)
        cursor.execute(
            f"INSERT INTO {table_name} VALUES ({placeholders})",
            tuple(row)
        )
    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"Dados salvos com sucesso na tabela {table_name}")
