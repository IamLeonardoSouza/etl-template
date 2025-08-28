"""
Integration test for the API ETL flow.
"""

import pytest
from src.api.extract.api_extract import extract_api
from src.api.transform.api_transform import transform_api
from src.api.saver.api_saver import save_api
from unittest.mock import MagicMock

def test_api_etl_integration(monkeypatch, mock_api_response_df):
    """
    Test the full ETL pipeline: extract -> transform -> save.
    """
    # Mock DB connection
    mock_conn = MagicMock()
    monkeypatch.setattr("src.db.db_connector.get_db_connection", lambda: mock_conn)

    df = extract_api()
    df_clean = transform_api(df)
    save_api(df_clean, table_name="integration_test_table")

    assert df_clean.shape[0] > 0
    assert mock_conn.cursor().execute.called
    assert mock_conn.commit.called
