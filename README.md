# BIN602_Project

# Authors: John Beliveau, Jourdan Hourican, Madison Tarasuik, Lenna Wolffe

# Project Description: 
    This project aims to download, process, explore and analyze a heart disease bioinformatics data set to answer key research questions (listed below) using clustering techniques. The goal is to indentify patterns within the dataset that provide meaningful insights into heart disease. 

# Key reasearch questions:
    1. Are there specific combinations of risk factors that form clusters in this dataset?
    
    2. Can we identify clusters based on clinical measurements (ex. cholesterol levels, resting blood pressure, maximum heart rate) and their association with heart disease?

# Dataset:
    Information regarding dataset: https://archive.ics.uci.edu/dataset/45/heart+disease

# Importing dataset:
    #install ucimlrepo package
    pip install ucimlrepo
    
    from ucimlrepo import fetch_ucirepo 
  
    #fetch dataset 
    heart_disease = fetch_ucirepo(id=45) 
  
    #data (as pandas dataframes) 
    X = heart_disease.data.features 
    y = heart_disease.data.targets 
  
    #metadata 
    print(heart_disease.metadata) 

# Preprocessing data:
    Use python script "data_processing.py" in order to import data, clean data by replacing any missing values with the mean value, extract features and target data, and perform a cluster analysis.

# Analysis:
    Use notebook "data_analysis.ipynb" to import the cleaned dataset and run the clustering analysis in order to answer key research questions.


# Project Insights:
    By running the clustering scipt we can identify clusters based on clinical measurements, and doing so seems to provide further insight into the heart disease association. For example, Cluster 0 seems to have more severe cardiovascular symptoms and risk factors, while Cluster 1 has better cardiovascular fitness and lower risk factors.

    
