## Program structure
### Methods
This program Assume that the input sets A and B only includes numbers that can be compared by `>, <`.  

### Tests
Tests include below:   
Test case 1: Normal use   
Test case 2, edge case: No intersection  
Test case 3, edge case: Input an empty list  

## Time Coplexity
To save searching time, I choose to use an ordered linked list. The method `addNode_acceding_order()` has one loop, therefore, the Big O is O(n).  
The ordered linked list allowed the program to stop the search before reach to the end of the linked list, but it didn't change the time complexity.  
Both of the method `union()` and `intersection()` has time compexity O(n^2).  
Therefore, This program has time complexity O(n^2 + n).  

## Space complexity  
The class `Node`,`LinkedList` have space complexity O(1).  

`to_list(self)` in the class `LinkedList`: It is inserting elements to a list and the size of the list depends on the input size. Thus, this method's space complexity is O(n).  

`__str__(self)` in the class `LinkedList`: It is saving elements to a string and the string size depends on the input size. Thus, this method's space complexity is O(n).

Other methods in the class `LinkedList` are not saving data which depends on input. Thus, any of these methods' Space Complexity is O(n).

`union(llist_1, llist_2)`: It is inserting elements to `union_list`, but it is only access the inputted lists and not saving any extra data. Therefore, this method's space complexity is O(1).  

`intersection(llist_1, llist_2)`: It is inserting elements to `intersection_list`, but it is only access the inputted lists and not saving any extra data. Therefore, this method's space complexity is O(1). 

