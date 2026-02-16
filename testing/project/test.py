import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)
    
    def test_list_fraction(self):
        data = [Fraction(1,2), Fraction(1,2), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result,1)
    


if __name__ == "__name_":
    unittest.main()
