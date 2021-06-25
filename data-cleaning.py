import pandas as pd
import numpy as np


data_frame = pd.read_csv('data/covid-data.csv')

# Remove unnecessary columns
columns_to_drop = ['Total Cases/1 mil population', 'Death/1 mil population', 'Total Cases.1', 'Tests/1 mil population']
data_frame.drop(columns=columns_to_drop, inplace=True)

# Set index to State
data_frame = data_frame.set_index('State')

# Remove commas from numerical data
total_cases = data_frame['Total Cases'].str.replace(',', '')
total_deaths = data_frame['Total Deaths'].str.replace(',', '')
total_recovered = data_frame['Total Recovered'].str.replace(',', '')
active_cases = data_frame['Active Cases'].str.replace(',', '')
population = data_frame['Population'].str.replace(',', '')

# Set column types to numeric
data_frame['Total Cases'] = pd.to_numeric(total_cases)
data_frame['Total Deaths'] = pd.to_numeric(total_deaths)
data_frame['Total Recovered'] = pd.to_numeric(total_recovered)
data_frame['Active Cases'] = pd.to_numeric(active_cases)
data_frame['Population'] = pd.to_numeric(population)
