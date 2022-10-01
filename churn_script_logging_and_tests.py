"""
A module to test the functions in churn_library
Author: Purusanth
Date: 30 July 2022
"""
import os
import logging
import pytest
import churn_library as cls


logging.basicConfig(
    filename='./logs/churn_library.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="module")
def pth():
    """
    A fixture to return the data path
    """
    return "./data/bank_data.csv"


@pytest.fixture(scope="module")
def import_data(pth):
    """
    A fixture to return the dataframe
    """
    return cls.import_data(pth)


@pytest.fixture(scope="module")
def perform_eda(import_data):
    """
    A fixture to perform the EDA
    """
    return cls.perform_eda(import_data)


@pytest.fixture(scope="module")
def category_lst():
    """
    A fixture to return a list of categorical columns
    """
    return [
        'Gender',
        'Education_Level',
        'Marital_Status',
        'Income_Category',
        'Card_Category']


@pytest.fixture(scope="module")
def response():
    """
    A fixture to return the rsponse columns
    """
    return "Churn"


@pytest.fixture(scope="module")
def keep_cols():
    """
    A fixture to return a list of wanted columns
    """
    return [
        'Customer_Age',
        'Dependent_count',
        'Months_on_book',
        'Total_Relationship_Count',
        'Months_Inactive_12_mon',
        'Contacts_Count_12_mon',
        'Credit_Limit',
        'Total_Revolving_Bal',
        'Avg_Open_To_Buy',
        'Total_Amt_Chng_Q4_Q1',
        'Total_Trans_Amt',
        'Total_Trans_Ct',
        'Total_Ct_Chng_Q4_Q1',
        'Avg_Utilization_Ratio',
        'Gender_Churn',
        'Education_Level_Churn',
        'Marital_Status_Churn',
        'Income_Category_Churn',
        'Card_Category_Churn']


@pytest.fixture(scope="module")
def encoder_helper(perform_eda, category_lst, response, keep_cols):
    """
    A fixture to perform caterorical encoding
    """
    return cls.encoder_helper(perform_eda, category_lst, response, keep_cols)


@pytest.fixture(scope="module")
def perform_feature_engineering(encoder_helper, response):
    """
    A fixture to perform feature engineering
    """
    return cls.perform_feature_engineering(encoder_helper, response)


@pytest.fixture(scope="module")
def train_models(perform_feature_engineering):
    """
    A fixture to do the model training
    """
    X_train, X_test, y_train, y_test = perform_feature_engineering
    return cls.train_models(X_train, X_test, y_train, y_test)


def test_import(import_data):
    '''
    test data import - this example is completed for you to assist with the other test functions
    '''
    try:
        df = import_data
        pytest.df = df
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err


def test_eda(perform_eda):
    '''
    test perform eda function
    '''
    try:
        df = perform_eda
        pytest.df = df
        logging.info("Testing perform_eda: SUCCESS")
    except BaseException:
        logging.error("Testing import_eda: EDA was failed")
    try:
        assert os.path.exists(
            "/home/workspace/images/eda/" +
            "churn_distribution.png")
        assert os.path.exists("/home/workspace/images/eda/" +
                              "customer_age_distribution.png")
        assert os.path.exists("/home/workspace/images/eda/" +
                              "marital_status_distribution.png")
        assert os.path.exists("/home/workspace/images/eda/" +
                              "total_transaction_distribution.png")
        assert os.path.exists(
            "/home/workspace/images/eda/" +
            "heatmap_distribution.png")
    except AssertionError as err:
        logging.error(
            "Testing perform_eda: Alteast one of the plot is missing")
        raise err


def test_encoder_helper(encoder_helper):
    '''
    test encoder helper
    '''
    try:
        df = encoder_helper
        pytest.df = df
        logging.info("Testing encoder_helper: SUCCESS")
    except KeyError as err:
        logging.error(
            "Testing import_eda: category column is not found in daframe")
        raise err

    try:
        assert 'Gender_Churn' in list(df.columns)
        assert 'Education_Level_Churn' in list(df.columns)
        assert 'Marital_Status_Churn' in list(df.columns)
        assert 'Income_Category_Churn' in list(df.columns)
        assert 'Card_Category_Churn' in list(df.columns)
    except AssertionError as err:
        logging.error(
            "Testing encoder_helper The dataset does not have one or more caterorical columns")
        raise err


def test_perform_feature_engineering(perform_feature_engineering):
    '''
    test perform_feature_engineering
    '''
    try:
        result = perform_feature_engineering
        logging.info("Testing perform_feature_engineering: SUCCESS")
    except ValueError as err:
        logging.error(
            "Testing test_perform_feature_engineering: \
            dataframe does not have enough data to split")
        raise err

    try:
        assert len(result) == 4
        assert result[0].shape[1] == result[1].shape[1]
    except AssertionError as err:
        logging.error(
            "Testing import_data: train and test dataset have different dimentions")
        raise err


def test_train_models(train_models):
    '''
    test train_models
    '''
    try:
        train_models
        logging.info("Testing train_models: SUCCESS")
    except ValueError as err:
        logging.error("Testing train_models:do not able to fit the models")
        raise err

    try:
        assert os.path.exists('./models/rfc_model.pkl')
        assert os.path.exists('./models/logistic_model.pkl')
    except AssertionError as err:
        logging.error(
            "Testing train_models: forlders does not have the trained models")
        raise err


# if __name__ == "__main__":
#     category_lst = [
#         'Gender',
#         'Education_Level',
#         'Marital_Status',
#         'Income_Category',
#         'Card_Category']
#     response = 'Churn'
#     keep_cols = [
#         'Customer_Age',
#         'Dependent_count',
#         'Months_on_book',
#         'Total_Relationship_Count',
#         'Months_Inactive_12_mon',
#         'Contacts_Count_12_mon',
#         'Credit_Limit',
#         'Total_Revolving_Bal',
#         'Avg_Open_To_Buy',
#         'Total_Amt_Chng_Q4_Q1',
#         'Total_Trans_Amt',
#         'Total_Trans_Ct',
#         'Total_Ct_Chng_Q4_Q1',
#         'Avg_Utilization_Ratio',
#         'Gender_Churn',
#         'Education_Level_Churn',
#         'Marital_Status_Churn',
#         'Income_Category_Churn',
#         'Card_Category_Churn']
