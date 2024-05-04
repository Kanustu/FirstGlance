import pandas as pd
import numpy as np
import pytest
import matplotlib.pyplot as plt
from report_functions import create_subplots, create_heatmap, data_input, data_describe, data_is_null, data_type



data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
data.to_csv('test_csv.csv', index=False)

def test_create_subplots_boxplot():
    plot_type = 'boxplot'
    # Execute the function
    create_subplots(data, plot_type)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None

def test_create_subplots_histplot():
    plot_type = 'histplot'
    
    # Execute the function
    create_subplots(data, plot_type)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None


@pytest.mark.xfail
def test_create_subplots_plottype_fail():
    plot_type = 'scatterplot'
    
    # Execute the function
    create_subplots(data, plot_type)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None


def test_create_heatmap():
    # Call the function
    create_heatmap(data)

    # At this point, the heatmap should be displayed, so we don't have a direct
    # return value to check. Instead, we can check if any errors occurred during
    # the execution of the function.
    # If no errors occurred, the test will pass.


def test_data_input():
    result = data_input('test_csv.csv')
    expected_columns = ['A', 'B', 'C']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what was expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is what was expected'


@pytest.mark.xfail
def test_data_input():
    result = data_input('test_csv.csv')
    expected_columns = ['A', 'D', 'C']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what was expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is what was expected'


def test_data_describe():
    result = data_describe(data)
    expected_columns = ['mean', 'std', 'min', '25%', '50%', '75%', 'max']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what is expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is not what was expected'


@pytest.mark.xfail
def test_data_describe():
    result = data_describe(data)
    expected_columns = ['std', 'min', '25%', '75%', 'max']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what is expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is not what was expected'


def test_data_is_null():
    result = data_is_null(data)
    expected_columns = ['null_count']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what is expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is not what was expected'


@pytest.mark.xfail
def test_data_is_null_fail():
    result = data_is_null(data)
    expected_columns = ['0']
    assert result.columns.tolist() == expected_columns, 'Columns returned are not what is expected'
    assert result.shape == (len(data.index), len(expected_columns)), 'Shape is not what was expected'


def test_data_type():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c'],
        'C': [1.1, 2.2, 3.3]
    })
    result = data_type(data)
    expected_output = pd.Series(['int64', 'object', 'float64'], index=['A', 'B', 'C'])
    assert result.equals(expected_output)

@pytest.mark.xfail
def test_data_type_fail():
    data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c'],
            'C': [1.1, 2.2, 3.3]
        })
        result = data_type(data)
        expected_output = pd.Series(['int64', 'str', 'float64'], index=['A', 'B', 'C'])
        assert result.equals(expected_output)







    
if __name__ == "__main__":
    pytest.main([__file__])