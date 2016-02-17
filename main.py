import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer

class Dora:
  def __init__(self, csv_file_path = None):
    self.logs = []
    self.snapshots = {}
    if (csv_file_path != None):
      self.initial_data = pd.read_csv(csv_file_path)
      self.data = self.initial_data.copy()

  def extract_feature(self, config):
    new_feature_column = map(
      config['mapper'],
      self.data[config['feature_to_map']]
    )
    self.data[config['new_feature_name']] = list(new_feature_column)
    self._log("self.extract_feature({0})".format(config))

  def impute_missing_values(self):
    column_names = self.data.columns
    output_copy = self.data[self.output].copy()
    imp = preprocessing.Imputer()
    imp.fit(self.data)
    imputed_data = imp.transform(self.data)
    self.data = pd.DataFrame(imputed_data)
    self.data.columns = column_names
    self.data[self.output] = output_copy
    self._log("self.impute_missing_values()")

  def scale_input_values(self):
    column_names = list(self.data.columns)
    column_names.remove(self.output)
    self.data[column_names] = preprocessing.scale(self.data[column_names])
    self._log("self.scale_input_values()")

  def extract_ordinal_feature(self, feature_name):
    feature = self.data[feature_name]
    feature_dictionaries = map(
      lambda x: { str(feature_name): str(x) },
      feature
    )
    vec = DictVectorizer()
    one_hot_matrix = vec.fit_transform(feature_dictionaries).toarray()
    one_hot_matrix = pd.DataFrame(one_hot_matrix)
    one_hot_matrix.columns = vec.get_feature_names()
    self.data = pd.concat(
      [
        self.data,
        one_hot_matrix
      ],
      axis = 1
    )
    del self.data[feature_name]
    self._log("self.extract_ordinal_feature({0})".format(feature_name))

  def set_training_and_validation(self):
    training_rows = np.random.rand(len(self.data)) < 0.8
    self.training_data = self.data[training_rows]
    self.validation_data = self.data[~training_rows]

  def input_data(self):
    columns = list(self.data.columns)
    columns.remove(self.output)
    return self.data[columns]

  def plot_feature(self, feature_name):
    x = self.data[feature_name]
    y = self.data[self.output]
    fit = np.polyfit(x, y, deg = 1)
    fig, ax = plt.subplots()
    ax.plot(x, fit[1] + fit[0] * x)
    ax.scatter(x, y)
    ax.set_title("{0} vs. {1}".format(feature_name, self.output))
    fig.show()

  def explore(self):
    features = self.input_data().columns
    row_count = math.floor(math.sqrt(len(features)))
    col_count = math.ceil(len(features) / row_count)
    figure = plt.figure(1)

    for index, feature in enumerate(features):
      figure.add_subplot(row_count, col_count, index + 1)
      x = self.data[feature]
      y = self.data[self.output]
      fit = np.polyfit(x, y, deg = 1)
      plt.plot(x, fit[0] * x + fit[1])
      plt.scatter(x, y)
      plt.title("{0} vs. {1}".format(feature, self.output))
    plt.show()

  def snapshot(self, name):
    snapshot = {
      "data": self.data.copy(),
      "logs": self.logs.copy()
    }
    self.snapshots[name] = snapshot

  def use_snapshot(self, name):
    self.data = self.snapshots[name]["data"]
    self.logs = self.snapshots[name]["logs"]

  def _log(self, string):
    self.logs.append(string)