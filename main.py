import os
import shutil
import pandas as pd
import numpy as np

from src.utils.movedata import MoveData
from src.utils.savedata import SavingData
from src.components.dataPreparation import DataPrepare
from src.components.dataclean import CleaningData
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


clean = CleaningData(df)

df1 = clean.Step_01_workclass(df)
df2 = clean.Step_02_education(df1)
df3 = clean.step_03_marital_status(df2)
df4 = clean.step_04_occupation(df3)
df5 = clean.step_05(df4)
df6 = clean.step_06(df5)

SavingData(df6, location=FILE_LOCATION, file_name="clean_data.csv")


print("main file completed working.")
