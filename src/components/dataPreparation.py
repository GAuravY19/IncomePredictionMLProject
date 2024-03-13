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
        Summary : Load the dataset from a specified path, assign column names, and convert it to a pandas DataFrame.

        Args:
            path (str): The path to the raw data file (.data).

        Returns:
            pd.DataFrame: A DataFrame created from the .data file with assigned column names.
        """


        logging.info("Inside readingData function.")

        data = pd.read_csv(path,
                           sep = ",",
                           names=self.columns)

        logging.info("Inside readingData function completed.")

        return data

    logging.info("Data Preparing completed.")


# ----------------------------------------------------------------------------------------------------------------------



