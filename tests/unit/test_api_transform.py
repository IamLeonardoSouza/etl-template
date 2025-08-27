"""
Unit tests for API transformation functions.
"""

import pandas as pd
import pytest
from src.api.transform.api_transform import transform_api

def test_transform_api(mock_api_response_df):
    """
    Test that transform_api removes duplicates and drops rows with null values.
    """
    df = transform_api(mock_api_response_df)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.duplicated().sum() == 0
    required_cols = ["API", "Description"]
    for col in required_cols:
        assert df[col].notna().all()
