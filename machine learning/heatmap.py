import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

# Load the data
data = pd.read_csv("./dataset_pro.csv")

# Encoding categorical variables
label_encoder = preprocessing.LabelEncoder()

data['Sex']= label_encoder.fit_transform(data['Sex'])
data['Ethnicity']= label_encoder.fit_transform(data['Ethnicity'])
data['Jaundice']= label_encoder.fit_transform(data['Jaundice'])
data['Family_mem_with_ASD']= label_encoder.fit_transform(data['Family_mem_with_ASD'])
data['Who completed the test']= label_encoder.fit_transform(data['Who completed the test'])
data['Class/ASD Traits ']= label_encoder.fit_transform(data['Class/ASD Traits '])

# Check unique values after encoding
data['Sex'].unique()
data['Ethnicity'].unique()
data['Jaundice'].unique()
data['Family_mem_with_ASD'].unique()
data['Who completed the test'].unique()
data['Class/ASD Traits '].unique()

# Create heatmap to show correlation between variables
plt.figure(figsize=(15,15))
sns.heatmap(data.corr(), annot=True)
plt.show()