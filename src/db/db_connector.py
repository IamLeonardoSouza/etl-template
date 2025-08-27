import pyodbc
import yaml

def get_db_connection(config_path="config/config.yaml"):
    """
    Cria e retorna a conexão com o banco via pyodbc.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    db = config["database"]

    conn_str = (
        f"DRIVER={{SQL Server}};"
        f"SERVER={db['server']};"
        f"DATABASE={db['database']};"
        f"UID={db['user']};"
        f"PWD={db['password']}"
    )
    conn = pyodbc.connect(conn_str)
    return conn
