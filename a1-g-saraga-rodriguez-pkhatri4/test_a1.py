#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment1
#   To use this, run: python test_a1.py

import unittest
from a1 import SortedList

class A1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
 
    def test_insert(self):
        my_data = [4,8,6,7,1,3,5,10,15,2,9]
        my_data2 = ["orange", "apple", "cherry", "banana", "mango","pear","plum"]
        first_list = SortedList()
        second_list = SortedList()
        for i in my_data:
            first_list.insert(i)

        for i in my_data2:
            second_list.insert(i)

        my_data.sort()
        my_data2.sort()
        j = 0
        for i in first_list:
            self.assertEqual(i,my_data[j])
            j+=1

        self.assertEqual(j,len(my_data))

        j = 0
        for i in second_list:
            self.assertEqual(i,my_data2[j])
            j+=1

        self.assertEqual(j,len(my_data2))

        j = len(my_data) - 1
        for i in reversed(first_list):
            self.assertEqual(i,my_data[j])
            j-=1

        j = len(my_data2) - 1
        for i in reversed(second_list):
            self.assertEqual(i,my_data2[j])
            j-=1



    def test_len(self):
        my_data = [4,8,6,7,1,3,5,10,15,2,9]
        my_data2 = ["orange", "apple", "cherry", "banana", "mango","pear","plum"]
        first_list = SortedList()
        second_list = SortedList()
        j=0
        for i in my_data:
            first_list.insert(i)
            j+=1
            self.assertEqual(len(first_list),j)            

        j=0
        for i in my_data2:
            second_list.insert(i)
            j+=1
            self.assertEqual(len(second_list),j)            



    def test_remove(self):
        my_data = [4,8,6,7,1,3,5,10,15,2,9]
        sorted_data = [4,8,6,7,1,3,5,10,15,2,9]
        sorted_data.sort()

        first_list = SortedList()

        for i in my_data:
            first_list.insert(i)

        for i in my_data:
            self.assertEqual(first_list.remove(i),True)
            sorted_data.remove(i)
            self.assertEqual(len(first_list),len(sorted_data))

            j = 0
            for k in first_list:
                self.assertEqual(k,sorted_data[j])
                j+=1

            j = len(sorted_data) - 1
            for k in reversed(first_list):
                self.assertEqual(k,sorted_data[j])
                j-=1



    def test_is_present(self):
        my_data = [4,8,6,7,1,3,5,10,15,2,9]
        my_data2 = ["orange", "apple", "cherry", "banana", "mango","pear","plum"]
        not_present = [16, 11, 12, 25,100]
        not_present2 = ["lichee", "peach", "watermelon", "grape"]
        first_list = SortedList()
        second_list = SortedList()
        for i in my_data:
            first_list.insert(i)

        for i in my_data2:
            second_list.insert(i)

        for i in my_data:
            self.assertEqual(first_list.is_present(i),True)

        for i in my_data2:
            self.assertEqual(second_list.is_present(i),True)

        for i in not_present:
            self.assertEqual(first_list.is_present(i),False)

        for i in not_present2:
            self.assertEqual(second_list.is_present(i),False)




if __name__ == '__main__':
    unittest.main()
