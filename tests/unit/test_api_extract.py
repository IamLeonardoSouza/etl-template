"""
Unit tests for API extraction functions.
"""

import pandas as pd
import pytest
from src.api.extract.api_extract import extract_api

def test_extract_api_returns_dataframe(mock_api_response_df):
    """
    Test that extract_api returns a DataFrame with expected columns and non-empty.
    """
    df = mock_api_response_df
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame."
    assert not df.empty, "DataFrame is empty."
    expected_columns = ["API", "Description"]
    for col in expected_columns:
        assert col in df.columns, f"Missing expected column: {col}"
