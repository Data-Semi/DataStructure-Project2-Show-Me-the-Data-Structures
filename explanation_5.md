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
In method `calc_hash` of the class `Block`, operation `json.dumps`, `json_text.encode`, `sha.update`, `sha.hexdigest` has space complexity O(n), other operations has O(1). Thus, this method's space complexity is O(n).  
In the class `BlockChain`, the method `toList` space complexity O(n) because it has a loop inside, other methods have space complexity O(1).  
In method `test_function`, other of mentioned operations above have O(1). Thus, this method's space complexity is O(n).  
In the method `main`, we do not have any loop operation and other of mentioned operations above have O(1). Therefore, this program has space complexity O(n).
