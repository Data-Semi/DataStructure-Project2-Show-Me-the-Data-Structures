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

`get(self, key)`: the function only access the list and return a single value regardless of the size of the cache, hence it is constant in nature and hence it is O(1).  

`set(self, key, value)`: the function set is also, internally having fixed number of variables, and the sizes of the variables are also independent of the size of the cache, hence it is also constant in nature and hence the Space Complexity for the function is O(1).  

`LRU_Cache`: As a class, it saves all the elements we insert in a dictionary and hence, it has a Space Complexity of O(n).


