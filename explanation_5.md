## Program structure
### Methods
I implemented the class `BlockChain(object)` with a linked list. Every node is an object of the `Block` class.  
The hash value inside a node `now_hash` is calculated from `timestamp` the Greenwich Mean Time timestamp of the node has been created, `data` the data of current node, and `previous_hash` the hash value of the previous node.  

### Tests
Tests include below:   
Test Case 1: Normal uses  
Test Case 2: Input is "", no data has been passed  
Test Case 3: Input is None, No data has been passed  

## Time Coplexity
Every operation in the program has time complexity O(1).  
Therefore, the program's time complexity is O(1).

## Space complexity  

`Block`, `BlockChain`: As a class,it is internally having fixed number of variables constant in nature, hence the Space Complexity is O(1).  

The method `toList(self)` in `BlockChain`: It is inserting elements to a list and the size of the list depends on the inputted tree size. The space complexity is again dependent on the amount of blocks we want to add and it will be variable. If n is the maximum lenght of the chain it will be O(n). Thus, this method's space complexity is O(n).  
