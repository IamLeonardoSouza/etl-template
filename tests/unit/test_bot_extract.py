"""
Unit tests for Bot extraction functions.
"""

import pandas as pd
import pytest
from src.bot.extract.bot_extract import extract_bot

def test_extract_bot_returns_dataframe(mock_bot_dataframe):
    """
    Test that extract_bot returns a DataFrame with expected shape.
    """
    df = mock_bot_dataframe
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
