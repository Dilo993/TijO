import unittest
import os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from QE import QuadraticEquation as QE

class QuadraticEquation_test(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        a,b,c=0,2,4

        self.assertRaises(ValueError, QE, a,b,c)

if __name__ == '__main__':
    unittest.main()