# Lab 5 Reflection and Observations

* Priya Khatri
* Anusmita Chanda
* Kuljit Kaur

## Heap Insertion

### Picture of heap created with 10 values

![20221103_150136](https://user-images.githubusercontent.com/25591984/199869337-335c5d2e-f979-494a-8630-9d5ca724c8f4.jpg)
![20221103_150221](https://user-images.githubusercontent.com/25591984/201254055-f48f53c5-16da-46d5-bc8f-6e9de964632c.jpg)
![20221103_150226](https://user-images.githubusercontent.com/25591984/199870941-13b1c2ef-7560-4287-b1bb-4f9471d830e5.jpg)
![20221103_150233](https://user-images.githubusercontent.com/25591984/199870958-76bff135-bea7-4ade-975a-d8a0ee7d36fe.jpg)
![20221103_150243](https://user-images.githubusercontent.com/25591984/199871007-87a781c5-8114-4e2d-936e-818de96f8bef.jpg)
![20221103_150301](https://user-images.githubusercontent.com/25591984/199871163-d84f8b7e-3aad-480a-b15b-57dd54f8a792.jpg)
![20221103_150311](https://user-images.githubusercontent.com/25591984/199871303-1e96a824-baf9-4a27-ae9b-a0df543007c9.jpg)
![20221103_150320](https://user-images.githubusercontent.com/25591984/199871340-7fb39013-3698-443d-b6b3-de6226a63dac.jpg)
![20221103_150327](https://user-images.githubusercontent.com/25591984/199871530-fc1763cd-efd1-45ac-8e2e-b5c8be655b13.jpg)
![20221103_150334](https://user-images.githubusercontent.com/25591984/199871561-9b9e660d-62c4-44c4-bae0-2385ef4deab2.jpg)
![20221103_150346](https://user-images.githubusercontent.com/25591984/199871563-ad385b66-3396-4937-aeb1-f3fddd3c4c58.jpg)
![20221110_230536](https://user-images.githubusercontent.com/25591984/201261232-ee5d91f2-eb82-4e3a-ba7d-11a2e6842e53.jpg)
![20221110_230547](https://user-images.githubusercontent.com/25591984/201261235-139bc4ea-e27a-433b-9f35-9608669a3275.jpg)

### Pictures of adding 11th value to heap
![20221110_231017](https://user-images.githubusercontent.com/25591984/201261748-cee53356-00c3-4439-8236-673e1099c8ca.jpg)
![20221110_231027](https://user-images.githubusercontent.com/25591984/201261751-4d09254b-bb16-4c71-b862-053aa2f0a2f3.jpg)
![20221110_231035](https://user-images.githubusercontent.com/25591984/201261754-bf627c83-0bbd-42db-b85a-70545a5bfcd9.jpg)
![20221110_231048](https://user-images.githubusercontent.com/25591984/201261756-ab6eea9c-c342-4aa5-a8e7-94d3a41723b0.jpg)


## Heap Removal

### Picture after 1 value was removed from heap
![20221110_142611](https://user-images.githubusercontent.com/25591984/201263391-197d146c-df3d-4565-a2f4-7a0a8cc3f107.jpg)

### Picture after 2 value was removed from heap
![20221110_142647](https://user-images.githubusercontent.com/25591984/201263496-b77ba1a6-8a22-4226-b28a-cb98cc0e565d.jpg)

### Picture after 3 value was removed from heap
![20221110_142704](https://user-images.githubusercontent.com/25591984/201263563-6684b62a-c512-4915-9d6e-7c19c20914e8.jpg)

### Values removed (in order removed):
The values that were removed were 1, 2, and 8 in this order which gives the results as shown above. When 1 was removed it was added to the end of the tree and everything was then shifted upwards to have the higher value compared in the tree until we have reached to the top of the tree. We added the value 1 to the end of the tree as it technically has been removed but there won't be any empty spots in the array since we shifted everything forward. This was a similar process with removing 2 as well as the value 8. 
When the value 2 was removed from the heap, 8 followed by 10 and 19 then got shifted upwards in the tree; the array was affected accordingly to the tree. 
Finally when 8 was removed and added to the end of the array it brought the value 107 up to the top of the tree and front of the array and nothing else needed to be changed after that since 107 has a higher value than 10 and 13.

## Array representation of heap

### Picture of heap
![20221110_142757](https://user-images.githubusercontent.com/25591984/201268014-87ffca3f-54c5-4eb4-85b0-118e7499bf32.jpg)

### Array representation of heap
The array representationn of the heap is as follows: 10, 19, 13, 27, 107, 35, 17, 29, 8, 2, 1

## Creating a heap from array

Photograph of your array and heap
![20221110_145531](https://user-images.githubusercontent.com/25591984/201417275-ed2a1fe8-c45a-4ff1-abea-bb20e9b7e058.jpg)
![20221110_150431](https://user-images.githubusercontent.com/25591984/201417506-52c512d8-af8b-4161-ad2b-dde8b5277234.jpg)
![20221110_151736](https://user-images.githubusercontent.com/25591984/201417737-8db7b42a-37bb-4406-8d73-664a8ec0ad52.jpg)
![20221110_151803](https://user-images.githubusercontent.com/25591984/201417897-ed3a2579-97a5-41cb-9375-84dfa559688d.jpg)

* What number is the first non-leaf node starting from bottom? 
The first non leaf starting from the bottom is 35. On the right side of the tree, it has the value, 107 whhich has 2 leafs 19 and 17 so this wouldn't be considered an example of non-leaf node and cancels out our options. Since we are checking from the bottom first it then lead us to looking on the left side nodes with 13, which has 2 leafs, 10 and 1. The other option to look at is 29, this also had leafs of 8 and 2. This has lead us to go higher up in the tree which then makes us look at 35 since you look right left to right and 35 is the first non-leaf node.

* What index is that node at? The index 35 is at is the 9th index because index starts at 0 so we would count the first index as 0 to continue to when we reach 35 it would be the 9th index


### Photograph of heap created by Heapify
![20221110_152716](https://user-images.githubusercontent.com/25591984/201267816-b9cb7daf-3218-48ed-9d78-d0c79c22a37d.jpg)

## HeapSort

Initial questions (do first):
* How many values are in your array? There are 11 values stored in the array.
* What is index of last value in array? The index of the last value in the array is 10 (with the value 2).

After doing 1 removal operation
![20221110_153308](https://user-images.githubusercontent.com/25591984/201267817-a7ce8a70-7415-4845-9365-3d86081453e7.jpg)

* what was the first value removed? How does this number compare with others in heap (biggest? smallest?) 
The first value removed and added to the end of the array was 107. It is the biggest number and the highest priority number compared to others that are lower priority. This was then swapped with the value 35 to the top priority number. After the comparison we noticed 35 is a higher number than 29 and 27, therefore, it would remain at the top after the removal to be the highest priority number.

* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap? 
After doing the removal for the value 107 in the array it would be added to the end of the array. This leaves the tree with 10 values remaining. The bottom right index value is 2 since it is considered the last active number in the tree/array in the heap. 

After doing 2 removal operations:
* Perform another remove from the heap and adjust the array to match
![20221110_160342](https://user-images.githubusercontent.com/25591984/201267819-a2b8929b-ee68-45c2-bedf-7192dd4b4880.jpg)

* What was the second value removed and how does it compare with others still in heap? 
The second number removed was 35 from the heap. We did similar to above in swapping it to the bottom value making 29 the highest priority and shifting it to the front of the array which then brings 35 to the end of the array. 29 was still compared from 27 however it's the value on the left which was higher and brought up to the top of the tree.
 
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?  
There are 9 values remaining in the heap portion of the array after the removal. The index of the bottom right value in the heap is 1, at index 8.

* Are there any open spots in the array that is not part of the heap and not holding anything useful? 
There are no open spots at the end. There may be temporarily open spots while doing the removal process since values are being replaced however there wouldn't be any at the end since every spot in the array is filled by a number with the removed values being placed at the end of the array.

After doing 3 removal operations:

* Perform another remove from the heap and adjust the array to match
![20221110_160806](https://user-images.githubusercontent.com/25591984/201267823-a5738ca9-08ff-4e32-a805-16736de38d78.jpg)

* What was the ~second~ third value removed and how does it compare with others still in heap? 
The third value that was removed from the heap was 29. This was a similar swap process but bringing the value 27 to the top of the tree and front of the array and 29 to the end of the array to fill in the temporary open spots since there won't be any permanent open spots in the array. Since 27 was brought upwards to the top because it's higher than 13, following that is 19 and nothing else needed to change.

* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
After doing the removal of the value 29 there are 8 values left in the array. The bottom right most value in heap is the value 2 because it is the last value in the tree that havn't been removed from the heap. The index is of the value 2 is at 7 in the array. 

* Are there any open spots in the array that is not part of the heap and not holding anything useful?
There are no open spots in the array in the heap since all the values are filled however the last 3 values are not useful since they have been removed and are holding a spot in the array. 


## Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
* Discuss what you learned about heaps and heap sort.
In this lab the topic that I learned was about heaps and heap sorts. This was interesting to understand with doing this hands on with sticky notes. Based on my understanding heap sorts is a comparison based technique which can be similar to the previous lab however this lab focused more on creating a heap, removing nodes, and the array representation which affects the binary tree. I also learned how values were never truley removed from the heap because they still hold space in the array. There will never be an empty space since we allocate 11 values (10 index) and each spot will always hold a value, even if they have no value to the heap. This can be similar to the selection based sort that we did in the previous lab as wwell because we compared the minimum elements and repeat this cycle until we have gone through the entire list of arrays. This was similar for lab 5 as well in getting to practise the comparison based technique

* What was the most surprising thing you learned about heaps?
The most surprising thing I learned about heaps was that it sounds more intimidating than it is. Before learning this I only had the knowledge of a heap and stack in C based coding languages. However learning this in a data structure point of view we see what happens in the back-end of the array as well as doing heap removals which wasn't something i've done before so it was interesting to learn about in this lab. This gave me a bigger understanding of how arrays work which can be confusing sometimes depending on the situation. 
Another thing that was surprising was working in a group and how at parts we would be stuck or have different ideas on different methods we can do. We would talk out the question and explain things to each other which gives us great perspective on the topic or task at hand. It would allow us to teach each other as well because we would explain why we believe the solution and sometimes confirm with professor to make sure we are on the right track.



