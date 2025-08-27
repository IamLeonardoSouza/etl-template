from loguru import logger

# Configuração básica de logging
logger.add("logs/etl.log", rotation="1 MB", retention="7 days", level="INFO")
