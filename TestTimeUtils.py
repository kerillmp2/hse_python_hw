import unittest
from TimeUtils import TimeUtils

class TestTimeUtils(unittest.TestCase):

    def setUp(self):
        pass


    def test_is_leap_year(self):
        self.assertEqual(TimeUtils.is_leap_year(2000), True)
        self.assertEqual(TimeUtils.is_leap_year(2010), False)
        self.assertEqual(TimeUtils.is_leap_year(2100), False)
        self.assertEqual(TimeUtils.is_leap_year(2004), True)
        self.assertEqual(TimeUtils.is_leap_year(2304), True)


    def test_days_in_month(self):
        self.assertEqual(TimeUtils.days_in_month(2000, "FEBRUARY"), 29)
        self.assertEqual(TimeUtils.days_in_month(2001, "FEBRUARY"), 28)
        self.assertEqual(TimeUtils.days_in_month(2001, "august"), 31)
        self.assertEqual(TimeUtils.days_in_month(999999, "September"), 30)
        
    
if __name__ == "__main__":
    unittest.main()
