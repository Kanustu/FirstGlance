# InitialAnalysis

InitialAnalysis is a Python library created with the intention of being used for very preliminary.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install InitialAnalysis.

```bash
pip install InitialAnalysis
```

## Usage

```python
import InitialAnalysis

# Returns seaborn boxplots, histograms, and heatmap using the numeric columns
InitialAnalysis.plot_analysis('example.csv')

# Returns pandas dataframe with entry count, null count, datatype and descriptive statistics for each column
InitialAnalysis.stats_report('example.csv')

```

## License

- choose a license--needs to be done