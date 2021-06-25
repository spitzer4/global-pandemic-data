import pandas as pd
import numpy as np

data_frame = pd.read_csv('data/covid-data.csv')
# data_frame.head()

columns_to_drop = ['Total Cases/1 mil population', 'Death/1 mil population', 'Total Cases.1', 'Tests/1 mil population']
data_frame.drop(columns=columns_to_drop, inplace=True)