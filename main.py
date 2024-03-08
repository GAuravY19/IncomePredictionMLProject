import os
import shutil
import pandas as pd
import numpy as np

from src.utils.movedata import MoveData
from src.utils.savedata import SavingData
from src.components.dataPreparation import DataPrepare
from src.exceptions import CustomException
from src.logger import logging

SOURCE_FOLDER = "D:/Recipe"
DESTINATION_FOLDER = "D:/IncomeML Model/data/raw"
FILE_NAME = "adult.data"

MoveData(source_folder = SOURCE_FOLDER,
         destination_folder = DESTINATION_FOLDER,
         file_name = FILE_NAME)

prepare = DataPrepare()

PATH = os.path.join(DESTINATION_FOLDER, FILE_NAME)

df = prepare.readingData(path=PATH)

FILE_LOCATION = "D:/IncomeML Model/data/processed"
SavingData(df, location=FILE_LOCATION, file_name='data.csv')

print("main file completed working.")
