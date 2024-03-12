import pandas as pd
import numpy as np
import sys

from src.exceptions import CustomException
from src.logger import logging


class CleaningData:
    """
    _summary_:

    """

    logging.info("Inside Data cleaning class.")

    def __init__(self, df:pd.DataFrame) -> None:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_
        """
        logging.info('Initializer initialized.')
        self.df = df


    def Step_01_workclass(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info("Inside step 01 of data cleaning.")

        try:
            logging.info("replacing `?` with private.")
            df['workclass'] = df['workclass'].replace(" ?", " Private")

            logging.info("removing extra space from workclass data values.")
            df['new_workclass'] = [i[-1] for i in df['workclass'].str.split(" ")]

            logging.info("dropping the workclass column.")
            df_new = df.drop(['workclass'], axis = 'columns')

            logging.info("step 1 completed.")

            return df_new

        except Exception as e:
            logging.info("Step 01 of data cleaning failed.")
            raise CustomException(e, sys)


    def Step_02_education(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

        logging.info("Inside step 02 of data cleaning.")

        try:
            logging.info("removing extra space from education data values.")
            df['new_education'] = [i[1] for i in df['education'].str.split(" ")]

            logging.info("dropping the older education columns")
            df_new = df.drop(['education'], axis = 'columns')

            logging.info('step 02 of data cleaning completed.')
            return df_new

        except Exception as e:
            logging.info("Step 02 of data cleaning failed.")
            raise CustomException(e, sys)


    def step_03_marital_status(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

        logging.info("Inside the step 03 of data cleaning.")

        try:
            logging.info("removing extra space from marital-status columns values.")
            df['new_marital_status'] = [i[1] for i in df['marital-status'].str.split(" ")]

            logging.info("dropping the old marital-status column")
            df_new = df.drop(['marital-status'], axis = 'columns')

            logging.info("step 03 of data cleaning completed.")

            return df_new

        except Exception as e:
            logging.info("step 03 of data cleaning failed.")
            raise CustomException(e, sys)


    def step_04_occupation(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

        logging.info("Inside step 04 of data cleaning.")

        try:
            logging.info("replacing the `?` with `Prof-specialty`")
            df['occupation'] = df['occupation'].replace(" ?", " Prof-specialty")

            logging.info("removing extra space from the data values.")
            df["new_occupation"] = [i[1] for i in df['occupation'].str.split(" ")]

            logging.info("droppig the old occupation column.")
            df_new = df.drop(['occupation'], axis = 'columns')

            logging.info("step 04 of data cleaning completed.")

            return df_new

        except Exception as e:
            logging.info("step 04 of data cleaning completed.")
            raise CustomException(e, sys)


    def step_05(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_:

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

        logging.info("Inside step 05 of data cleaning.")

        try:
            logging.info("dropping non related columns.")
            df_new = df.drop(['fnlwgt', 'education-num', 'relationship', 'race', 'sex', 'native-country'], axis = 'columns')

            logging.info('step 05 of data cleaning completed')

            return df_new

        except Exception as e:
            logging.info('Step 05 of data cleaning completed.')
            raise CustomException(e, sys)

    def step_06(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function is created for removing the extra space from the data values of income column.

        Args:
            df (pd.DataFrame): data set containing the income column with the extra space in data values.

        Returns:
            pd.DataFrame: cleaned dataframe with new income column.
        """

        logging.info("Inside the step 06 of data cleaning.")

        try:
            logging.info("removing extra space from the values of the income column.")

            df['income'] = [i[1] for i in df['income'].str.split(" ")]

            logging.info("removing extra space from the values of the income column completed.")

            return df

        except Exception as e:
            logging.info("step 06 of data cleaning failed.")
            raise CustomException(e, sys)

