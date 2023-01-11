# Lab 7


* Priya Khatri
* Noel Ibruli
* Anusmita Chanda

## Part A: BST Insert

As a group review bst insertion algorithm.

* Take one photo of the original row of sticky notes

![313202259_893556408319886_3885038918737086349_n](https://user-images.githubusercontent.com/25591984/205468317-c5d1808b-95c5-4654-a01a-3e276d64c46e.jpg)


* When completed, take one photo of the final tree

![317362356_526805322666433_6855844819351639394_n](https://user-images.githubusercontent.com/25591984/205468916-567d64b5-d11a-4f76-802c-a3586959e854.jpg)

Answer this question
* What is the height of your final tree?

The height of the tree is 6. This is because we would count the leaf nodes starting from 1 and continue with each level going upwards. Therefore, the total number of nodes from root to furthest leaf is what would be counted as the height.


## PART B: BST Deletion

* Find a node in your tree with 2 children and remove that node.
	* Take a picture of tree

![318483772_1115979945749321_6732299892222486661_n_](https://user-images.githubusercontent.com/25591984/205469167-4790e9f3-2ebc-4f75-ae1a-59ee93309a64.jpg)


* find another node with 2 children and remove that node
	* Take picture of tree

![318351012_3425034901059516_7407691762039872826_n_](https://user-images.githubusercontent.com/25591984/205469188-f4d10d6e-d2bc-4cd7-b480-358f4cb91d82.jpg)


* remove the root node of the tree
	* take picture of tree

![root](https://user-images.githubusercontent.com/25591984/205508517-3808c903-4899-487d-8bab-30eff5c1026b.jpg)


Answer this question:

* Anytime you remove a node with 2 children, you need to find a node to take over for node being removed.  Explain how you found your replacement.

When a node with 2 children needed to be removed from the tree it would take the left side of the node and move it forward. When removing the number 19 it was removed with 12 because 12 it bigger number than 9, therefore, it would go as the parent node for that subtree section. Afterwards, while removing 91, the number 82 would go upwards to take it's place because it is on the left side of the tree and that is the rule to take the left side of the node. Finally, removing the root of the tree was again replaced by the left side of the tree and therefore, leaving the root with the number 2. The idea from my understanding is we are going to look at the left side until there is no more left since it is the smallest value typically and then take the inorder successor to replace the node we are removing which is what we have done in our tree shown above.

## Part C AVL
* Take one photo of the original row of sticky notes

![avlrow](https://user-images.githubusercontent.com/25591984/205509178-5d19bd28-281c-4362-b55f-cf2ad6d81225.jpg)

* When completed, take one photo of the final tree

![avltree](https://user-images.githubusercontent.com/25591984/205509190-c1044be5-ed30-4c03-a315-9e652af685aa.jpg)

Answer these questions. 
* How many times you had to do a single rotation? 
 
There were 4 single rotations done during this AVL tree exercise. The first single rotation that occured in the tree was after adding 12 then 53, since they all fell on the right side, it did a single rotation to the left to balance the numbers. The second single rotation right occured on the left side of the subtree when adding the value 2 which went down and 5 came up to balance the tree. Afterwards, adding the value 100 to the bottom right node, there was a single rotation left, making the root value 55. Finally, another single rotation when adding the last value 22 to the bottom of the tree, then leading 21 to go upwards. From my understanding a single rotation occurs when the tree is not height balanced so it would need to be rotated to balance the numbers in the tree.

* How many times you had to do a double rotation? 

There were 3 double rotations that occured during this AVL tree exercise. The first double rotation occured after adding the value 82 to the tree, a double rotation to the right would occur which then brought 55 down and 82 up. The second double rotation was after adding the number 73 there was a double rotation left because it was then inbalanced on the right and left side so it would bring up 73 to be the child of 82 and the sibling of 91. Finally, when adding the number 38 to the tree it would bring it higher in the tree and 19 down in the double rotation.

* How tall is your final tree? 
 
My tree has 5 levels. Level 1 (left to right) which has all the child nodes: 2, 9, 19, 22, 44, 73, 100. Level 2 which is the parents of those children: 5, 21, 53, 91. Level 3: 38, 82. Level 4: 12. Finally level 5 as the root value: 55. 

## Part D Red-black trees (optional)

* Take one photo of the original row of sticky notes

![317431301_515265457301520_1037166083521322370_n](https://user-images.githubusercontent.com/25591984/205474681-2e4e5bc4-e270-4183-a51b-e03733d62f26.jpg)

* When completed, take one photo of the final tree

![randbtree](https://user-images.githubusercontent.com/25591984/205509839-417e606d-0f37-411a-8950-86268c6034e6.jpg)


* how many times did you perform a colour swap, zig-zig and zig-zag rotation?

There were 9 colour swaps. A new node will always start off as black and when ever a new child node is added it will be red. Since there can't be 2 red nodes back to back in a tree the colour will swap everytime a child node is added under a parent node, from my understanding. In our Red-black tree with the first three numbers 38, 5, 73 where 38 is the root and 5 is the left node, 73 is the right node. The number 5 and 73 would be red since they are both child nodes right now. This will swaped colours for the first time as soon as I added 55 to the tree. The number 73 and 5 stopped being red and it went to 55 since 55 is the new child node in the tree and 73 becomes the parent of that. The second time there was a colour swap was adding the number 100 which then makes 55 and 91 black again and swaps 73 and 100 to being red since 73 is the child node and red nodes cannot have red parents. This pattern goes on throughout the tree 7 more times. 

There was 1 zig-zig rotation. This happened when adding the final number 44 it was leaning left of the tree under 55 so it was then zig-zig rotation to bring 53 upwards and 53 will be black and the child would be 44 and 55 as red. 

There was 1 zig-zag rotation. This occured when adding the number 12 which started as a child node to the left of 21, then was brought up and swaped around to bringing it to the bottom left of 38. This happens when there is a left node and a right node causing a bend, it would be considered an unbalanced tree therefore, a zig-zag single rotation would occur twice causing a double rotation. 

The patterns that I noticed while doing this exercise is if there are nodes straight in one direction the middle number would go upwards to balance the nodes in the tree in zig-zag formation, also known as a single rotation. A double zig-zag rotation would occur if there is a bend as mentioned above.


## Part E 2-3 trees

* Take one photo of the original row of sticky notes

![2to3tree](https://user-images.githubusercontent.com/25591984/205512334-cbd38e03-d502-48d8-a7cb-ffdb7de9657c.jpg)

* When completed, take one photo of the final tree

![23final](https://user-images.githubusercontent.com/25591984/205512344-c1478266-8b9e-4b16-885e-bf8799f65fe5.jpg)

* How many times did you split?

This 2-3 tree split 7 times. The first split happens after the third number, 21 was added so it will then split into 2 individual leafs showing as 21 left child node of 44 root and 73 right child leaf. Another split happens after adding the number 2 which would go in the same circle as 2 and 21 but once 2 is added then 9 will go up with 44. This happens because there cannot be more than 2 numbers in a leaf so you would take the medium number to the root of the child leafs. The third  time a split happened was with 12, 21, 22 which split with 21 going up to the original root making it 9, 21 and 44. This then spliting the root node again so 21 is only at the root of the tree since it is considered the medium in that leaf. Afterwards, the diagram follows the similar pattern with the other values 7 times throughout adding a number to the correct side of the tree based on if it's higher or lower than the parent then being split afterwards.

## Part F Dijkstra's Algorithm


![Graph](https://user-images.githubusercontent.com/1699186/203682880-1f8d6068-3668-4b2c-9abe-40cb79294177.png)


Use Dijkstra's algorithm to find the shortest distance from vertex A to every other vertex.  Show your work by creating the table below:

| Vertex | Distance to A | Previous Vertex | Known|
|---|---|---|---|
| A  |  0 | -  |  False |
| B  |  5 | A  |  True  |
| C  |  9 | B  |  True  |
| D  |  11 | C  |  True  |
| E  |  10 | F  |  True  |
| F  |  3 | A  |  True  |
| G  |  13 | D  |  True  |


Result summary: Fill in the final result in this table.  For path list all nodes for example, if you are going from A to B to C to D, then path is A-B-C-D


| Vertex | Path | Distance to A|
|---|---|---|
| A  |  - | 0 |
| B  | A-B | 5 |
| C  | A-B-C | 9 |
| D  | A-B-C-D | 11 |
| E  | A-F-E | 10 |
| F  | A-F | 3 |
| g  | A-B-D-G | 13 |

## Part G: Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.

This lab was very interesting for me because I enjoyed learning the different patterns for the different tree types and understanding the similarities and differences between each. One thing I learned that I wasn't familiar with was how to do Dijkstra's algorithm. Originally it looks very complicated and after researching a bit about how this algorithm works I found that no graph will be similar so it's not about how the outlook is in the way we look at a tree and can understand the height values or a balanced tree. This is based on the shortest path to the goal value, which in this case was shortest path to A. Originally they all start as `False` in the first diagram because they are not known and then going through each one to see how they are known. Going through the process with my group was helpful to understand how this pattern works.

Another concept I learned in this lab was when completing the AVL tree. I understood the pattern of the smaller number going on the right node and larger going to the left of the parent node, however I originally didn't understand when a zig-zag rotation would occur and which number goes up or how would I know? This is something I had to practice a few times to understand that the idea of this tree is to make it a height balanced tree not a perfectly balanced tree. So in the exercise if there were more subtrees on the left side subtree then there would be a rotation done to make sure it is balanced and this is done throughout adding numbers to the tree one by one to check if a rotation needs to be done. Similarily to the zig-zag rotation done in an AVL tree was done in a Red-Black tree. Except in this tree it was also watching out for a colour swap. I learned that there can't be 2 red nodes back to back, also known as parent and child. One thing I didn't understand was when it would switch and can it switch thorugh the tree once or as many times needed? I think if it were a bigger tree it would change many times through adding more numbers in them but once I noticed that any new child node that is added on either side of the subtree then the colour will change to black if the child node is red. As well as when a single or double rotation is necessary. A simple rule that I learned to understand quicker for a rotation was if there was an order of grandparent to parent to child in a single straight line then do a zig-zig rotation where the median number going up as a parent. If there was an order of the same but a bend such as a left right left then there would be a zig-zag rotation. The zig-zig and zig-zag rotation was something I had to practise alot at home to understand the reason why this happens when it is necessary. These are a few things I learned while doing this lab.

