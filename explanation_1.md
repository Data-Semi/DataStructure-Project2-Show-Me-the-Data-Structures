## Program structure
### Methods  
I chose dictionary type queue data structure to store the input (key, value) dataset.  
Every time when these methods `get(key)` or `set(key, value)` have been called, the (key,value) will move to the tail of the queue.  

This makes the least used item is always in the first position of the queue.  

If a key is new for the cache and the cache is at capacity, the method `set(key, value)` will remove the item in the first position of the queue.  

### Tests
Tests includes below:   
Test case 1: Normal set and get.  
Test case 2, edge case: The key is not exists  
Test case 3, edge case: Cashe reached capacity,and new key is given.  
Test case 4, edge case: handle value == -1 to set(key, value)  

## Time complextity  
All operations takes O(1) time.   
Therefor, The total time complexity is O(1).