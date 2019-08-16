import csv


import h5py
import pandas as pd


df = pd.read_csv("data/no_images.csv")
columns = df.columns.values.tolist()
preview = df.head()
dtypes = preview.dtypes
print('hi')

