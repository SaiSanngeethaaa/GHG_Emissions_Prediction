# Week1
Executed these steps in 1st week of internship 
Step 1: Import Required Libraries 
Step 2: Load Dataset 
Step 3: Data Preprocessing

# Week2
Specifically, we performed the following steps:
Step 1: **Dropped the 'Unnamed: 7' column:** This column was identified as having no data.
Step 2: **Inspected the DataFrame:** We checked the column names, data types, and non-null counts using df.info() and summary statistics using df.describe().
Step 3: **Checked for Null Values:** We confirmed there were no null values remaining after dropping the 'Unnamed: 7' column.
Step 4: **Visualized Target Variable Distribution:** We created a histogram to understand the distribution of the 'Supply Chain Emission Factors with Margins'.
Step 5: **Examined and Encoded Categorical Features:** We looked at the unique values in 'Substance', 'Unit', and 'Source' and then mapped these categorical values to numerical representations.
Step 6: **Dropped Irrelevant Columns:** We removed the 'Name', 'Code', and 'Year' columns as they were not needed for the planned modeling.
Step 7: **Defined Features and Target:** We separated the data into features (X) and the target variable (y) for machine learning.
Step 8: **Performed Univariate and Multivariate Analysis:** We created count plots for the categorical variables and a correlation heatmap for the numerical variables to understand relationships within the data.
Step 9: **Identified Top Emitting Industries:** We grouped the data to find and visualize the top 10 industries with the highest average supply chain emission factors.
These steps were crucial for cleaning and preparing the data before building a machine learning model.
