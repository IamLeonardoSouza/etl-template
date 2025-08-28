"""
Integration test for the Bot ETL flow.
"""

import pytest
from src.bot.extract.bot_extract import extract_bot
from src.bot.transform.bot_transform import transform_bot
from src.bot.saver.bot_saver import save_bot
from unittest.mock import MagicMock

def test_bot_etl_integration(monkeypatch, mock_bot_dataframe):
    """
    Test the full ETL pipeline for bot data: extract -> transform -> save.
    """
    mock_conn = MagicMock()
    monkeypatch.setattr("src.db.db_connector.get_db_connection", lambda: mock_conn)

    df = extract_bot()
    df_clean = transform_bot(df)
    save_bot(df_clean, table_name="integration_test_bot")

    assert df_clean.shape[0] > 0
    assert mock_conn.cursor().execute.called
    assert mock_conn.commit.called
