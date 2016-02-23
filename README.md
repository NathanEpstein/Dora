# Dora
<img src="path/to/testing/badge">

Exploratory data analysis toolkit for Python.

## Contents
- [Summary](#summary)
- [Installation](#install)
- [Usage](#use)
  - [Configure](#config)
  - [Cleaning](#clean)
  - [Feature Selection & Extraction](#feature)
  - [Visualization](#visual)
  - [Model Validation](#model)
  - [Data Versioning](#version)
- [Testing](#test)
- [Contribute](#contribute)
- [License](#license)

<a name="summary" />
## Summary

Dora is a Python library designed to automate the painful parts of exploratory data analysis.

The library contains convenience functions for data cleaning, feature selection & extraction, visualization, partitioning data for model validation, and versioning transformations of data.

The library uses and is intended to be a helpful addition to common Python data analysis tools such as pandas, scikit-learn, and matplotlib.

<a name="install">
## Installation

...

<a name="use">
## Usage

<a name="config">
#### Configure

```python
# without initial config
>>> dora = Dora()
>>> dora.configure(output = 'A', data = 'path/to/data.csv')

# is the same as
>>> import pandas as pd
>>> dataframe = pd.read_csv('path/to/data.csv')
>>> dora = Dora(output = 'A', data = dataframe)

>>> dora.data

   A   B  C      D  useless_feature
0  1   2  0   left                1
1  4 NaN  1  right                1
2  7   8  2   left                1

```


