#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 1
#   To use this, run: python test_lab1.py
#   Tested using Python 3.10
#

import unittest
from lab1 import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal,UpCounter,DownCounter

class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab1"""
    
    def test_win_rock_scissors_paper(self):
        self.assertEqual(wins_rock_scissors_paper("rock","scissors"),True)
        self.assertEqual(wins_rock_scissors_paper("rock","paper"),False)
        self.assertEqual(wins_rock_scissors_paper("scissors".upper(),"paper"),True)
        self.assertEqual(wins_rock_scissors_paper("Scissors","Rock"),False)
        self.assertEqual(wins_rock_scissors_paper("paper","sCiSsOrs"),False)
        self.assertEqual(wins_rock_scissors_paper("paper".title(),"ROCK"),True)
        self.assertEqual(wins_rock_scissors_paper("paper","PaPeR"),False)
        self.assertEqual(wins_rock_scissors_paper("rock","ROCK"),False)
        self.assertEqual(wins_rock_scissors_paper("SCISSORS","scissors"),False)


    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)
        self.assertEqual(fibonacci(35),9227465)


    def test_sum_to_goal(self):
        mylist =[5741, 5742, 4234, 1950, 2255, 3899, 974, 1332, 726, 4208, 2914, 4721, 2094, 2252, 1892, 
                676, 3097, 2725, 1639, 1122, 4212, 3191, 616, 5346, 1121, 444, 2873, 2597, 1134, 1262, 3838, 
                1564, 4176, 1873, 4068, 3277, 1765, 4431, 1256, 924, 3440, 4143, 5444, 5653, 5436, 3992, 4902, 
                2476, 5976, 3699, 2683, 2786, 4001, 2293, 2191, 2530, 4336, 3000, 4713, 2061, 4900, 2844, 128, 
                4539, 465, 550, 5067, 2636, 5579, 512, 323, 4547, 4125, 4112, 4746, 3860, 1104, 1261, 1791, 5301, 
                3293, 1464, 3989, 193, 4036, 1132, 3247, 4618, 4033, 3332, 3579, 3221, 5410, 2242, 1495, 2513, 
                4430, 4508, 3262, 3259]

        self.assertEqual(sum_to_goal(mylist,8716),18969664)
        self.assertEqual(sum_to_goal(mylist,3385),1470976)
        self.assertEqual(sum_to_goal(mylist,7327),13257612)
        self.assertEqual(sum_to_goal(mylist,3103),2399496)
        self.assertEqual(sum_to_goal(mylist,3470),632461)
        self.assertEqual(sum_to_goal(mylist,0),0)
        self.assertEqual(sum_to_goal(mylist,3471),0)
        self.assertEqual(sum_to_goal(mylist,5080),0)


    def test_UPCounter(self):
        counter=UpCounter(5)
        counter.update()
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),15)
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),25)


    def test_DownCounter(self):
        counter=DownCounter(3)
        counter.update()
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),-9)
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),-15)
 
if __name__ == '__main__':
    unittest.main()
