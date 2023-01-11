#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 3
#   To use this, run: python test_lab3.py
#   Tested using Python 3
#

import unittest
from lab3 import factorial,linear_search,binary_search

class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab3"""
    
    def test_linear_search(self):
        mylist = [34, 1, 18, 20, 25, 30, 15, 16, 17, 22, 24, 31, 163, 9, 33, 55]
        self.assertEqual(linear_search(mylist,0), -1)
        self.assertEqual(linear_search(mylist,19), -1)
        self.assertEqual(linear_search(mylist,164), -1)
        curr = 0
        for i in mylist:
            self.assertEqual(linear_search(mylist,i),curr)
            curr+=1

    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_binary_search(self):
        mylist = [1, 2, 4, 5, 8, 10, 15, 22, 27, 29, 30, 33, 55, 81, 100, 108, 200, 205, 310, 315]
        self.assertEqual(binary_search(mylist,0),-1)
        self.assertEqual(binary_search(mylist,19),-1)
        self.assertEqual(binary_search(mylist,201),-1)
        self.assertEqual(binary_search(mylist,320),-1)
        curr = 0
        for i in mylist:
            self.assertEqual(binary_search(mylist,i),curr)
            curr+=1


 
if __name__ == '__main__':
    unittest.main()
