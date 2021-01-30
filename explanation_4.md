## Program structure
### Methods
Method `is_user_in_group()` is a recursive function.  
If there is a subgroup inside a group, the method `is_user_in_group()` will call itself recursively.

The method `print_group_structure()` is helper method. It prints out full pathes of every folder and file in the inputed group.  

### Tests
Tests includes as below:   
Test case 1: The user is inside the group  
Test case2: The user is not inside the group  
Test case3: No user to find  
Test case4: empty group  
Test case5: Befor and after add a user to a group  

## Time complextity
All operation takes O(1) and a for-loop inside `is_user_in_group()` enumelates subgroups in inputed group, the time complexity is O(n).  
Therefor, The total time complexity is O(n).
 