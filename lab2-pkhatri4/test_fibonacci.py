#
#   Author: Catherine Leung
#   Timing for fibonacci
#   To use this, run: python test_fibonacci.py
#


import unittest
from lab1 import fibonacci

class FibTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab1"""
    

    def test_fibonacci(self):
        self.assertEqual(fibonacci(35),9227465)

if __name__ == '__main__':
    unittest.main()
