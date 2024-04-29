# Import libraries
import pandas as pd
from pandas import DataFrame
from typing import List, Union, Dict
from pydantic import BaseModel
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


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
    
def create_boxplots_by_column(data, num_cols):
    numeric_columns = [column for column in data.columns 
                       if data[column].dtypes == 'int64' or data[column].dtypes == 'float64']
    
    num_plots = len(numeric_columns)
    #num_cols = 1  # Number of columns in the grid
    num_rows = (num_plots + num_cols - 1) // num_cols  # Number of rows in the grid
    
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))  # Create subplots
    
    for i, column in enumerate(numeric_columns):
        row = i // num_cols  # Row index
        col = i % num_cols   # Column index
        sns.boxplot(x=data[column], ax=axes[row, col])  # Plot on specific axes
        axes[row, col].set_title(f'{column}'.capitalize())

    plt.suptitle("Boxplot Analysis", fontsize=16, y=1.02)
        
    # Hide any unused axes
    for i in range(num_plots, num_rows * num_cols):
        row = i // num_cols
        col = i % num_cols
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()
    

def create_histplots_by_column(data, num_cols):
    numeric_columns = [column for column in data.columns 
                       if data[column].dtypes == 'int64' or data[column].dtypes == 'float64']
    
    num_plots = len(numeric_columns)
    #num_cols = 2  # Number of columns in the grid
    num_rows = (num_plots + num_cols - 1) // num_cols  # Number of rows in the grid
    
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))  # Create subplots
    
    for i, column in enumerate(numeric_columns):
        row = i // num_cols  # Row index
        col = i % num_cols   # Column index
        sns.histplot(x=data[column], ax=axes[row, col])  # Plot on specific axes
        axes[row, col].set_title(f'{column}'.capitalize())
        
    plt.suptitle("Histogram Analysis", fontsize=16, y=1.02)
    
    # Hide any unused axes
    for i in range(num_plots, num_rows * num_cols):
        row = i // num_cols
        col = i % num_cols
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()

            
def create_heatmap(data):
    data = numeric_data(data)
    corr_matrix = data.corr()
    
    # Set up the heatmap figure
    plt.figure(figsize=(8, 6))
    
    # Customize the appearance of the heatmap
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", linewidths=.5)
    
    # Add title to the heatmap
    plt.title('Correlation Heatmap')
    
    # Adjust layout
    plt.tight_layout()
    
    # Show the heatmap
    plt.show()


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
    data_read = data_input(data)
    df1 = pd.DataFrame(data_count(data_read)).T.rename(columns={0: 'entry_count'})
    df1['data_type'] = data_type(data_read)
    df1['null_count'] = data_isnull(data_read)
    df2 = data_describe(data_read)
    report = pd.merge(df1, df2, left_index=True, right_index=True, how='left')
    return report


def initial_analysis(csv: str, num_cols):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        pd.set_option('mode.use_inf_as_na', True)
        data = data_input(csv)
        print('\n\n')
        create_boxplots_by_column(data, num_cols)
        print('\n\n')
        create_histplots_by_column(data, num_cols)
        print('\n\n')
        create_heatmap(data)

    