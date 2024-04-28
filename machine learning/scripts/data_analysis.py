import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("../dataset_pro.csv")

# Details about the data
print("\nDimensions of the dataset:", df.shape)
print("\nNumber of missing values in each column:\n", df.isnull().sum())

# Histograms for Age and Qchat-10-Score
df[['Age_Mons', 'Qchat-10-Score']].hist(figsize=(10, 8))
plt.suptitle('Histograms for Age and Qchat-10-Score', x=0.5, y=0.95, weight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig("../images/histograms.svg")
plt.savefig("../images/histograms.png")

# Statistical Summary for Age and Qchat-10-Score
print("\nStatistical Summary: \n")
summary = df[['Age_Mons', 'Qchat-10-Score']].describe()
print(summary)
print("\n\n")

# Show the Statistical Summary on a table
fig, ax = plt.subplots(1, 1)
ax.axis('off')
table = plt.table(cellText=summary.values, colLabels=summary.columns, rowLabels=summary.index, cellLoc = 'center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 1.5)
plt.title('Statistical Summary', y=0.8, weight='bold')

#plt.show()
plt.savefig("../images/statistical_summary.svg")
plt.savefig("../images/statistical_summary.png")


# Class Distribution
class_distribution = df['Class/ASD Traits'].value_counts()
print("Class Distribution: \n", class_distribution)
print("\n\n")

# Plotting the class distribution
plt.figure(figsize=(6,5))
class_plot = sns.barplot(x=class_distribution.index, y=class_distribution.values, alpha=0.8, palette="colorblind", width=0.4)

for i, value in enumerate(class_distribution.values):
    class_plot.text(i, value, value, ha='center', va='bottom')

plt.title('Class Distribution')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Class/ASD Traits', fontsize=12)

#plt.show()
class_plot.figure.savefig("./../images/class_distribution.svg")
class_plot.figure.savefig("./../images/class_distribution.png")
