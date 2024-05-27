import pandas as pd

"""
After analysing the dataset, we concluded that we needed to remove a few columns to have a better data to train and test our dataset.

* The column ***"Who completed the test"*** was removed because we considered this factor to have no relevance on the current analysis.
* The column ***"Qchat-10-Score"*** was removed because it is a score that is calculated by adding the answers from the column Q1 to Q10.

We downloaded the dataset from its [website](https://www.kaggle.com/datasets/vaishnavisirigiri/autism-dataset-for-toddlers) in a CSV format and imported it to a pandas dataframe.

We did a small pre-processing for better consistency on the data analysis, such as removing possible duplicates and transforming all text to lowercase to have a homogeneous dataset.
"""

# Load the data
data = pd.read_csv("../dataset.csv")

# Transform data to lower case
data = data.apply(lambda x: x.astype(str).str.lower())

# Drop duplicates
# This needs to be done before deleting the column with the case number
data = data.drop_duplicates()

# Delete column with case number
del data['Case_No']

# Delete column with Qchat-10-Score
del data['Qchat-10-Score']

# Delete column with who completed the test
del data['Who completed the test']

# Delete rows with missing values
data = data.dropna()


# Save the data to new csv file
data.to_csv("../dataset_pro.csv", index=False)

