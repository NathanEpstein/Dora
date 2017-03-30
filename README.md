# Dora
Exploratory data analysis toolkit for Python.

## Contents
- [Summary](#summary)
- [Setup](#setup)
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

<a name="summary"></a>
## Summary

Dora is a Python library designed to automate the painful parts of exploratory data analysis.

The library contains convenience functions for data cleaning, feature selection & extraction, visualization, partitioning data for model validation, and versioning transformations of data.

The library uses and is intended to be a helpful addition to common Python data analysis tools such as pandas, scikit-learn, and matplotlib.

<a name="setup"></a>
## Setup

```
$ pip3 install Dora
$ python3
>>> from Dora import Dora
```

<a name="use"></a>
## Usage

<a name="config" ></a>
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

<a name="clean" ></a>
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

<a name="feature" ></a>
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

# extract a transformation of another feature
>>> dora.extract_feature('C', 'twoC', lambda x: x * 2)
>>> dora.data
   A   B  C  D=left  D=right  twoC
0  1   2  0       1        0     0
1  4 NaN  1       0        1     2
2  7   8  2       1        0     4
```

<a name="visual" ></a>
#### Visualization

```python
# plot a single feature against the output variable
dora.plot_feature('column-name')

# render plots of each feature against the output variable
dora.explore()
```

<a name="model" ></a>
#### Model Validation

```python
# create random partition of training / validation data (~ 80/20 split)
dora.set_training_and_validation()

# train a model on the data
X = dora.training_data[dora.input_columns()]
y = dora.training_data[dora.output]

some_model.fit(X, y)

# validate the model
X = dora.validation_data[dora.input_columns()]
y = dora.validation_data[dora.output]

some_model.score(X, y)
```

<a name="version" ></a>
#### Data Versioning

```python
# save a version of your data
>>> dora.data
   A   B  C      D  useless_feature
0  1   2  0   left                1
1  4 NaN  1  right                1
2  7   8  2   left                1
>>> dora.snapshot('initial_data')

# keep track of changes to data
>>> dora.remove_feature('useless_feature')
>>> dora.extract_ordinal_feature('D')
>>> dora.impute_missing_values()
>>> dora.scale_input_values()
>>> dora.data
   A         B         C    D=left   D=right
0  1 -1.224745 -1.224745  0.707107 -0.707107
1  4  0.000000  0.000000 -1.414214  1.414214
2  7  1.224745  1.224745  0.707107 -0.707107

>>> dora.logs
["self.remove_feature('useless_feature')", "self.extract_ordinal_feature('D')", 'self.impute_missing_values()', 'self.scale_input_values()']

# use a previous version of the data
>>> dora.snapshot('transform1')
>>> dora.use_snapshot('initial_data')
>>> dora.data
   A   B  C      D  useless_feature
0  1   2  0   left                1
1  4 NaN  1  right                1
2  7   8  2   left                1
>>> dora.logs
[]

# switch back to your transformation
>>> dora.use_snapshot('transform1')
>>> dora.data
   A         B         C    D=left   D=right
0  1 -1.224745 -1.224745  0.707107 -0.707107
1  4  0.000000  0.000000 -1.414214  1.414214
2  7  1.224745  1.224745  0.707107 -0.707107
>>> dora.logs
["self.remove_feature('useless_feature')", "self.extract_ordinal_feature('D')", 'self.impute_missing_values()', 'self.scale_input_values()']
```

<a name="test" ></a>
## Testing

To run the test suite, simply run `python3 spec.py` from the `Dora` directory.

<a name="contribute" ></a>
## Contribute

Pull requests welcome! Feature requests / bugs will be addressed through issues on this repository. While not every feature request will necessarily be handled by me, maintaining a record for interested contributors is useful.

Additionally, feel free to submit pull requests which add features or address bugs yourself.


<a name="license" ></a>
## License

**The MIT License (MIT)**

> Copyright (c) 2016 Nathan Epstein
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
