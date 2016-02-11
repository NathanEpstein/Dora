import pandas as pd
import math
from sklearn import preprocessing

class Dora:
  def __init__(self, csv_file_path = None):
    if (csv_file_path != None):
      self.data = pd.DataFrame.from_csv(csv_file_path)
      self.transformed_data = self.data

  def data(self, new_data = None):
    if (not new_data): return self.data
    self.data = pd.DataFrame(new_data)
    self.transformed_data = pd.DataFrame(new_data)

  def pre_process(self, config):
    self.output = config['output'] #output column label
    self.ordinal_features = config['ordinal_features'] #ordinal column labels

  def extract_feature(self, config):
    new_feature_column = map(
      config['mapper'],
      self.transformed_data['feature_to_map']
    )
    self.transformed_data[config['new_feature_name']] = new_feature_column

  def _extract_ordinal_features(self):
    for feature in self.ordinal_features:
      # do something with the feature...

  def _impute_missing_values(self):
    # copy output column and replace it after imputing is applied
    output_copy = self.transformed_data[self.output].copy()
    imp = preprocessing.Imputer(copy = False)
    imp.fit_transform(self.transformed_data)
    self.transformed_data[self.output] = output_copy

  def _scale_input_values(self):
    # copy output column and replace it after scaling is applied
    output_copy = self.transformed_data[self.output].copy()
    preprocessing.scale(self.transformed_data, copy = False)
    self.transformed_data[self.output] = output_copy

  def _set_training_and_validation():
    training_rows = np.random.rand(len(self.transformed_data)) < 0.8
    self.training_data = self.transformed_data[training_rows]
    self.validation_data = self.transformed_data[~training_rows]
