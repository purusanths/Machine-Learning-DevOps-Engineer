# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
This project is an implementation of churn prediction that follow coding and engineerng best practices for implementing software.
* Objective: Implement coding best practices
* Learning outcome: you will be confident in testing, logging, coding best practices
What to do?
* churn_notebook.ipynb contain solutions to indetify the customers who are likely to churn but without following coding best practices. your task is to refactor to follow the coding best practices to develop the following files
    * churn_library.py: A library of functions to find customers who are likely to churn
    * churn_script_logging_and_tests.py : Contain unit tests for the churn_library.py functions
    * README.md: This file will provide an overview of the project, the instructions to use the code
## Files and data description
The dataset contain 20 feature and Attrition_Flag as target. There are numerical and categorical field are present in the data frame.
Categorical field
* Gender
* Education_Level
* Marital_Status
* Income_Category
* Card_Category

Numerical field
*   Customer_Age
*   Dependent_count
*   Months_on_book
*   Total_Relationship_Count
*   Months_Inactive_12_mon
*   Contacts_Count_12_mon
*   Credit_Limit
*   Total_Revolving_Bal
*   Avg_Open_To_Buy
*   Total_Amt_Chng_Q4_Q1
*   Total_Trans_Amt
*   Total_Trans_Ct
*   Total_Ct_Chng_Q4_Q1
*   Avg_Utilization_Ratio

Target
* Attrition_Flag



# Files
 * [data](./data)
    * [bank_data.csv](./data/bank_data.csv)
 * [images](./images)
    * [eda](./eda)
         * [churn_distribution.png](./images/eda/churn_distribution.png)
        * [customer_age_distribution.png](./images/eda/customer_age_distribution.png/)
        * [heatmap.png](./images/eda/heatmap.png)
        * [marital_status_distribution.png](./images/eda/marital_status_distribution.png)
    * [results](./results)
        * [feature_importance.png](./images/results/feature_importance.png)
        * [logistics_results.png](./images/results/logistics_results.png)
        * [rf_results.png](./images/results/rf_results.png)
        * [roc_curve_result.png](./images/results/roc_curve_result.png)
 * [logs](./logs)
    * [churn_library.log](./logs/churn_library.log)
 * [models](./models)
    * [logistic_model.pkl](./models/logistic_model.pkl)
    * [rfc_model.pkl](./models/rfc_model.pkl)
* [churn_library.py](./churn_library.py)
* [churn_notebook.ipynb](./churn_notebook.ipynb)
* [churn_script_logging_and_tests.py](./churn_script_logging_and_tests.py)
* [requirements.txt](./requirements.txt)
 * [README.md](./README.md)
## Running Files
##### install the required libraries

```sh
pip3 install -r requirements.txt
```
##### churn_library.py : 
When we are running this file it will perform the standard process in the data science pipline and save the result/artifacts, model to the relavant folders. The code snipt below shows how to run this file
```sh
python churn_library.py
```
#####  churn_script_logging_and_tests.py  
when we run this file it will perform unitest for the functions defined in churn_library.py and log the error and info message to a file. So  we can review it later to idendifty what happened whnen the programm was running
```sh
python churn_script_logging_and_tests.py 
```
#####  Code to test the PEP8 style guide
The code blow give a score. This score indicate how much you follow the PEP8 coding style

```sh
pylint churn_library.py
pylint churn_script_logging_and_tests.py
```
#####  PEP8 style guide
The code below automatically modify the code to follow the PEP8 style guide.
```sh
autopep8 --in-place --aggressive --aggressive churn_script_logging_and_tests.py
autopep8 --in-place --aggressive --aggressive churn_library.py
```