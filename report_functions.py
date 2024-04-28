# Import libraries
import pandas as pd
from pandas import DataFrame
from typing import List, Union, Dict
from pydantic import BaseModel
import seaborn as sns
import matplotlib.pyplot as plt

def numeric_data(data):
    numeric_columns = []
    for column in data.columns:
        if data[column].dtypes == 'int64' or data[column].dtypes == 'float64':
            numeric_columns.append(column)
    df = pd.DataFrame(data, columns=numeric_columns)
    return df

def non_numeric_data(data):
    non_numeric_columns = []
    for column in data.columns:
        if data[column].dtypes != 'int64' and data[column].dtypes != 'float64':
            non_numeric_columns.append(column)
    df = pd.DataFrame(data, columns=non_numeric_columns)
    return df
    
def create_boxplots_by_column(data):
    # Iterate over each column in the DataFrame
    for column in data.columns:
        # Create a boxplot for the current column
        if data[column].dtypes == 'int64' or data[column].dtypes == 'float64':
            sns.boxplot(x=data[column])
            plt.title(f'Boxplot for {column}')
            plt.show()

def create_histplots_by_column(data):
    pd.option_context('mode.use_inf_as_na', True)
    for column in data.columns:
        if data[column].dtypes == 'int64' or data[column].dtypes == 'float64':
            sns.histplot(x=data[column])
            plt.title(f'Histogram for {column}')
            plt.show()
            
def create_heatmap(data):
    data = numeric_data(data)
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix)

def data_input(csv: str) -> pd.DataFrame:
    """
    Read a CSV file and return its contents as a DataFrame.

    Parameters:
        csv (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(csv)
    
    
def data_describe(data: DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics of the DataFrame columns.

    Parameters:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: Descriptive statistics for the DataFrame columns.
    """
    return data.describe().T.drop(columns='count')
    
    
def data_isnull(data: DataFrame) -> pd.DataFrame:
    """
    Count the number of missing values in each column of the DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the count of missing values for each column.
    """
    return data.isnull().sum().to_frame().rename(columns={0: 'null_count'})
    

def data_type(data: DataFrame) -> pd.Series:
    """
    Get the data types of each column in the DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.Series: A Series containing the data types of each column.
    """
    return data.dtypes
    
    
def data_count(data: DataFrame) -> dict:
    """
    Count the number of entries in each column of the DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        dict: A dictionary containing the count of entries for each column.
    """
    count_dict = {}
    for column in data.columns:
        count_dict[column] = [data.shape[0]]
    return count_dict
    
    
def eda_report(data: DataFrame) -> pd.DataFrame:
    """
    Generate an Exploratory Data Analysis (EDA) report for the DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: An EDA report containing descriptive statistics, data types, null counts, and entry counts for each           column.
    """
    df1 = pd.DataFrame(data_count(data)).T.rename(columns={0: 'entry_count'})
    df1['data_type'] = data_type(data)
    df1['null_count'] = data_isnull(data)
    df2 = data_describe(data)
    report = pd.merge(df1, df2, left_index=True, right_index=True, how='left')
    return report

def initial_analysis(csv: str):
    data = data_input(csv)
    print(eda_report(data))
    print(create_boxplots_by_column(data))
    print(create_histplots_by_column(data))
    print(create_heatmap(data))
    