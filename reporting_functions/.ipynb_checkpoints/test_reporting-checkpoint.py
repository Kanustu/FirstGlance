import pandas as pd
import numpy as np
import pytest
from report_functions import create_subplots, create_heatmap



def test_create_subplots_boxplot():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    })
    plot_type = 'boxplot'
    num_cols = 2
    
    # Execute the function
    create_subplots(data, plot_type, num_cols)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None

def test_create_subplots_histplot():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    })
    plot_type = 'histplot'
    num_cols = 2
    
    # Execute the function
    create_subplots(data, plot_type, num_cols)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None


@pytest.mark.xfail
def test_create_subplots_plottype_fail():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    })
    plot_type = 'scatterplot'
    num_cols = 3
    
    # Execute the function
    create_subplots(data, plot_type, num_cols)
    
    # Check if the subplots are created without any errors
    # We'll use plt.gcf() to get the current figure and plt.gca() to get the current axis
    # Then, we'll check if these are not None, indicating that the subplots were created
    assert plt.gcf() is not None
    assert plt.gca() is not None


def test_create_heatmap():
    # Create a DataFrame with some sample data
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    # Call the function
    create_heatmap(data)

    # At this point, the heatmap should be displayed, so we don't have a direct
    # return value to check. Instead, we can check if any errors occurred during
    # the execution of the function.
    # If no errors occurred, the test will pass.

@pytest.mark.xfail
def test_create_heatmap_fail():
    # Create a DataFrame with some sample data
    data = pd.DataFrame({
        'A': ['one', 'two', 'three'],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    # Call the function
    create_heatmap(data)













    
if __name__ == "__main__":
    pytest.main([__file__])