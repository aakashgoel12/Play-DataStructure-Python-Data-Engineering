import os,glob,gc
import pandas as pd

def read_data(input_file_path, delimiter=",", skiprows=0):
    filename, file_extension = os.path.splitext(input_file_path)
    if file_extension == '.csv':
        try:
            texts = pd.read_csv(input_file_path, sep=delimiter, skiprows=skiprows, encoding="utf-8")
        except IOError:
            print("Could not read file {}", input_file_path)
            return None
    elif file_extension == '.xlsx' or file_extension == '.xls':
        try:
            texts = pd.read_excel(input_file_path, skiprows=skiprows, encoding="utf-8")
        except IOError:
            print("Could not read file {}", input_file_path)
            return None
    try:
        gc.collect()
        return texts
    except:
        print("Please input file in {} or {} format".format('.csv', '.xlsx'))
        return None
