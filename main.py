import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer

class Dora:
  def __init__(self, csv_file_path = None):
    if (csv_file_path != None):
      self.initial_data = pd.read_csv(csv_file_path)
      self.data = self.initial_data.copy()

  def extract_feature(self, config):
    new_feature_column = map(
      config['mapper'],
      self.data[config['feature_to_map']]
    )
    self.data[config['new_feature_name']] = list(new_feature_column)

  def impute_missing_values(self):
    column_names = self.data.columns
    output_copy = self.data[self.output].copy()
    imp = preprocessing.Imputer()
    imp.fit(self.data)
    imputed_data = imp.transform(self.data)
    self.data = pd.DataFrame(imputed_data)
    self.data.columns = column_names
    self.data[self.output] = output_copy

  def scale_input_values(self):
    column_names = self.data.columns
    output_copy = self.data[self.output].copy()
    scaled_data = preprocessing.scale(self.data)
    self.data = pd.DataFrame(scaled_data)
    self.data.columns = column_names
    self.data[self.output] = output_copy

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

  def set_training_and_validation(self):
    training_rows = np.random.rand(len(self.data)) < 0.8
    self.training_data = self.data[training_rows]
    self.validation_data = self.data[~training_rows]

  def input_data(self):
    columns = list(self.data.columns)
    columns.remove(self.output)
    return self.data[columns]