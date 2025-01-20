'''
File: data_processing.ipynb
Author: Jourdan Hourican, Lenna Wolffe, Madison Tarasuik, John Beliveau
Date: 2024-01-15
Purpose: Utilizing the UC Irvine database on heart disease, this script will import data, clean data by replacing any missing values with the mean value,
 extract features and target data, and perform a cluster analysis to answer/analyze two questions: 
 1. Are there specific combinations of risk factors that form clusters in this dataset?
 2. Can we identify clusters based on clinical measurements (ex. cholesterol levels, 
 resting blood pressure, maximum heart rate) and their association with heart disease?
'''

#install ucimlrepo package
#pip install ucimlrepo
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



"""
In this paper they used these 14 attributes:
https://archive.ics.uci.edu/dataset/45/heart+disease
https://www.semanticscholar.org/paper/International-application-of-a-new-probability-for-Detrano-J%C3%A1nosi/a7d714f8f87bfc41351eb5ae1e5472f0ebbe0574
      1. #3  (age)       In year
      2. #4  (sex)       (1 = male; 0 = female)
      3. #9  (cp)        
      4. #10 (trestbps)  resting blood pressure (on admission to the hospital) mm Hg
      6. #16 (fbs)       fasting blood sugar > 120 mg/dl
      7. #19 (restecg)   
      8. #32 (thalach)   maximum heart rate achieved
      9. #38 (exang)     exercise induced angina
      10. #40 (oldpeak)  ST depression induced by exercise relative to rest
      11. #41 (slope)     
      12. #44 (ca)       number of major vessels (0-3) colored by flourosopy
      13. #51 (thal)      
      14. #58 (num)      diagnosis of heart disease	(the predicted attribute)
            
            58 num: diagnosis of heart disease (angiographic disease status)
        -- Value 0: < 50% diameter narrowing
        -- Value 1: > 50% diameter narrowing
        (in any major vessel: attributes 59 through 68 are vessels)
 """


def Import_UCI_Heart_Disease_Data(): # Import dataset
    heart_disease = fetch_ucirepo(name='Heart Disease')
    # Alternatively; heart_disease = fetch_ucirepo(id=45) 
    return heart_disease

def Dataframe_features(heart_disease):# data (as pandas dataframes)
    features = heart_disease.data.features 
    return features

def Dataframe_targets(heart_disease): #identify target (number of diagnoses of major vessel diameter narrowing (50%))
    diagnosis = heart_disease.data.targets
    return diagnosis

def Replace_Empty_Values(data): #Handle missing values by filling with mean of the data
    return data.fillna(data.mean())

def Perform_KMeans_Clustering(features, n_clusters=3): # functiong for K-means clustering analysis
    # performs K-means clustering on feature data. Scales the data for consistent clustering and uses K-means to group data into clusters
    # features : pandas dataframe containing feature data
    # n_clusters : number of clusters to form ( 3 is the default)
    # returns cluster_labels: array of cluster labels for data points

    # scale data to standardize feature values
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    # initializing K-means algorithm
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_features)
    return cluster_labels

# creating function to interpret/analyze clustering 
def Analyze_Clusters(features, cluster_labels):
    # adds cluster labels to feature data fram and prints statistics for each cluster
    features['Cluster'] = cluster_labels # adding cluster labels as a column to features dataframe 
    cluster_summary = features.groupby('Cluster').mean() # grouping by clusters and calculating statistics 
    print("/nCluster Summary Statistics:")
    print(cluster_summary)

def unit_test():
    #Calling functions to test import, extraction, and clean up of UCI Heart Disease Data
    heart_disease = Import_UCI_Heart_Disease_Data() 
    features = Dataframe_features(heart_disease)
    diagnosis = Dataframe_targets(heart_disease)
    features = Replace_Empty_Values(features)
    diagnosis = Replace_Empty_Values(diagnosis)
    #print(heart_disease)
    #print(features)
    #print(diagnosis)
    print("test completed") #no large errors found if you see this message after running test
    print("/nPerfomring K-means Clustering")
    cluster_labels = Perform_KMeans_Clustering(features, n_clusters=3)
    print("/nAnalyzing Clustering Results")
    Analyze_Clusters(features, cluster_labels)
    print("/nUnit test completed.")


if __name__ == '__main__':
    unit_test()

