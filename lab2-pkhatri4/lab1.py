'''Lab 1'''
# Author: Priya Khatri
# Student Number: 110149176
#
# Place the code for your lab 1 here.  Read the specs carefully.
# Function name must be exactly as provided.
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Priya Khatri
# Student Number: 110149176

def wins_rock_scissors_paper(player_action, opponent_action):
    '''Function 1: rock paper scissors'''
    p_1 = player_action.lower()
    p_2 = opponent_action.lower()
    if p_1 == "rock" and p_2 == 'scissors':
        return True
    elif p_1 == 'paper' and p_2 == 'rock':
        return True
    elif p_1 == 'scissors' and p_2 == 'paper':
        return True #if player has won
    else:
        return False #if it was a tie or loss

def factorial(num):
    '''Function 2: Factorial of a number using recursion'''
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

number = int(input("Enter a number:"))

if number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is", factorial(number))

def fibonacci(num):
    '''Function 3: for nth Fibonacci number using recursion'''
    if num < 0:
        print("Incorrect input")

    elif num == 0:
        return 0

    #Check if n is 1,2 it will return 1
    elif num == 1 or num == 2:
        return 1

    #Return sum of the 2 previous fib numbers
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def sum_to_goal(nums, goal):
    '''Function 4: Finds 2 nums in the list that sum up to the goal value'''
    #Variable set to 0
    product = 0

    #Loop from i=0 to i=last idx of nums list
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if i != j:
                #if the sum of i and j of nums list equals to the goal
                #number then calculating and returning the product of those 2 value
                if(nums[i] + nums[j]) == goal:
                    product = nums[i] * nums[j]
                    return product
    #After the loop, if still no numbers found in the nums list that sum up
    #to goal number then return the inital value of product that is 0
    return product

class UpCounter:
    '''keeps track of a number. the number can be increased by a fixed step size'''
    def __init__(self, stepsize):
        self.stepsize = stepsize
        self.num = 0

    def count(self):
        '''returns the current counter value'''
        return self.num

    def update(self):
        '''increases the counter value by stepsize'''
        self.num = self.num + self.stepsize

class DownCounter(UpCounter):
    '''counter decrements the counter value by stepsize'''
    def update(self):
        self.count = self.count - self.stepsize
