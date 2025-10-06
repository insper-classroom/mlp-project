Dataset Explanation
This dataset is a synthetic version inspired by the original Credit Risk dataset, enriched with additional variables based on Financial Risk data for Loan Approval. It contains 45,000 records and is designed for classification tasks, specifically to predict the approval or rejection of a loan.

Detailed Dataset Description
What does it represent?
The dataset represents a collection of information about loan applicants, which can be used to train a machine learning model to predict whether a loan should be approved or not.

What are the features (inputs) and their types?
The features of the dataset are:

Numerical:

Age: The applicant's age.

Annual Income: The applicant's annual income.

Employment Experience: The applicant's work experience.

Loan Amount: The amount of the loan requested.

Loan Interest Rate: The interest rate of the loan.

Loan Amount as a percentage of annual income: The loan amount as a percentage of the annual income.

Length of credit history: The length of the applicant's credit history.

Credit score: The applicant's credit score.

Previous loan defaults on file: Records of previous loan defaults.

Categorical:

Gender: The applicant's gender.

Education: The applicant's education level.

Home Ownership: Whether the applicant owns a home.

Loan Intent: The purpose of the loan.

What is the target variable (classes/labels)?
The target variable is loan_status, which is a binary variable:

1: Loan approved

0: Loan rejected

Domain Knowledge
In this context of loan approval, some financial terms are important:

Credit Score: A numerical score that represents an individual's creditworthiness. A higher score generally indicates a lower risk of default.

Loan Intent: The reason why the loan is being requested (e.g., for education, medical expenses, home improvements). The purpose can influence the risk assessment.

Default: The failure to meet the obligation to repay a loan. Having a history of defaults significantly increases the risk for the lender.
