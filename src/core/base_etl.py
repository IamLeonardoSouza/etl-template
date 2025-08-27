"""
Module: base_etl
Provides a BaseETL class for building ETL pipelines.

This module defines a generic ETL pipeline base class that can be
extended for specific data sources (API, RPA/Bot, CSV, etc.).
It includes structured logging, standardized method signatures, 
and a template for extract, transform, and load processes.
"""

import pandas as pd
from abc import ABC, abstractmethod
from loguru import logger
from typing import Optional


class BaseETL(ABC):
    """
    Abstract base class for ETL pipelines.

    Attributes:
        name (str): Name of the ETL process.
        data (Optional[pd.DataFrame]): Data loaded and processed during the ETL pipeline.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the BaseETL instance.

        Args:
            name (str): A descriptive name for the ETL process.
        """
        self.name = name
        self.data: Optional[pd.DataFrame] = None

    @abstractmethod
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the source system.

        Returns:
            pd.DataFrame: Raw data extracted from the source.
        """
        pass

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform raw data into a processed format.

        Args:
            df (pd.DataFrame): Raw data to transform.

        Returns:
            pd.DataFrame: Transformed data ready for loading.
        """
        pass

    @abstractmethod
    def load(self, df: pd.DataFrame) -> None:
        """
        Load the transformed data into the target system.

        Args:
            df (pd.DataFrame): Transformed data to load.
        """
        pass

    def run(self) -> None:
        """
        Execute the full ETL pipeline: extract, transform, and load.

        This method provides structured logging for each step
        and assigns the processed data to `self.data`.
        """
        logger.info(f"==== Starting ETL: {self.name} ====")
        try:
            # Extract
            raw_data = self.extract()
            logger.info(f"[{self.name}] Extracted {len(raw_data)} rows.")

            # Transform
            processed_data = self.transform(raw_data)
            logger.info(f"[{self.name}] Transformation completed.")

            # Load
            self.load(processed_data)
            logger.info(f"[{self.name}] Load completed successfully.")

            # Store processed data
            self.data = processed_data

            logger.success(f"==== ETL {self.name} finished successfully! ====")

        except Exception as e:
            logger.exception(f"ETL {self.name} failed: {e}")
            raise
