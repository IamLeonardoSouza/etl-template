"""
Module: api_transform
Provides functions to transform and clean data extracted from an API.

This module applies standard data cleaning procedures such as
removing duplicates, handling missing values, and ensuring
the data is ready for insertion into a database.

Dependencies:
    - pandas: For data manipulation and cleaning.
    - loguru: For structured logging.
"""

import pandas as pd
from src.utils.logger import logger


def transform_api(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform and clean API data.

    This function removes duplicate rows, handles missing values in key columns,
    and logs the number of valid records after transformation.

    Args:
        df (pd.DataFrame): Raw data extracted from the API.

    Returns:
        pd.DataFrame: Cleaned and transformed DataFrame ready for saving.

    Raises:
        ValueError: If the input DataFrame is empty.
    """
    if df.empty:
        logger.warning("Input DataFrame is empty. Transformation skipped.")
        return df

    try:
        logger.info("Starting API data transformation...")

        # Remove duplicate rows
        df_clean = df.drop_duplicates()

        # Drop rows with missing values in important columns
        required_columns = ["API", "Description"]
        missing_cols = [col for col in required_columns if col not in df_clean.columns]
        if missing_cols:
            logger.warning(f"Missing expected columns: {missing_cols}. They will be skipped in cleaning.")

        cols_to_check = [col for col in required_columns if col in df_clean.columns]
        df_clean = df_clean.dropna(subset=cols_to_check)

        logger.info(f"API data transformation completed: {len(df_clean)} valid records retained.")
        return df_clean

    except Exception as e:
        logger.exception(f"Error during API data transformation: {e}")
        raise ValueError("Failed to transform API data.") from e
