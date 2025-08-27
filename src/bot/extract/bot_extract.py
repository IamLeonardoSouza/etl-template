"""
Module: bot_extract
Provides functions to extract data using RPA techniques (e.g., Selenium) or reading files.

This module supports multiple extraction strategies:
    - Reading data from Excel/CSV files
    - Future extension to web scraping or automation via Selenium

Dependencies:
    - pandas: For data handling and conversion.
    - loguru: For structured logging.
    - openpyxl / xlrd: For reading Excel files.
"""

import pandas as pd
from typing import Optional
from src.utils.logger import logger
import os


def extract_bot(file_path: str = "data/bot_data.xlsx") -> pd.DataFrame:
    """
    Extract data using a bot simulation (RPA) or from a local file.

    Args:
        file_path (str): Path to the input file (Excel). Defaults to "data/bot_data.xlsx".

    Returns:
        pd.DataFrame: Extracted data as a DataFrame. Returns empty DataFrame if file is not found.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file content cannot be read properly.
    """
    try:
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        logger.info(f"Starting bot data extraction from file: {file_path}")
        df = pd.read_excel(file_path)
        logger.info(f"Extraction completed successfully: {len(df)} records retrieved.")

        return df

    except FileNotFoundError as e:
        raise e
    except Exception as e:
        logger.exception(f"Failed to extract bot data from {file_path}: {e}")
        raise ValueError(f"Failed to extract bot data from {file_path}") from e
