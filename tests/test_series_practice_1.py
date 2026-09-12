import unittest
import pandas as pd
import numpy as np
from src.series_practice_1 import *

class TestElectronicsStoreSalesAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Recreate the test Series so it’s consistent and self-contained
        dates = [
            "2023-10-10", "2023-10-11", "2023-10-12",
            "2023-10-13", "2023-10-14", "2023-10-15", "2023-10-16"
        ]
        sales = [1500, 2300, 2100, 2400, 1800, 2200, 2050]
        cls.series = pd.Series(sales, index=dates)

    def test_get_total_sales(self):
        """Total sales should sum correctly to a single scalar value."""
        result = get_total_sales(self.series)
        # Allow scalar or small array
        if isinstance(result, (pd.Series, np.ndarray)):
            result = result.sum()
        self.assertEqual(result, 14350)

    def test_get_date_with_highest_sales(self):
        """Highest sales should correspond to Oct 13."""
        result = get_date_with_highest_sales(self.series)
        # Handle Index or Series return types
        if isinstance(result, (pd.Index, pd.Series, np.ndarray)):
            result = result.tolist()[0]
        self.assertEqual(result, "2023-10-13")

    def test_get_average_sales(self):
        """Mean sales should be approximately 2050.0."""
        result = get_average_sales(self.series)
        # Allow Pandas or NumPy scalar
        if isinstance(result, (pd.Series, np.ndarray)):
            result = float(np.mean(result))
        self.assertAlmostEqual(result, 2050.0, 2)

    def test_get_days_with_sales_above(self):
        """Days with sales above 2000 should match exact expected list."""
        result = get_days_with_sales_above(self.series, 2000)
        # Normalize to list of strings for comparison
        if isinstance(result, (pd.Index, pd.Series, np.ndarray)):
            result = result.tolist()
        expected = ["2023-10-11", "2023-10-12", "2023-10-13", "2023-10-15", "2023-10-16"]
        self.assertEqual(result, expected)

    def test_get_sales_on_selected_days(self):
        """Fancy indexing should match expected positional values."""
        result = get_sales_on_selected_days(self.series, [0, 3, 5])
        # Normalize to list of numbers
        if isinstance(result, (pd.Series, pd.Index, np.ndarray)):
            result = result.tolist()
        expected = [1500, 2400, 2200]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
