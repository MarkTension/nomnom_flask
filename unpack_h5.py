import numpy as np
import pandas as pd
import h5py
import tables
from sqlalchemy import create_engine
import sqlite3


def read_p5():
  """
  get hdf5 into pandas dataframe
  """
  # filename = 'data/res_info_adam.h5'
  filename = 'data/no_images.h5' # read file w/o images

  df = pd.read_hdf(filename) # put into df
  # columns = df.columns.values.tolist()

  # drop images from db
  # df2 = df.drop(['Images'], axis=1)

  """
  save to file
  """
  # save db without images to hdf5
  # df2.to_hdf('data/no_images.h5', key='df', mode='w')
  # df2.to_csv('data/no_images.csv',index=True)

  # columns_after = df2.columns.values.tolist() # check if images is deleted


  return df


def make_sql(df):
  """
  save to sqlite
  """

  disk_engine = create_engine('sqlite:///data/restaurants_v1.db')
  df.to_sql('restaurants_no_image', disk_engine, if_exists='append')

  # read from database example
  dfer = pd.read_sql_query('SELECT * FROM restaurants_no_image LIMIT 3', disk_engine)
  dfer.head()
  columns_after = dfer.columns.values.tolist()

  print("workec")


df = read_p5()
make_sql(df)
