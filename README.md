# FirstGlance

FirstGlance is a Python library created with the intention of being used for preliminary data analysis primarily within a notebook environment.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FirstGlance.

```bash
pip install FirstGlance
```

## Usage

```python
import FirstGlance as fg

# Returns seaborn boxplots, histograms, and heatmap using the numeric columns
fg.plot_analysis('example.csv')

- add screenshot

# Returns pandas dataframe with entry count, null count, datatype and descriptive statistics for each column
fg.stats_report('example.csv')

- add screenshot

```

## Dependencies

- [pandas](https://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)

Before using this package, make sure you have installed the above dependencies. You can install them using pip:

```bash
pip install pandas seaborn
```

## License

- choose a license--needs to be done