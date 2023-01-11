#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment1
#   To use this, run: python test_a1.py

import unittest
from a2 import ChainingHash, LinearProbingHash

class A2TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
    def test_ChainingHash_insert(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]
        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = ChainingHash()

        # test that return value from insert is correct,
        # capacity is unchanged, number of records is correctly
        # returned
        for i in range(32):
            self.assertEqual(table.insert(keys[i],values[i]),True)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),i+1)

        # test that return value from insert is correct when adding
        # key/value pair where key already exists
        # capacity is unchanged, number of records is not changed
        for i in range(32):
            self.assertEqual(table.insert(keys[i],values[i]+1),False)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),32)


    def test_ChainingHash_search(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = ChainingHash()

        for i in range(32):
            table.insert(keys[i],values[i])

        # test that inserted key/value pairs have correct matching 
        # results
        for i in range(32):
            self.assertEqual(table.search(keys[i]),values[i])

        # search for keys that do not exist in table, search
        # should return None
        for i in range(32,48):
            self.assertEqual(table.search(keys[i]),None)


    def test_ChainingHash_modify(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = ChainingHash()

        # Try to modify records that are not in table.  function
        # should do nothing and return false
        for i in range(32):
            self.assertEqual(table.modify(keys[i],values[i]),False)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),0)

        # test that no records were added
        for i in range(32):
            self.assertEqual(table.search(keys[i]),None)


        for i in range(32):
            table.insert(keys[i],values[i])

        # test that modify returns true for records that exists
        # as we are modifying what is already in table, the 
        # capacity and number of records should not change
        for i in range(32):
            self.assertEqual(table.modify(keys[i],values[i]+10),True)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),32)


        # test that values were correctly modified
        for i in range(32):
            self.assertEqual(table.search(keys[i]),values[i]+10)

                    
    def test_ChainingHash_grow(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = ChainingHash(4)
        self.assertEqual(table.capacity(),4)
        self.assertEqual(len(table),0)

        for i in range(4):
            table.insert(keys[i],values[i])

        self.assertEqual(table.capacity(),4)
        self.assertEqual(len(table),4)

        table.insert(keys[4],values[4])
        self.assertEqual(table.capacity(),8)
        self.assertEqual(len(table),5)

        for i in range(5,8):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),8)
        self.assertEqual(len(table),8)

        table.insert(keys[8],values[8])
        self.assertEqual(table.capacity(),16)
        self.assertEqual(len(table),9)

        for i in range(9,16):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),16)
        self.assertEqual(len(table),16)

        table.insert(keys[16],values[16])
        self.assertEqual(table.capacity(),32)
        self.assertEqual(len(table),17)

        for i in range(17,32):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),32)
        self.assertEqual(len(table),32)

        table.insert(keys[32],values[32])
        self.assertEqual(table.capacity(),64)
        self.assertEqual(len(table),33)

        for i in range(32,48):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),64)
        self.assertEqual(len(table),48)

        # test that values are all still present after all insertions
        for i in range(48):
            self.assertEqual(table.search(keys[i]),values[i])




    def test_ChainingHash_remove(self):
        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = ChainingHash()

        for i in range(0,48):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),64)
        self.assertEqual(len(table),48)

        total=48
        # remove every other value, return should be true
        for i in range(0,48,2):
            total-=1
            self.assertEqual(table.remove(keys[i]),True)
            self.assertEqual(len(table),total)
            self.assertEqual(table.capacity(), 64)

        # perform search and make sure that only those that
        # should be gone are gone, and those that should be there
        # are there 
        for i in range(0,48):
            if i%2 == 0:
                self.assertEqual(table.search(keys[i]),None)
            else:
                self.assertEqual(table.search(keys[i]),values[i])

        # removing records that are not there should result 
        # in false return
        for i in range(0,48,2):
            self.assertEqual(table.remove(keys[i]),False)
            self.assertEqual(len(table),total)
            self.assertEqual(table.capacity(), 64)


        # ensure that trying to remove records that do not exist
        # has no effect on records that are in table
        for i in range(0,48):
            if i%2 == 0:
                self.assertEqual(table.search(keys[i]),None)
            else:
                self.assertEqual(table.search(keys[i]),values[i])


    def test_LinearProbingHash_insert(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]
        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = LinearProbingHash()

        # test that return value from insert is correct,
        # capacity is unchanged, number of records is correctly
        # returned
        for i in range(22):
            self.assertEqual(table.insert(keys[i],values[i]),True)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),i+1)

        # test that return value from insert is correct when adding
        # key/value pair where key already exists
        # capacity is unchanged, number of records is not changed
        for i in range(22):
            self.assertEqual(table.insert(keys[i],values[i]+1),False)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),22)


    def test_LinearProbingHash_search(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = LinearProbingHash()

        for i in range(32):
            table.insert(keys[i],values[i])

        # test that inserted key/value pairs have correct matching 
        # results
        for i in range(32):
            self.assertEqual(table.search(keys[i]),values[i])

        # search for keys that do not exist in table, search
        # should return None
        for i in range(32,48):
            self.assertEqual(table.search(keys[i]),None)


    def test_LinearProbingHash_modify(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = LinearProbingHash()

        # Try to modify records that are not in table.  function
        # should do nothing and return false
        for i in range(22):
            self.assertEqual(table.modify(keys[i],values[i]),False)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),0)

        # test that no records were added
        for i in range(22):
            self.assertEqual(table.search(keys[i]),None)


        for i in range(22):
            table.insert(keys[i],values[i])

        # test that modify returns true for records that exists
        # as we are modifying what is already in table, the 
        # capacity and number of records should not change
        for i in range(22):
            self.assertEqual(table.modify(keys[i],values[i]+10),True)
            self.assertEqual(table.capacity(), 32)
            self.assertEqual(len(table),22)


        # test that values were correctly modified
        for i in range(22):
            self.assertEqual(table.search(keys[i]),values[i]+10)

                    
    def test_LinearProbingHash_grow(self):


        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = LinearProbingHash(8)
        self.assertEqual(table.capacity(),8)
        self.assertEqual(len(table),0)

        for i in range(5):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),8)
        self.assertEqual(len(table),5)

        table.insert(keys[5],values[5])
        self.assertEqual(table.capacity(),16)
        self.assertEqual(len(table),6)



        for i in range(6,11):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),16)
        self.assertEqual(len(table),11)

        table.insert(keys[11],values[11])
        self.assertEqual(table.capacity(),32)
        self.assertEqual(len(table),12)



        for i in range(12,22):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),32)
        self.assertEqual(len(table),22)

        table.insert(keys[22],values[22])
        self.assertEqual(table.capacity(),64)
        self.assertEqual(len(table),23)

        for i in range(23,44):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),64)
        self.assertEqual(len(table),44)

        table.insert(keys[44],values[44])
        self.assertEqual(table.capacity(),128)
        self.assertEqual(len(table),45)

        for i in range(45,48):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),128)
        self.assertEqual(len(table),48)

        # test that values are all still present after all insertions
        for i in range(48):
            self.assertEqual(table.search(keys[i]),values[i])




    def test_LinearProbingHash_remove(self):
        keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

        values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]

        table = LinearProbingHash()

        for i in range(0,48):
            table.insert(keys[i],values[i])
        self.assertEqual(table.capacity(),128)
        self.assertEqual(len(table),48)

        total=48
        # remove every other value, return should be true
        for i in range(0,48,2):
            total-=1
            self.assertEqual(table.remove(keys[i]),True)
            self.assertEqual(len(table),total)
            self.assertEqual(table.capacity(), 128)

        # perform search and make sure that only those that
        # should be gone are gone, and those that should be there
        # are there 
        for i in range(0,48):
            if i%2 == 0:
                self.assertEqual(table.search(keys[i]),None)
            else:
                self.assertEqual(table.search(keys[i]),values[i])

        # removing records that are not there should result 
        # in false return
        for i in range(0,48,2):
            self.assertEqual(table.remove(keys[i]),False)
            self.assertEqual(len(table),total)
            self.assertEqual(table.capacity(), 128)


        # ensure that trying to remove records that do not exist
        # has no effect on records that are in table
        for i in range(0,48):
            if i%2 == 0:
                self.assertEqual(table.search(keys[i]),None)
            else:
                self.assertEqual(table.search(keys[i]),values[i])



if __name__ == '__main__':
    unittest.main()
