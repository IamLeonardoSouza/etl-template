from sqlalchemy import create_engine
import yaml

# Função para obter a engine de conexão com o banco de dados
def get_db_engine(config_path="config/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    db = config["database"]
    conn_str = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['db_name']}"
    engine = create_engine(conn_str)
    return engine
