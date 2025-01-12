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
  
    #variable information 
    print(heart_disease.variables)

    
