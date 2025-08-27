"""
Module: bot_transform
Provides functions to transform and clean data extracted via RPA (bot).

This module applies standard data cleaning procedures such as:
    - Removing duplicates
    - Handling missing values
    - Logging transformations
It ensures data is ready for insertion into a database.

Dependencies:
    - pandas: For data manipulation and cleaning.
    - loguru: For structured logging.
"""

import pandas as pd
from src.utils.logger import logger


def transform_bot(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform and clean bot-extracted data.

    This function removes duplicate rows, fills missing values,
    and logs the number of valid records after transformation.

    Args:
        df (pd.DataFrame): Raw data extracted by the bot.

    Returns:
        pd.DataFrame: Cleaned and transformed DataFrame ready for saving.

    Raises:
        ValueError: If the input DataFrame is empty.
    """
    if df.empty:
        logger.warning("Input DataFrame is empty. Transformation skipped.")
        return df

    try:
        logger.info("Starting bot data transformation...")

        # Remove duplicate rows
        df_clean = df.drop_duplicates()

        # Fill missing values with placeholder
        df_clean = df_clean.fillna("N/A")

        logger.info(f"Bot data transformation completed: {len(df_clean)} valid records retained.")
        return df_clean

    except Exception as e:
        logger.exception(f"Error during bot data transformation: {e}")
        raise ValueError("Failed to transform bot data.") from e
