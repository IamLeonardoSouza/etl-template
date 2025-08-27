"""
Global fixtures for ETL tests.
"""

import pytest
import pandas as pd
import json
from pathlib import Path
from src.api.extract.api_extract import extract_api
from src.bot.extract.bot_extract import extract_bot

@pytest.fixture
def mock_api_response_df():
    """Return a mock DataFrame simulating API extraction."""
    mock_file = Path(__file__).parent / "mocks/mock_api_response.json"
    with open(mock_file, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data.get("entries", []))
    return df

@pytest.fixture
def mock_bot_dataframe():
    """Return a mock DataFrame simulating Bot extraction."""
    mock_file = Path(__file__).parent / "mocks/mock_bot_data.xlsx"
    df = pd.read_excel(mock_file)
    return df
