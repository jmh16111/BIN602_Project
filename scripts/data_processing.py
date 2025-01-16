'''
File: data_processing.ipynb
Author: Jourdan Hourican
Date: 2024-01-15
Purpose: Import, clean, and process data for analysis.
'''

#install ucimlrepo package
#pip install ucimlrepo
import pandas as pd
from ucimlrepo import fetch_ucirepo


# Import dataset
heart_disease = fetch_ucirepo(id=45)
# alternatively: fetch_ucirepo(name='Heart Disease')

# data (as pandas dataframes) 
features = heart_disease.data.features 
targets = heart_disease.data.targets 

# Handle missing values by filling with ???
features = features.fillna(features.mean())

# View the data
print(features)

