# Dora
<img src="path/to/testing/badge">

Exploratory data analysis toolkit for Python.

## Contents
- [Summary](#summary)
- [Installation](#install)
- [Usage](#use)
  - [Reading Data & Configuration](#config)
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
#### Reading Data & Configuration

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

<a name="clean">
#### Cleaning

```python
# read data with missing and poorly scaled values
>>> import pandas as pd
>>> df = pd.DataFrame([
...   [1, 2, 100],
...   [2, None, 200],
...   [1, 6, None]
... ])
>>> dora = Dora(output = 0, data = df)
>>> dora.data
   0   1    2
0  1   2  100
1  2 NaN  200
2  1   6  NaN

# impute the missing values (using the average of each column)
>>> dora.impute_missing_values()
>>> dora.data
   0  1    2
0  1  2  100
1  2  4  200
2  1  6  150

# scale the values of the input variables (center to mean and scale to unit variance)
>>> dora.scale_input_values()
>>> dora.data
   0         1         2
0  1 -1.224745 -1.224745
1  2  0.000000  1.224745
2  1  1.224745  0.000000

```

<a name="feature">
#### Feature Selection & Extraction
```python
# feature selection / removing a feature
>>> dora.data
   A   B  C      D  useless_feature
0  1   2  0   left                1
1  4 NaN  1  right                1
2  7   8  2   left                1

>>> dora.remove_feature('useless_feature')
>>> dora.data
   A   B  C      D
0  1   2  0   left
1  4 NaN  1  right
2  7   8  2   left

# extract an ordinal feature through one-hot encoding
>>> dora.extract_ordinal_feature('D')
>>> dora.data
   A   B  C  D=left  D=right
0  1   2  0       1        0
1  4 NaN  1       0        1
2  7   8  2       1        0

```