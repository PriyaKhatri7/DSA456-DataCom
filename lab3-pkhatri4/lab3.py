#
# Author: Priya Khatri
# Student Number: 110149176
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number): #find the number * number -1 * number-2 * ...1
	if(number == 0):
		return 1
	else:
		return number*factorial(number-1) #For recursively it's this but stops when number is 0 which returns 1


#this is easier than below linear_search()
def recursive_linear_search(list, key, index): #find the key in the list and the index
	if list is None or len(list) == 0: #"is None" is same as "not list" but "not list" is better python
		return - 1
	elif list[0] == key:
		return index
	else:
		return recursive_linear_search(list[1:], key, index+1) #calling the same function but 1 to the end. has to pass key because it's recurisve so it's over and over to pass
								#index++ becareful in using this. you need something to pass you do index+1

def linear_search(list, key):
	#return recursive_linear_search
    return recursive_linear_search(list, key, 0) #this should be doing things recursively so you also have to pass the position

#For recursive_linear_search I used a helper function which does the actual recursion linear search. This function takes an index along with list and key. 
#This index is the current index we are going to search for the key. If match is found then we return the index else we will recursively search for index+1. 
#If index reaches the end of list and we haven't found the key then we return -1.

def binary_search_helper(list, low, high, key): #add low index and high index.
	if(high >= low):
		mid = (high + low) //2
		if list[mid] == key:
			return mid
		elif list[mid] > key:
			return binary_search(list, low, mid-1, key)
		else:
			return binary_search(list, mid +1, high, key)
	else:
		return -1

def binary_search(self,list,key):
    return binary_search_helper(list,0,len(list)-1,key)

#For binary search I used a binary search helper function wihch does the recursive part. The idea is pretty simple given low and high indices, compare the key with element at middle index,
#if they are equal then it retusn the middle index
#if the key is greater than search in the right part else search in the left part.
#if we haven't found key, it return -1.