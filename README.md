 # Week 1

Executed these steps in 1st week of internship:

- **Step 1:** Import Required Libraries  
- **Step 2:** Load Dataset  
- **Step 3:** Data Preprocessing


# Week 2

Specifically, I performed the following steps:

- **Dropped the 'Unnamed: 7' column**  
  This column was identified as having no data.

- **Inspected the DataFrame**  
  We checked the column names, data types, and non-null counts using `df.info()` and summary statistics using `df.describe()`.

- **Checked for Null Values**  
  We confirmed there were no null values remaining after dropping the 'Unnamed: 7' column.

- **Visualized Target Variable Distribution**  
  Created a histogram to understand the distribution of the *'Supply Chain Emission Factors with Margins'*.

- **Examined and Encoded Categorical Features**  
  Mapped unique values in `'Substance'`, `'Unit'`, and `'Source'` to numerical representations.

- **Dropped Irrelevant Columns**  
  Removed the `'Name'`, `'Code'`, and `'Year'` columns as they were not needed for modeling.

- **Defined Features and Target**  
  Split the data into features (`X`) and target variable (`y`) for machine learning.

- **Performed Univariate and Multivariate Analysis**  
  Created count plots for categorical variables and a correlation heatmap for numerical variables.

- **Identified Top Emitting Industries**  
  Grouped and visualized data to find the top 10 industries with the highest average supply chain emission factors.

These steps were crucial for **cleaning and preparing the dataset** before building a machine learning model.


# Week 3

Executed the following key steps in Week 3:

- **Normalize Features**  
  Scaled the feature data (`X`) using `StandardScaler` to ensure all features contribute equally during model training.

- **Train-Test Split**  
  Divided the scaled features and target variable (`y`) into training and testing sets for model evaluation.

- **Model Selection**  
  Initialized the **Random Forest Regressor** for initial training and evaluation.

- **Step 4: Model Training**  
  Trained the Random Forest model using the training data to learn patterns and relationships in the dataset.

- **Step 5: Prediction and Evaluation**  
  Made predictions on the test set and evaluated model performance using **RMSE** and **R²** metrics.  
  Also trained and evaluated a **Linear Regression** model for performance comparison.

- **Step 6: Hyperparameter Tuning**  
  Used **GridSearchCV** to tune the Random Forest model and find the best-performing set of parameters.

- **Best Model Evaluation**  
  Evaluated the tuned Random Forest model and compared its performance against the baseline models.

- **Step 7: Model Comparison and Final Selection**  
  Compared performance of all trained models and selected **Linear Regression** as the best performer based on accuracy and simplicity.

- **Model Saving**  
  Created a `models` directory and saved the best model as `LR_model.pkl` and the `StandardScaler` as `scaler.pkl`.

- **Streamlit App Development**  
  Installed Streamlit and created the `app.py` and `utils` directory. Built a user-friendly web app to perform predictions.  
  Used **pyngrok** to generate a public URL for easy external access.

# Final Project Overview
🌍 Greenhouse Gas Emissions Prediction – AICTE Internship Final Project
This project focuses on predicting greenhouse gas (GHG) emissions using advanced machine learning techniques as part of the AICTE Virtual Internship program. The goal is to analyze global emission trends and build predictive models that support environmental sustainability and informed decision-making.

🔍 Key Features:
📊 Data Analysis: In-depth EDA on global GHG emissions datasets.

🤖 Machine Learning Models: Implemented and evaluated models like Linear Regression, Random Forest, and XGBoost.

📈 Prediction Capability: Accurately forecasts future GHG emission levels based on historical data.

📎 Clean and Well-Commented Code: Developed in Python using Jupyter Notebook (Google Colab compatible).

📂 Organized Structure: Contains datasets, notebooks, result visualizations, and reports.

🧠 Tools & Libraries Used:
Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn



