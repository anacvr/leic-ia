import pandas as pd

# Load the data
data = pd.read_csv("../dataset.csv")

# Transform data to lower case
data = data.apply(lambda x: x.astype(str).str.lower())

# Delte column with case number
del data['Case_No']

# Save the data to new csv file
data.to_csv("../dataset_pro.csv", index=False)

