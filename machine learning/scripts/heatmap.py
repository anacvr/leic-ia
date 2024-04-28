import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

# Load the data
df = pd.read_csv("../dataset_pro.csv")

# Encoding categorical variables
label_encoder = preprocessing.LabelEncoder()

df['Sex']= label_encoder.fit_transform(df['Sex'])
df['Ethnicity']= label_encoder.fit_transform(df['Ethnicity'])
df['Jaundice']= label_encoder.fit_transform(df['Jaundice'])
df['Family_mem_with_ASD']= label_encoder.fit_transform(df['Family_mem_with_ASD'])
df['Who completed the test']= label_encoder.fit_transform(df['Who completed the test'])
df['Class/ASD Traits']= label_encoder.fit_transform(df['Class/ASD Traits'])

# Check unique values after encoding
df['Sex'].unique()
df['Ethnicity'].unique()
df['Jaundice'].unique()
df['Family_mem_with_ASD'].unique()
df['Who completed the test'].unique()
df['Class/ASD Traits'].unique()

# Create heatmap to show correlation between variables
plt.figure(figsize=(14,14))
sns.heatmap(df.corr(), annot=True)
plt.tight_layout()

# Save the heatmap
plt.savefig("../images/heatmap.png")
plt.savefig("../images/heatmap.svg")

plt.show()