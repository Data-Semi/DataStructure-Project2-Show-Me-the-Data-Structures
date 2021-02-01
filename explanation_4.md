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
`Group`: As a class, it saves all the elements we insert in lists `groups`, `users`. Hence, it has a Space Complexity of O(2n).

`is_user_in_group`: The function only access the list and return a single value regardless of the size of the list, hence it is constant in nature and hence it is O(1).