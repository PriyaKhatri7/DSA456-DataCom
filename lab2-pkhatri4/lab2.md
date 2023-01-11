# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;

	for i in range(0,number):
		x = (i+1)
		total+=(x*x)

	return total
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1, number):
		total*=(i+1)
	return total
```


## In class portion


### Group members
List the members of your group member below:

	* Priya Khatri
	* Anusmita Chanda

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Priya Khatri |  3.739s | 1.444s |
| Anusmita Chanda | 3.384s | 1.555s |


### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 1.444s | 1.555s | 0.111s |
|fibonacci | 3.384s | 3.739s | 0.355s  |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.
- For function 1 about regarding rock, paper, scissors there wasn't much of a difference however I realized that in syntax I didn't correctly handle the case sensitivity well. 
- Function 2 is done in a different approch, Anusmita did hers in a for loop using range and I did mines with an if else with additionally asking the user to enter some data so they will run differently but should pass the test around similar timespeed but mines might be a bit longer
- Function 3 is the exact same code however Anusmita was faster by 0.355s. I think this is based on how fast our laptop is running the test
- Function 4 sum_to_goal is identicle code syntax as well but I am using list and Amusmita is not. Based on the test we've run mines is faster by 0.111s and it seems like maybe it has to do with using list since that is mostly the major difference.
- The UpCounter() class and DownCounter() class is also about the same syntax however sligthly different where Amusmita us using def __init__ in her downCounter as well which i am not, just the update function.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
What i notice about the difference is small in sum_to_goal because we are both using different methods and but that is why there isn't much of a difference in speed between each function of sum_to_number and fibonacci.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?
Since the fibonacci function is done the same way there is no extra space resources however in sum_to_goal after seeing the different, the range, len, list order does use a bit of extra space resource in the file 

3. What sort of conclusions can you draw based on your observations?
Overall, programmers can have different code and get the same result it's just some takes longer than the other and some is quicker. It is important however to make sure you are using the most efficient method.


