import os
import shutil

from src.exceptions import CustomException
from src.logger import logging

def MoveData(source_folder:str, destination_folder:str, file_name:str) -> None:
    logging.info("Moving of dataset started.")

    if not os.path.exists(source_folder):
        logging.info("Source folder does not exists.")
        return None

    if not os.path.exists(destination_folder):
        logging.info("Destination folder does not exists. Creating a new folder")
        os.makedirs(destination_folder)

    files_list = os.listdir(source_folder)

    found = False

    for files in files_list:

        if files == file_name:
            found = True

            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(destination_folder, file_name)

            logging.info("Moving of files started.")
            shutil.move(source_file, destination_file)
            logging.info("Moving of files completed.")

    if found == False:
        logging.info(f"{file_name} not found.")

    logging.info("Moving of dataset completed.")

