## Program structure
### Methods  
I chose q dictionary type queue data structure to store the input (key, value) dataset.  
Every time when these methods `get(key)` or `set(key, value)` have been called, the (key, value) will move to the tail of the queue.  

This makes the least used item is always in the first position of the queue.  

If a key is new for the cache and the cache is at capacity, the method `set(key, value)` will remove the item in the first position of the queue.  

### Tests
Tests include below:   
Test case 1: Normal set and get.  
Test case 2, edge case: The key is not exists  
Test case 3, edge case: Cashe reached capacity, and new key is given.  
Test case 4, edge case: handle value == -1 to set(key, value)  
Test case 5, edge case: handle cache capacity is 0.  

## Time complexity  
All operations takes O(1) time.   
Therefor, The total time complexity is O(1).

## Space complextity  
In method `get(self, key)`, `self.cashe` has space complexity O(n), `key` has O(1), `value` has O(1). Thus, this method's space complexity is O(n).  
in method `set(self, key, value)`, the space complexity of `len(self.cashe)` is O(n), other operations is O(1). Thus, this method's space complexity is O(n).  
In method `test_function`, other of mentioned operations above have O(1). Thus, this method's space complexity is O(n).  
In the method `main`, we do not have any loop operation and other of mentioned operations above have O(1). Therefore, this program has space complexity O(n). 

