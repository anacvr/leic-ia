# IA 2023/2024

## Project 2: Prediction of Autism Spectrum Disorder in Toddlers

### Dependencies

To analyze the dataset and apply the Machine Learning models, we used the following Python libraries:

* **Pandas:** For data manipulation and analysis.
* **Matplotlib:** For creating plot visualizations.
* **Seaborn:** For statistical data visualization.
* **Scikit-learn:** For preprocessing data, implementing machine learning models and calculating evaluation metrics.

You can install these dependencies using pip:

```bash
pip install pandas matplotlib scikit-learn seaborn
```

### Usage

To compile and run the project, simply execute the [Project's Jupyter Notebook](Autism&#32;Dataset&#32;Notebook.ipynb). This notebook contains all the steps for the project, and the cells should be run in sequence due to dependencies between them.

**[Autism Dataset Notebook.ipynb](Autism&#32;Dataset&#32;Notebook.ipynb)**

The notebook includes all the necessary steps for the project, not just the application of the Machine Learning models. It is divided into sections for "Data Analysis", "Dataset Pre-processing", "Defining Training and Testing Sets", and "Machine Learning Models".

### ML Models Used

#### [Decision Tree](./Autism%20Dataset%20Notebook.ipynb#Decision-Tree)

The Decision Tree model was used due to its interpretability and ease of use. It performed well on the dataset, achieving an accuracy of 85%.


#### [Support Vector Machines (SVM)](./Autism%20Dataset%20Notebook.ipynb#SVM-(Support-Vector-Machines))

The SVM model was chosen for its ability to handle high-dimensional data and its effectiveness in classification tasks. It achieved an accuracy of 100% on the dataset. We acknowledge that this unusually high accuracy could suggest overfitting. Despite our efforts, we were unable to resolve this issue.


#### [K-Nearest Neighbors (KNN)](./Autism%20Dataset%20Notebook.ipynb#K-Nearest-Neighbors-(KNN))

The KNN model was used for its simplicity and effectiveness in handling multi-class problems. It achieved an accuracy of 92% on the dataset.


