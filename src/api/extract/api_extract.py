"""
Module: api_extract
Provides functions to extract data from an external API.

This module reads configuration from a YAML file, executes HTTP requests to the API,
and returns the extracted data as a pandas DataFrame.

Dependencies:
    - requests: For HTTP requests to the API.
    - pandas: For data handling and conversion.
    - pyyaml: For reading configuration files.
"""

import requests
import pandas as pd
import yaml
from typing import Optional
from src.utils.logger import logger


def extract_api(config_path: str = "config/config.yaml") -> pd.DataFrame:
    """
    Extract data from an external API and return it as a pandas DataFrame.

    Reads the API endpoint and timeout configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file. Defaults to "config/config.yaml".

    Returns:
        pd.DataFrame: Extracted data as a DataFrame. Returns an empty DataFrame if no entries are found.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        KeyError: If required keys are missing in the configuration file.
        requests.RequestException: If the HTTP request fails.
        ValueError: If the response JSON is invalid or missing expected data.
    """
    try:
        # Load API configuration
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        endpoint = config["api"]["endpoint"]
        timeout = config["api"].get("timeout", 30)

    except FileNotFoundError as e:
        logger.exception(f"Configuration file not found: {config_path}")
        raise e
    except KeyError as e:
        logger.exception(f"Missing configuration key: {e}")
        raise e

    try:
        logger.info(f"Starting data extraction from API: {endpoint}")
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        entries = data.get("entries", [])
        if not entries:
            logger.warning("No entries found in API response.")
        
        df = pd.DataFrame(entries)
        logger.info(f"Extraction completed successfully: {len(df)} records retrieved.")
        return df

    except requests.RequestException as e:
        logger.exception(f"HTTP request to API failed: {e}")
        raise e
    except ValueError as e:
        logger.exception(f"Invalid JSON response from API: {e}")
        raise e
