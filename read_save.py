import os,glob,gc
import pandas as pd
import pickle

## read either csv, xlsx file
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

## save either in csv, xlsx, pkl format
def save_data(data, output_file_path, encoding='utf-8',index_status=False):
    filename, file_extension = os.path.splitext(output_file_path)
    if file_extension == '.csv':
        try:
            data.to_csv(output_file_path, encoding=encoding, index=index_status)
        except Exception as e:
            print("Error in saving file: {}".format(e))
    elif file_extension == '.xlsx' or file_extension == '.xls':
        try:
            data.to_excel(output_file_path, encoding=encoding, index=index_status)
        except Exception as e:
            print("Error in saving file: {}".format(e))
    elif file_extension == '.pkl' or file_extension == '.pickle'
        try:
            with open(output_file_path,'wb') as f:
                pickle.dump(data,f)
                f.close()
        except Exception as e:
            print("Error in saving file: {}".format(e))