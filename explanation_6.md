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
All methods inside class `Node` have space complexity O(1).  
The  method `__str__`, `to_list`, `append`, `append_node`, `addNode_acceding_order`, `size` of the class `LinkedList`, a loop has space complexity O(n), other operations has O(1). Thus, this method's space complexity is O(n).  

In method `union`, there are 2 loops nested. The nested loops have space complexity O(n^2), and method `append_node` is inside the deepest loop. Because the method `append_node` has space complexity O(n), this method `union` has space complexity(n^3). 

In method `intersection`, there are 2 loops nested. The nested loops have space complexity O(n^2), and method `append` is inside the deepest loop. Because the method `append` has space complexity O(n), this method `intersection` has space complexity(n^3).  

In method `test_function`, other of method `to_list` has O(1). Because method `to_list` has space complexity O(n), this method's space complexity is O(n).  

In the method `main`, we do not have any loop operation. The code line which uses method `union` as the input of the `test_function` has O(n^4) because of method `union` has O(n^3) and method `test_function` has O(n). With the same logic, the code line which uses method `intersection` as the input of the `test_function` has O(n^4) because of method `intersection` has O(n^3) and method `test_function` has O(n). Other operations have O(1).  

Therefore, this program has space complexity O(n^4).