"""
Unit tests for Bot saver functions.
"""

import pandas as pd
import pytest
from src.bot.saver.bot_saver import save_bot
from unittest.mock import MagicMock

def test_save_bot_calls_execute(monkeypatch, mock_bot_dataframe):
    """
    Test that save_bot calls execute_query_from_file for each row.
    """
    mock_conn = MagicMock()
    monkeypatch.setattr("src.db.db_connector.get_db_connection", lambda: mock_conn)
    
    save_bot(mock_bot_dataframe, table_name="test_table")
    
    assert mock_conn.cursor().execute.called
    assert mock_conn.commit.called
