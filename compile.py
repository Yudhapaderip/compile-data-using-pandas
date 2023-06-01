import os
import pandas as pd

# data_file_folder = './' #nama folder data

df = []
for file in os.dir(data_file_folder):
    if file.endswith('.xlsx'):
        print('loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_file_folder, file), sheet_name = 'Data'))