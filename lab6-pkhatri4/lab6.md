
1. What sorting algorithm was the speaker trying to improve?

The sorting algorithm that Alexandrescu was trying to improve was the quicksort algorithm in reference to binary search. He said that no one knows how to sort a medium sized array (1000 elements) quickly and this is the challenge that he wants to get into. Alexandrescu has done the test and showed that with binary insertion sort it will always be slower than the linear insertion sort because he tried to increase the threshold, however that made things much slower. 

---
2. At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?

During the partition a pivot happens and this is where it will put the array in order. The order is everything smaller than the pivot number goes on the left side and everything larger goes on the right side and then it sorts through the algorithm. This is simplier and similar to lab 5 when we did this eercise to divide the pile of numbers by doing as mentioned above, there is a random number in the middle and we divide it into 2 groups. Take a pile and repeat the steps until there are 4 main piles. In this way you would do as many necessary depending on how many elements you have in your algorithm, considering Alexandrescu is talking about a quicksort implementation there won't be too many to go through and the best case is you find the median.

---
3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?

The partition size does perform on a 16 gnu for a simpler sort algorithm depending on the operating system. It also changes the threshold depending on the input given to the algorithm. For example, if the value given can be assigned then it will use a larger threshold otherwise, smaller which was explained as "clang" by Alexandrescu. This is important for creating space for the new operating systems, and moving around data. 


---
4. Regular insertion sort does a linear search backwards from end of array for correct spot to insert. According to the speaker, why does switching to a binary search not improve performance?

For regular insertion sort a linear search backwards from end of array to correct spot in the array is much faster than in a binary search and it always will be. Alexandrescu explains his process in increasing the threshold and thinking that it's less work to get to the same results so it must be better, furhtermore, after looking into it further with a 32 threeshold and making the comparison it came back with 15% reduction with the same amount of actions. However it came back 13% pessimization which means it takes more during runtime which is why binary search will always be slower even if there are fewer comparisons.

---
5. Describe what is meant by branch prediction? (this may require further research)

Branch predictor works well with highly predictable comparisons. This is because it a branch predictor likes to attempt to guess the outcome/destination between the operation is complete with very minimal context. This is supposed to increase the flow in instructions. For example, if we chose to do a search in the middle which will get us the most information then when it comes to a binary search the branch predictor won't have a good impact since they are harder to predict compared to a linear search where it will work excellent. However there is also something called "branchless binary" which is much more slow since it doesn't stop until it's finihsed going through all the bits.


---
6. What is meant by the term **informational entropy**? (this may require further research)

Informational entropy means to get the quantity of the information given and calculate using probability. This is very useful for things such as building tress. This is also why it goes in hand with branch predictability. The success rate would also be much higher passing percentage. Entropy looks at the amount of random variables or the results of them in a random process which can give different values that are present in the variable but also by the amount of surprise that the value of the variable holds. This explains a random variable as an average amount of information that can hold the variable's possible outcome.


---
7. If size == 15, what is size & 1?  if size == 16, what is size & 1?  Explain how right = first + 1 + (size & 1) avoids a conditional check.

	Hint:
	* The & is the bitwise AND operator in C/C++.  It takes the bit representation of the two operands and perform an AND operation on each of the corresponding bits to form a result
	* To do this question first convert 15, 16 and 1 to base 2 (use 5 digit representation for all of them).  Then perform an AND operation of the correseponding bits of the operands... this will get you a 5 digit binary value.  Convert the value back to base 10 .

In bitwise of size == 15, the size of &1 is 01111. If it were to convert the value from binary to base 10 then it would be 15 base-10. 

If the value of size == 16, the size of &1 is 10000. If it was to be converted back to to base 10 it would be 16 base-10

`right = first + 1 + (size & 1)` first is explained as positioning ourself in the middle of the array but then depending on how that is with the number of elements, i would try to make myself in the middle with an odd number of elements. This avoids the conditional check because there is no if condition in the code, meaning no `if(size = 1; right++)` which means this is going to be alot faster because it is a code with a jump.

---
8. Speaker suggests the following algorithm:
	* make_heap()
	* unguarded_insertion_sort()

	He suggests that by doing make_heap() first then you can do something called unguarded_insertion_sort().  Explain what is unguarded_insertion_sort() and why it is faster than regular insertion sort.  How does performing make_heap() allow you to do this?
	
When doing an `insertion_sort()` it takes more work because you have to make a heap first, hence `make_heap()` because `make_heap()` itelf has alot of things it's doing and so when it reaches the `insertion_sort()` it ruins the structure of the heap. Compared to an `unguarded_insertion_sort()` because it doesn't require to do a bounce checking with the `make_heap()` when going through the array since it will only come with the smallest value in the array and when you hit something smaller than you then you insert it in the order and that would complete that process and this is why it's faster than the `insertion_sort()`.
	
---
9. The speaker talks about incorporate your conditionals into your arithmetic.  What does this mean?  Provide an example of this from the video and explain how the conditional is avoided.

When the speaker talks about incorporating the conditional into the arithmetic he explains that there is a method that pushes an element that's not in the heap into the heap, called `push_heap()` which helps to optimize the code outside the outer loop. Alexandrescu then goes into explaining that when you integrate conditionals within the arithmetic, you want to make sure everything is a bool, no `if`. The example code he used shows `if (size < 3) { sort2(first[0], first[size == 2]);` which means that that it will swap the elements if size is less than 3 and not in the right order. This is the example that he showed on integrating conditionals in our arithmetic and why it's important. 

---
10.  The speaker talks about a bug in gnu's implementation.  Describe the circumstances of this bug.

When Alexandrescu talks about the `push_heap` explanation and shows how it's inefficient in gnu because of the structured loops and finite for which makes it slow. The bug in `push_heap()` is because it needs to be done multiple times and breaking too early. When it breaks right after the if condition it makes the remaining code do more work which is esentially wirrten poorly making the runtime slow because it will execute many times. Alexandrescu's solution is to always use inifinite loop. 

---
11.  The speaker shows several graphs about what happens as threshold increases using his new algorithm.  The metric of comparison is increased, the metric of moves are increased but time drops... What metric does the author think is missing?  Describe the missing metric he speaks about in the video.  What is the metric measuring?

The metric the author thinks is missing is when time continues to drop and the comparison increases is `Collect D(n), average distance between two subsequent array accesses`. This metric will give the idea of cache without actually having a cache specific metric because it will come back and show that it doesn't work because it gives different ends of the array. Alexandrescu then looked at the distance for quicksort and it's very large since it starts at the worst case for partitioning. He then looks at `D(n)` and looks at the graph but both metrics are still going down. His solution is to build a composite metric that encompasses all of the three implementation so you'd have a blended cost of your computation. The metric is for improving sorted algorithms.

---
12.  What does the speaker mean by fast code is left leaning?

When Alexandrescu talkings about "fast code is left leaning" he says if you want code to be fast it goes to the left of the page. When you think about the way we write code and you have the if statements, for loops, switch and other decision points it isn't fast because it's going in a loop which makes the code inefficient. A code that wants to be fast is left-leaning because it doesn't want to mix hot and cold operations which is explained more in the next question.

---
13.  What does the speaker mean by not mixing hot and cold code?

When Alexandrescu says hot and cold code he describes it as a "anti-pattern inefficiency" which is something you don't have to have. You would want hot code together and cold code together. An example of hot code is when you hit to break and return and get out of the code, however cold code isn't as important because it's more or less just "fix-up". 

## Reflection:

1. What did you/your team find most difficult to understand in the video?
I found it difficult to understand when he was speaking about the `unguarded_insertion_sort()` for the generic type. This was a part i have to rewatch multiple times to understand his explanation however I then understood what he was explaining with the code and how this affects the heap as written above. `unguarded_insertion_sort()` doesn't require a bounce check unlike the regular `insertion_sort()` because it affects the heap differently. For example, the first element in `insertion_sort()` is sorted and the second and third element can be out of order because that is still a valid heap. You can have 1, 7, 4 and that's valid as the root because it's less than 2nd and 3rd elements with it's children making it a valid heap. However this wouldn't matter in `unguarded_insertion_sort()` since it will work and be valid.

2. What is the most surprising thing you learned that you did not know before?
It was interesting to learn about the different intermediate structure other than the heap. From my understanding the main reason why constructing a heap improves the performance is that a heap is already partially sorted and so the linear searches end up ending shorter or more uniform, improving both locality and maybe branch prediction. I think in data structure we have learned about big-O in week 2 which can compare in terms of performance which would be simpler to contruct as well. However it would have similar effect for linear insertion sort.
It was interesting when Alexandrescu only tried to show the performances with heaps with 2 basic child heap which was simple to understand, however using something like fibonnaci heap might have different results. Although this reseasoning may go harder in the direction of strong invariants and can also lead to worse performances overall. I am keeping in mind that these heaps are also still under a size threshold that went up to 255 elements at most and the heap has to live in the array that's getting sorted.

3. Has the video given you ideas on how you can write better/faster code?  If yes, explain what you plan to change when writing code in the future.  If no, explain why not.
This video has given me alot of ideas on improving my code especailly comparing to the examples given. Things that Alexandrescu has shown in his video such as `insertion_sort()` and `unguarded_insertion_sort()` or showing how gnu would affect the chart if it were to be plotted. He goes through the importance levels of this and how to make this more efficient. As well as when he was speaking about bubble search sort and linear search sort since that is simething we work on in class it was interesting to see another speakers perspective on understanding the topic more with visual and examples to learn from.

## References:

- https://pvk.ca/Blog/2012/07/03/binary-search-star-eliminates-star-branch-mispredictions/

- https://machinelearningmastery.com/what-is-information-entropy/

- https://www.analyticsvidhya.com/blog/2020/11/entropy-a-key-concept-for-all-data-science-beginners/#:~:text=Information%20Entropy%20or%20Shannon's%20entropy,heterogeneity%20of%20the%20target%20variable.


