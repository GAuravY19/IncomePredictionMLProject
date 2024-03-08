import pandas as pd
import numpy as np

from src.logger import logging

class DataPrepare:
    """
    _summary_:This class will make the dataset ready for use.

    Returns:
        pd.DataFrame: A new dataframe that can be further used for different processes.
    """

    logging.info("Inside Data Preparaing class.")

    def __init__(self) -> None:
        # initializing the function with different column names.
        self.columns = ['age', 'workclass', 'fnlwgt',
                        'education', 'education-num',
                        'marital-status', 'occupation',
                        'relationship', 'race', 'sex',
                        'capital-gain', 'capital-loss',
                        'hours-per-week', 'native-country', 'income']



    def readingData(self, path:str) -> pd.DataFrame:
        """
        _summary_: This function loads the dataset, adds column names to it and then converts it to pandas Dataframe.

        Args:
            path (str): path where the raw data is stored.

        Returns:
            pd.DataFrame: A dataframe which is converted from .data file to pandas Dataframe with added column names.
        """

        logging.info("Inside readingData function.")

        data = pd.read_csv(path,
                           sep = ",",
                           names=self.columns)

        logging.info("Inside readingData function completed.")

        return data

    logging.info("Data Preparing completed.")


# ----------------------------------------------------------------------------------------------------------------------



