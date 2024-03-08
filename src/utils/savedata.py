import os
import pandas as pd

from src.logger import logging

def SavingData(dataframe:pd.DataFrame, location:str, file_name:str) -> None:
    """
    _summary_:This function is created for saving the dataframe to desired location.

    Args:
        dataframe (pd.DataFrame): The dataframe that is to be saved.
        location (str): Location at which it will be saved.
        file_name (str): Name of the saving dataframe.
    """
    logging.info("Into Saving dataframe function.")

    if not os.path.exists(location):
        logging.info(f"`{location}` does not exists. Creating it.")
        os.makedirs(location)

    file_save_location = os.path.join(location, file_name)

    dataframe.to_csv(file_save_location, index=False)

    logging.info("Saving of Dataframe completed.")


