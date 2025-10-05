import pandas as pd
import numpy as np

# Cleans and transforms the raw loan approval data. All decisions
# for filtering and transformation are based on the exploratory analysis
# from the 'data_exploration.ipynb' notebook.

df = pd.read_csv('data/loan_approval/loan_data.csv')

# Log-transform skewed numerical features
df['person_income'] = np.log(df['person_income'])
df['loan_amnt'] = np.log(df['loan_amnt'])

# Map the sparse 'OTHER' category to null
df['person_home_ownership'] = df['person_home_ownership'].replace('OTHER', np.nan)

# Filter out extreme outliers based on EDA findings
df = df[df['person_age'] <= 70]
df = df[df['person_emp_exp'] <= 40]
df = df[df['person_income'] < 14]

# Save the processed data to a new file
df.to_csv('data/loan_approval/loan_data_refined.csv', index=False)