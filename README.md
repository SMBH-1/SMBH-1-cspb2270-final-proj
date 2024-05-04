# Searching Using Skip Lists

### CSPB 2270 - Data Structures & Algorithms - Final Project - Sid Reddy
______________________

#### *Project Goal:* 
Create and implement a skip list data structure and identify the benefits and drawbacks of using skip lists in 
performing search operations.

#### *Skip Lists - An Introduction*
Skip lists are probabilistic data structures (one that uses randomness or probabilistic methods) to maintain a sorted 
list and have logarithmic time -- O(log(n)) -- complexity for search, insertion, and deletion. 

A skip list comprises multiple linked lists arranged in layers, one on top of another. Each successive list in the 
next layer contains fewer elements than previous layers by skipping over specific nodes. Thus, a skip list's bottom-most 
the layer would contain all possible nodes (e.g., 13 nodes), and the next layer might have 10 nodes. The next layer 
could have eight nodes, etc. These layers above the bottom one have nodes with pointers to other nodes that skip several 
in-between nodes in the original bottom linked list. These upper layers are like 'express lanes,' allowing for faster 
traversal through the skip list.

Where a skip list applies probabilistic methods and randomness is in the number of layers of linked lists, it will have
and the number of nodes that are skipped in each successive layer.

For search, insertion, and deletion operations, the algorithms start at the top-most layer (with the fewest nodes of the
complete list) and move down the layers, searching for the correct node location. If the target value is larger than the
current node, the algorithm moves down a layer and traverses to the next node in this new layer's linked list. This
process continues until the target is found (for search or deletion), or if not found, it returns that the value doesn't 
exist. For insertion, the target value is inserted between the two nodes where the value would be 


Skip lists support full text and fuzzy text searches and are often more memory-efficient than other balanced tree 
structures like AVL trees or Red-Black trees. The probabilistic nature of skip lists allows efficient approximate 
searching. 


#### *Project Implementation*
I attempted to implement this project by creating a skip list data structure featuring a skip list class with
search, insertion, and deletion functions. To narrow the scope of my project, I chose to compare it to the AVL tree to
test and see how the two would compare by performance. For the skip list, I had to settle on a maximum level count 
(how many layers that skip list could have and the probability factor of whether a node would exist on additional 
layers). I then created performance metrics to measure the insertion, search, and deletion speed for skip lists
and AVL trees. I went back and found a way to measure memory usage to see which data structure was more
memory efficient (based on my research, skip lists were mentioned as being more memory efficient).

#### *Results*

The project produced some surprising results. With my initial implementation, the program generated a list of 100
strings, each 5 ASCII characters long. Then, the program used a randomly selected string from that list to search, insert,
and delete operations for both the skip and AVL trees. The program recorded the time to run these operations and printed
those times to the console. When I ran the program, I was surprised that the AVL tree was faster in all three operations. I realized
I forgot to sort my list of words into order. Even with this adjustment, AVL tree implementation was significantly
quicker. I attempted several modifications: 
* adjusting the max levels and probability factor of the skip list
implementation
* increasing the number of strings from 100 to 1000 and 10000 as well as the length of the strings from 5
characters to 9 and 11
* modifying the AVL tree to make it highly imbalanced

All my attempts still resulted in AVL tree operations being approximately ten times faster. See chart (the smaller number
= faster time):
___________
- Insertion time (SkipList): 0.00026583403814584017
- Insertion time (AVLTree): 4.912505391985178e-05
___________
- Search time (SkipList): 0.0018605419900268316
- Search time (AVLTree): 0.00012383400462567806
___________
- Deletion time (SkipList): 0.0024173749843612313
- Deletion time (AVLTree): 0.00012429198250174522
___________

I was trying to determine exactly why these specific implementations generated the results. Whatever I attempted to 
Modifications or changes didn't have much effect (Skip Lists continued to be slower in all operations). 

I went back to researching why this might be. The significant difference was that
skip lists' average case runtime was in O(log(n)), as were AVL trees. Skip lists proved more advantageous when you have
a skewed tree that could not self-balance. Unlike AVL trees, run time complexity was the same for
average and worst cases for insertion, deletion, and search. Based on my research,
AVL trees that require many rebalancing operations could theoretically be more inefficient than skip lists.
The other advantages listed included more straightforward implementation, which I experienced firsthand, more modification accessibility, and
simpler memory management. 

To expand on this project, I would re-attempt with a variety of inputs (not just a list of ASCII character strings) as
well as other data structures.