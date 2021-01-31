## Program structure
### Methods
Method `is_user_in_group()` is a recursive function.  
If there is a subgroup inside a group, the method `is_user_in_group()` will call itself recursively.

The method `print_group_structure()` is helper method. It prints out full paths of every folder and file in the inputted group.  

### Tests
Tests include below:   
Test case 1: The user is inside the group  
Test case2: The user is not inside the group  
Test case3: No user to find  
Test case4: empty group  
Test case5: Before and after add a user to a group  

## Time complextity
All operation take O(1) and a for-loop inside `is_user_in_group()` enumelates subgroups in inputed group, the time complexity is O(n).  
Therefore, The total time complexity is O(n).

## Space complexity  
All methods inside class `Group` have space complexity O(1).  
In method `is_user_in_group`, the recursion operation has space complexity O(n), other operations have O(1). Thus, this method's space complexity is O(n).  
In method `print_group_structure`, the recursion operation has space complexity O(n), other operations have O(1). Thus, this method's space complexity is O(n).  
In method `test_function`, other of mentioned operations above have O(1). Thus, this method's space complexity is O(n).  
In the method `main`, we do not have any loop operation and other of mentioned operations above have O(1). Therefore, this program has space complexity O(n).