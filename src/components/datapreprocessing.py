import pandas as pd
import numpy as np
import sys

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder

from src.exceptions import CustomException
from src.logger import logging


class DataPreprocessing:
    """
    Summary: This class encapsulates essential functions (methods) for conducting feature engineering on a dataset.

    Returns:
        pd.DataFrame: Returns a refined dataframe optimized for model building.
    """

    logging.info("Inside the DataPreprocessing function.")

    def __init__(self, df:pd.DataFrame) -> None:
        logging.info("DataPreprocessing function initialized.")

        self.data = df



    def step_01_Age(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Min-Max scaling to the 'age' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'age' column to be scaled.

        Returns:
            pd.DataFrame: A new DataFrame with the 'age' column values scaled using Min-Max scaling.
        """

        logging.info('Inside the step 01 of data preprocessing.')

        try:
            logging.info("initializing MinMaxScaler for age column.")

            age_scale = MinMaxScaler()

            age_scale.fit(df[['age']])

            df['age'] = age_scale.transform(df[['age']])

            logging.info('Step 01 of data preprocessing completed.')
            return df

        except Exception as e:
            logging.info('Step 01 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_02_capital_gain(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Min-Max scaling to the 'capital-gain' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'capital-gain' column to be scaled.

        Returns:
            pd.DataFrame: A new DataFrame with the 'capital-gain' column values scaled using Min-Max scaling.
        """


        logging.info('Inside the step 02 of data preprocessing.')

        try:
            logging.info("initializing MinMaxScaler for capital gain column.")

            capital_gain_scale = MinMaxScaler()

            capital_gain_scale.fit(df[['capital-gain']])

            df['capital-gain'] = capital_gain_scale.transform(df[['capital-gain']])

            logging.info('Step 02 of data preprocessing completed.')

            return df

        except Exception as e:
            logging.info('Step 02 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_03_capital_loss(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Min-Max scaling to the 'capital-loss' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'capital-loss' column to be scaled.

        Returns:
            pd.DataFrame: A new DataFrame with the 'capital-loss' column values scaled using Min-Max scaling.
        """

        logging.info('Inside the step 03 of data preprocessing.')

        try:
            logging.info("initializing MinMaxScaler for capital loss column.")

            captial_loss_scale = MinMaxScaler()

            captial_loss_scale.fit(df[['capital-loss']])

            df['capital-loss'] = captial_loss_scale.transform(df[['capital-loss']])

            logging.info('Step 03 of data preprocessing completed.')

            return df

        except Exception as e:
            logging.info('Step 03 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_04_hours_per_week(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Standard scaling to the 'hours-per-week' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'hours-per-week' column to be scaled.

        Returns:
            pd.DataFrame: A new DataFrame with the 'hours-per-week' column values scaled using Standard scaling.
        """

        logging.info('Inside the step 04 of data preprocessing.')

        try:
            logging.info('Initializing StandardScaler for hours-per-week column.')

            hours_per_week_scale = StandardScaler()

            hours_per_week_scale.fit(df[['hours-per-week']])

            df['hours-per-week'] = hours_per_week_scale.transform(df[['hours-per-week']])

            logging.info('Step 04 of data preprocessing completed.')

            return df

        except Exception as e:
            logging.info('Step 04 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_05_target(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Label encoding to the 'target(income)' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'target(income)' column to be ecoded.

        Returns:
            pd.DataFrame: A new DataFrame with the 'target(income)' column values scaled using Label encoding.
        """

        logging.info('Inside the step 05 of data preprocessing.')

        try:
            logging.info('Initializing LabelEncoder for target(income) column.')

            Lb_encoder = LabelEncoder()

            Lb_encoder.fit(['<=50K', '>50K'])

            df['target'] = Lb_encoder.transform(df['income'])

            df_new = df.drop(['income'], axis = 'columns')

            logging.info('Step 05 of data preprocessing completed.')

            return df_new

        except Exception as e:
            logging.info('Step 05 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_06_education(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies Ordinal encoding to the 'education' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'education' column to be encoded.

        Returns:
            pd.DataFrame: A new DataFrame with the 'education' column values scaled using Ordinal encoding.
        """

        logging.info('Inside the step 06 of data preprocessing.')

        try:
            logging.info('Initializing OrdinalEncoder for education column.')

            order = [['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad', 'Some-college', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Masters', 'Doctorate', 'Prof-school']]

            ord_enc = OrdinalEncoder(categories = order)

            ord_enc.fit(df[['new_education']])

            df['new_education'] = ord_enc.transform(df[['new_education']])

            logging.info('Step 06 of data preprocessing completed.')

            return df

        except Exception as e:
            logging.info('Step 06 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_07_encoding(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function applies OneHot encoding to the 'workclass' and 'occupation' column in the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing the 'workclass' and 'occupation' column to be encoded.

        Returns:
            pd.DataFrame: A new DataFrame with the 'workclass' and 'occupation' column values scaled using OneHot encoding.
        """

        logging.info('Inside the step 07 of data preprocessing.')

        try:
            logging.info('Initializing OneHotEncoder for Encoding columns.')

            ohe = OneHotEncoder(drop='first', sparse_output=False, dtype=np.float32)

            ohe.fit(df[['new_workclass', 'new_occupation']])

            Encoded_values = ohe.transform(df[['new_workclass', 'new_occupation']])

            feature_names = ohe.get_feature_names_out(input_features=['new_workclass', 'new_occupation'])

            new_encoded_dataframe = pd.DataFrame(Encoded_values, columns=feature_names)

            df1 = pd.concat([df, new_encoded_dataframe], axis = 'columns')

            df2 = df1.drop(['new_workclass', 'new_occupation', 'new_marital_status'], axis = 'columns')

            logging.info('Step 07 of data preprocessing completed.')

            return df2

        except Exception as e:
            logging.info('Step 07 of data preprocessing failed.')
            raise CustomException(e, sys)



    def step_08_restructuring(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        _summary_: This function is designed to rearrange the order of columns within a dataset.

        """
        logging.info("Inside the step 08 of the Data Preprocessing.")

        try:
            new_order = ['age', 'new_education', 'new_workclass_Local-gov',
                         'new_workclass_Never-worked', 'new_workclass_Private',
                         'new_workclass_Self-emp-inc', 'new_workclass_Self-emp-not-inc',
                         'new_workclass_State-gov', 'new_workclass_Without-pay',
                         'new_occupation_Armed-Forces', 'new_occupation_Craft-repair',
                         'new_occupation_Exec-managerial', 'new_occupation_Farming-fishing',
                         'new_occupation_Handlers-cleaners', 'new_occupation_Machine-op-inspct',
                         'new_occupation_Other-service', 'new_occupation_Priv-house-serv',
                         'new_occupation_Prof-specialty', 'new_occupation_Protective-serv',
                         'new_occupation_Sales', 'new_occupation_Tech-support',
                         'new_occupation_Transport-moving','capital-gain', 'capital-loss',
                         'hours-per-week', 'target']

            df_new = df[new_order]

            logging.info("Restructuring completed.")

            return df_new

        except Exception as e:
            logging.info("step 08 of preprocessing failed.")
            raise CustomException(e, sys)


