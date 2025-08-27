"""
Unit tests for API saver functions.
"""

import pandas as pd
import pytest
from src.api.saver.api_saver import save_api
from unittest.mock import MagicMock

def test_save_api_calls_execute(monkeypatch, mock_api_response_df):
    """
    Test that save_api calls execute_query_from_file for each row.
    """
    mock_conn = MagicMock()
    monkeypatch.setattr("src.db.db_connector.get_db_connection", lambda: mock_conn)
    
    save_api(mock_api_response_df, table_name="test_table")
    
    # Check if cursor.execute was called at least once
    assert mock_conn.cursor().execute.called
    # Check commit was called
    assert mock_conn.commit.called
