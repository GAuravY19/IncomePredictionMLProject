import pickle


def Load_picke_files(file_path:int):

    DATA = None

    with open(f"{file_path}", 'rb') as f:
        DATA = pickle.load(f)

    return DATA
