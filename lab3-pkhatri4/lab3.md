# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0): #1 unit time is taken to compare
		return 1
	elif (number == 1): #1 unit time is taken to compare
		return value
	else:
		return value * function1(value, number-1)
```
In the first run is (total time) = 1+1+ time of function1(value, n-1) .....(i), 
time of function1(value, n-1) = 1+1+ time of function(value, n-2).......(ii) # n is decreased by one each time and so on up to n=1
time of function1(value, n-(n-1)) = 1+1 (as at second condition because true and it reurns so no else block runs)
therefore, replacing (ii) in (i) total time = 1+1 + (1+1 + time of function1(value, n-2) 
											= 2 + (2 + time of function1(value, n-2)) 
if we add n-2 time then total time  =  2 + (2 +  (2+ function1(value, n-3))) and so on
so on each function call we add 2 + function1() with one less number so for n we add n times 2 so,
total time = 2+ 2+ 2+......2 (n times) 
			= 2n 

so time complexity = O(n) 

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ): #1 unit time
		return True
	else:
		if(mystring[a] != mystring[b]): #1 unit time
			return False #function ends
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```
In function2 we are calling recursive_function2() with a string, 0 and length -1 and in recursive_function2() if a >= b then it returns means functions ends means a can have maximum value is half of length of string and so b has minimum value can be up to half of length
In the else block if a character at index a and b is not the same then it returns means function ends not calling recursive_function2()
else is all conditions don't meet then it calls recursive to itself so each time the function is called it's incremented by 1 and b is decremented by 1 so a and b iterated max time is half of string let say length of string is n so manx iteration is n/2 now time of each iteration(function call) time is 2 unit so, for n/2 iteration 
total time = 2 * (n/2)
			= n

So therefore time complexity is T(n) = O(n)


### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0): #1 unit time
		return 1
	elif (number == 1): #1 unit time
		return value
	else:
		half = number // 2 #1 unit time
		result = function3(value, half)
		if (number % 2 == 0): #1 unit time
			return result * result
		else:
			return value * result * result

```
In each function call, time is 3 unit. it's calculating no of iteration(function call) if number is n in each function call execution we are calling function3() with number half of iteself so each time number gets half


T(0)=0 & T(1) = 1 (if n is even -> I would get to 6+T(n/2)XXXXXXXXXXXx)
T(n)= 7 + T(n/2) n is odd

number of function calls
T(n/2) = 7 + T(n/4) --> T(n) = 7 + 7 + T(n/4)
							 = 7 * 2 + T(n/2^2)
							 = 7 * 3 + T(n/2^3)
							 = 7 * k + T(n/2^k) #this is 1

so look at power of 2 kth function call number is n/2^k-1
last call number is 1 so let it was a kth call so
n/2k-1 >= 1 (we are doing integer devision , so we descarding fraction )
      n >= 2k-1 
taking log both side 
    log(n) >= (k-1)log(2)
    log2(n) >= k-1
    log2(n) +1 = k
so k is total number of calls as we assumed so 
total time = 3k(each call takes 3 unit of time so total calls is)
		   = 3(log2(n)+1)
		   = 3 log2(n) +3

So therefore time complexity is O (log2(n))

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
To write a recursive function first need to define a function factorial and put in the necessary input parameters. There should also always been atleast one base case where the problem cannot be reduced any further and it's easy to just produce the correct answer straight away. The base case will still do some of the work for the values and the recursive case will just solve the problem. 
This is an example of the 2 key elements of a recursive algorithm which was shown to us in lab3.py in function 1:
- the termination condition: n == 0
- the reduction step where the function calls itself with a smaller number each time: factorial(n-1)
In the same example we call this function with a postive integer, it will recursively call itself by decreasing the number. Each function  multiplies the number with the factorial of the number below it until it is equal to one. 
Our recursion ends hen the number reduces to 1. This is how you know it's the base condition. Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.  

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
When analyzing recursive functions from non-recursive functions you already need to declare the variables and functions in both. Then you count what is happening to your final equarion in each line of code by adding comments to each line or writing what each line is doing at the bottom. Such as seeing usually how amny times it goes through a loop or a condition.
Following that you establish the math expression for T(n) by adding up the operation counts in the comments as shown in the functions above. then to simplify your equation which is not done with a non-recursive function. Finally you state your final result and conclude with the time complexity of T(n) and/or O(n)
