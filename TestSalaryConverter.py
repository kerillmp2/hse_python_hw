import unittest
from SalaryConverter import SalaryConverter

class TestSalaryConverter(unittest.TestCase):

    def setUp(self):
        pass


    def test_calculate_hour_income(self):
        self.assertEqual(SalaryConverter.calculate_hour_income(1, 8), 1)
        self.assertEqual(SalaryConverter.calculate_hour_income(1, 8000), 1000)
        self.assertEqual(SalaryConverter.calculate_hour_income(1, 1), 0.12)
        self.assertEqual(SalaryConverter.calculate_hour_income(5, 80), 2)
        
    
if __name__ == "__main__":
    unittest.main()
