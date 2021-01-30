## Program structure
### Methods
This program Assume that the input sets A and B only includes numbers which can compared by `>, <`. 

## Time Coplexity
For save searching time, I choose to use ordered linked list. The method `addNode_acceding_order()` has one loop, therefore, the Big O is O(n).  
The ordered linked list allowes me to stop search before reach to the end of linked list, but it didn't change the time complexity.  
Both of the method `union()` and `intersection()` has time compexity O(n^2).  
Therefore, This program has time complexity O(n^2 + n).  