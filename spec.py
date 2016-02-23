import unittest
from main import Dora
import pandas as pd

class TestDora(unittest.TestCase):
  def setUp(self):
    self.dora = Dora()
    self.dora.configure(output = 'A', data = './spec_data.csv')

  def test_configure(self):
    data = pd.read_csv('./spec_data.csv')
    self.assertEqual(self.dora.output, 'A')
    self.assertTrue(self.dora.data.equals(data))

  def test_remove_feature(self):
    self.dora.remove_feature('useless_feature')
    self.assertFalse('useless_feature' in self.dora.data.columns)

  def test_extract_feature(self):
    self.dora.extract_feature(
      'useless_feature',
      'another_useless_feature',
      lambda x: x * 2
    )

    actual_column = list(self.dora.data['another_useless_feature'])
    expected_column = [2, 2, 2]
    self.assertEqual(actual_column, expected_column)

  def test_impute_missing_values(self):
    del self.dora.data['D']
    self.dora.impute_missing_values()

    actual_column = list(self.dora.data['B'])
    expected_column = [2.0, 5.0, 8.0]
    self.assertEqual(actual_column, expected_column)

  def test_scale_input_values(self):
    del self.dora.data['D'], self.dora.data['B']
    self.dora.scale_input_values()

    actual_column = list(self.dora.data['C'])
    expected_column = [-1.224745, 0.0, 1.224745]
    pairwise_diffs = map(
      lambda actual, expected: abs(actual - expected),
      actual_column,
      expected_column
    )
    total_diff = sum(pairwise_diffs)
    self.assertAlmostEqual(total_diff, 0, places = 6)

  def test_extract_ordinal_feature(self):
    self.dora.extract_ordinal_feature('D')
    features = self.dora.data.columns
    self.assertTrue('D=left' in features and 'D=right' in features)

  def test_input_columns(self):
    actual_input_columns = list(self.dora.input_columns())
    expected_input_columns = list(self.dora.data.columns)
    expected_input_columns.remove(self.dora.output)
    self.assertEqual(actual_input_columns, expected_input_columns)

  def test_logs(self):
    self.dora.extract_ordinal_feature('D')
    self.dora.impute_missing_values()
    self.dora.scale_input_values()

    actual_logs = self.dora.logs
    expected_logs = [
      "self.extract_ordinal_feature('D')",
       'self.impute_missing_values()',
       'self.scale_input_values()'
    ]
    self.assertEqual(actual_logs, expected_logs)

  def test_snapshots(self):
    self.dora.snapshot('start')
    self.dora.extract_ordinal_feature('D')
    self.dora.use_snapshot('start')

    self.assertEqual(self.dora.logs, [])
    self.assertTrue(self.dora.data.equals(self.dora.initial_data))

if __name__ == '__main__':
    unittest.main()
