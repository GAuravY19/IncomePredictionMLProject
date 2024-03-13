import pandas as pd
import numpy as np
import sys

from src.exceptions import CustomException
from src.logger import logging


class CleaningData:
    """
    Summary: This class encapsulates a set of methods designed to cleanse the dataframe, preparing it for subsequent experimentation and analysis.
    """

    logging.info("Inside Data cleaning class.")

    def __init__(self, df:pd.DataFrame) -> None:
        logging.info('Initializer initialized.')
        self.df = df


    def Step_01_workclass(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Summary: This function is designed to handle missing values and remove extra spaces in the 'workclass' column of the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'workclass' column.

        Returns:
            pd.DataFrame: A cleaned DataFrame with the 'workclass' column processed to replace NaN values and eliminate extra spaces.
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
        Summary: This function removes extra spaces from the 'education' column in the provided DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame with the 'education' column.

        Returns:
            pd.DataFrame: Cleaned DataFrame with processed 'education' column.

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
            Summary: This function removes extra spaces from the 'marital-status' column in the given DataFrame.

            Args:
                df (pd.DataFrame): The input DataFrame containing the 'marital-status' column.

            Returns:
                pd.DataFrame: A cleaned DataFrame with the 'marital-status' column processed.
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
        Summary: This function is designed to handle missing values and eliminate extra spaces in the 'occupation' column of a given DataFrame.

        Args:
            df (pd.DataFrame): The input dataframe containing the 'occupation' column.

        Returns:
            pd.DataFrame: A cleaned dataframe with the 'occupation' column processed.

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
        Summary:
            This function is designed to remove non-essential columns from a given DataFrame.

        Args:
            df (pd.DataFrame): The input dataframe containing the following columns:
                - 'fnlwgt': Final weight assigned to observations
                - 'education-num': Number of years of education
                - 'relationship': Relationship status
                - 'race': Ethnicity or race
                - 'sex': Gender
                - 'native-country': Country of origin

        Returns:
            pd.DataFrame: A modified dataframe containing only the essential columns.
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
        Summary: Removes extra spaces from the data values in the income column of the provided DataFrame.

        Args:
            df (pd.DataFrame): The dataset containing the income column with extra spaces in data values.

        Returns:
            pd.DataFrame: A cleaned DataFrame with the income column having spaces removed.
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

