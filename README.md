# Loan Approval Prediction using a Multi-Layer Perceptron (MLP)

## 1. Project Overview

This project aims to build and evaluate a machine learning model to predict the approval or rejection of loan applications. The core of the project is the application of a Multi-Layer Perceptron (MLP), a type of neural network, for this binary classification task.

The project utilizes a synthetic dataset inspired by real-world credit risk scenarios. It simulates one of the most classic and high-impact challenges in the financial sector: credit risk assessment. The relevance of solving this problem efficiently and fairly is immense, both for financial institutions and for society.

## 2. The Business Challenge

The central challenge is to build a model that accurately balances two competing objectives:

1.  **Minimizing the Risk of Default (False Positives):** Approving a loan for someone who will not pay it back results in a direct financial loss.
2.  **Maximizing Business Opportunity (False Negatives):** Rejecting a loan for someone who would have paid it back correctly means lost revenue and the potential loss of a customer.

Furthermore, the model must be fair and interpretable, as institutions are often required to explain why a loan was denied. This project serves as a practical exercise in building effective and responsible AI systems.

## 3. The Dataset

The dataset represents a collection of 45,000 records of loan applicants.

### 3.1. Features

#### Numerical Features

- **Age:** The applicant's age.
- **Annual Income:** The applicant's annual income.
- **Employment Experience:** The applicant's work experience.
- **Loan Amount:** The amount of the loan requested.
- **Loan Interest Rate:** The interest rate of the loan.
- **Loan Amount as a percentage of annual income:** The loan amount as a percentage of the annual income.
- **Length of credit history:** The length of the applicant's credit history.
- **Credit score:** The applicant's credit score.
- **Previous loan defaults on file:** Records of previous loan defaults.

#### Categorical Features

- **Gender:** The applicant's gender.
- **Education:** The applicant's education level.
- **Home Ownership:** Whether the applicant owns a home.
- **Loan Intent:** The purpose of the loan.

### 3.2. Target Variable

The target variable is `loan_status`, which is a binary variable:
- **1:** Loan Approved
- **0:** Loan Rejected

## 4. Project Files and Structure

- **`data_exploration_preprocess.ipynb`**: This is the main Jupyter Notebook for the project. It contains the complete workflow, including:
    - Initial data loading and inspection.
    - **Exploratory Data Analysis (EDA):** Visualizing distributions (histograms, box plots) to understand the data's characteristics.
    - **Data Cleaning & Preprocessing:** Handling outliers, transforming skewed features (log transform), and preparing the data for modeling.
- **`data/`**: A directory containing the raw and processed datasets.
- **`README.md`**: This file, providing a detailed explanation of the project.

## 5. Methodology: Applying an MLP for Classification

The primary goal of this project is to apply a **Multi-Layer Perceptron (MLP)**, a type of feedforward artificial neural network, to this classification problem.

MLPs are particularly well-suited for this task for several reasons:
- **Learning Non-Linear Relationships:** Financial data is complex. The relationship between an applicant's features (like age, income, and credit score) and their creditworthiness is rarely linear. MLPs excel at learning these complex, non-linear patterns.
- **Automatic Feature Interaction:** Neural networks can automatically learn the intricate interactions between different input features without requiring manual feature engineering.
- **Scalability:** They can effectively handle a large number of features and data points, making them suitable for large-scale, real-world datasets.

The objective is to train the MLP on the preprocessed applicant data to learn the underlying patterns that distinguish between a "good" and a "bad" loan applicant, thereby accurately classifying new loan applications.

## 6. Requirements

To run the analysis and modeling code in `data_exploration_preprocess.ipynb`, you need to have Python installed along with the following libraries. You can install them using pip:

```bash
pip install -r requirements.txt
```
