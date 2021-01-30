## Program structure
### Methods
I implemented the class `BlockChain(object)` with a linked list. Every node is an object of the `Block` class.  
The hash value inside a node `now_hash` is calculated from `timestamp` the Greenwich Mean Time timestamp of the node has been created, `data` the data of current node and `previous_hash` the hash value of previous node.  

### Tests
Tests includes below:   
Test Case 1: Normal uses  
Test Case 2: Input is "", no data has been passed  
Test Case 3: Input is None, No data has been passed  

## Time Coplexity
Every operation in the program has time complexity O(1).  
Therefore, the program's time complexity is O(1).
