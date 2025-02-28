import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from math_lib import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        result = self.calc.add(3, 2)
        self.assertEqual(result, 5)

    def test_devide_by_zero(self): 
        print("** test_devide_by_zero()")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None

if __name__ == '__main__':
    unittest.main()