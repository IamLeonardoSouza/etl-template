"""
Unit tests for Bot transformation functions.
"""

import pandas as pd
import pytest
from src.bot.transform.bot_transform import transform_bot

def test_transform_bot(mock_bot_dataframe):
    """
    Test that transform_bot removes duplicates and fills N/A values.
    """
    df = transform_bot(mock_bot_dataframe)
    assert isinstance(df, pd.DataFrame)
    assert df.duplicated().sum() == 0
    assert df.isna().sum().sum() == 0  # no NaN values
