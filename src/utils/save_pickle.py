import pickle
import os


def save_pickle_file(file_path:str, dataname):

    with open(f"{file_path}", "wb") as f:
        pickle.dump(dataname, f)

