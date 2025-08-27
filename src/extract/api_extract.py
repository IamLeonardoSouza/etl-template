import requests
import pandas as pd
from src.utils.logger import logger
import yaml

# Função para extrair dados de uma API pública
def extract_api(config_path="config/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    endpoint = config["api"]["endpoint"]

    logger.info(f"Iniciando extração de dados da API: {endpoint}")
    response = requests.get(endpoint, timeout=config["api"]["timeout"])
    data = response.json()
    
    df = pd.DataFrame(data.get("entries", []))
    logger.info(f"Extração concluída: {len(df)} registros")
    return df

if __name__ == "__main__":
    df = extract_api()
    print(df.head())
