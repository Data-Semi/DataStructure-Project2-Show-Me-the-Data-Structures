#!/usr/bin/env python
# coding: utf-8

# ## Least Recently Used Cache 
# ### problem description  
# We have briefly discussed caching as part of a practice problem while studying hash maps.
# 
# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
# 
# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.
# 
# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.
# 
# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.
# 
# Your job is to use an appropriate data structure(s) to implement the cache.
# 
# In case of a cache hit, your get() operation should return the appropriate value.  
# In case of a cache miss, your get() should return -1.  
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.  
# All operations must take O(1) time.
# 
# For the current problem, you can consider the size of cache = 5.
# 
# Here is some boiler plate code and some example test cases to get you started on this problem:

# ### Analysis
# I chose dictionary data type to treat the input (key, value) set to a queue data structure.
# Every time when the program access methods get(key) or set(key, value), the (key,value) will move to the tail of the queue.
# This makes least used item is always in the first position of the queue.
# If a key is new for the cache and the cache is at capacity, the method set(key, value) will remove the item in the first position of the queue.
# All operations takes O(1) time. 

# In[5]:


#I would like to use queue for the cache

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cashe = {}
        self.capacity = capacity
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        # I decide to use get() method instead of self.cashe.pop(key,None) for simplicity.
        value = self.cashe.get(key)  # if can not found the key, the value will be set to -1
        if value == None:  
            value = -1
        else:
            # found the key,delete from the original position and append it to the last positon of the dictionary
            self.cashe.pop(key)
            self.cashe[key] = value
        return value

    def set(self, key, value):
        # If the key is new and the cache is at capacity, remove the least used item which is in the first position of the dictionary
        # if I use self.get() instead of self.cashe.get(key), I can not distinguish the rusult is value==-1 or "key not found"
        if (self.cashe.get(key) == None) and (len(self.cashe) == self.capacity):
            first_key = next(iter(self.cashe))
            del self.cashe[first_key]  # delete the first key , it is the least used item
                
        self.cashe[key] = value


# In[6]:


def test_function(our_cache,func_return,expected_result,expected_cashe):
    if (func_return == expected_result) and (our_cache.cashe == expected_cashe):
        print("pass")
        print("The function returned: ", func_return)
        print("The cashe is: ", our_cache.cashe)
    else:
        print("fail")
        print("The function returned: ", func_return)
        print("The cashe is: ", our_cache.cashe)


# In[7]:


our_cache = LRU_Cache(5)


# In[8]:


#Test case 1: Normal set and get.
test_function(our_cache, our_cache.set(1, 1), None,{1: 1})  #None
test_function(our_cache, our_cache.set(2, 2), None,{1: 1, 2: 2})  #None
test_function(our_cache, our_cache.set(3, 3), None,{1: 1, 2: 2, 3: 3})  #None
test_function(our_cache, our_cache.set(4, 4), None,{1: 1, 2: 2, 3: 3, 4: 4})  #None
test_function(our_cache, our_cache.get(1), 1, {2: 2, 3: 3, 4: 4, 1: 1})  #1
test_function(our_cache, our_cache.get(2), 2, {3: 3, 4: 4, 1: 1, 2: 2})  #2

#Test case 2, edge case: The key is not exists
test_function(our_cache, our_cache.get(9), -1, {3: 3, 4: 4, 1: 1, 2: 2})  #-1

#Test case 3, edge case: Cashe reached capacity,and new key is given.
test_function(our_cache, our_cache.set(5, 5), None,{3: 3, 4: 4, 1: 1, 2: 2, 5: 5})  #None
test_function(our_cache, our_cache.set(6, 6), None,{4: 4, 1: 1, 2: 2, 5: 5, 6: 6})  #None #The leaset used itme (3,3) has been deleted
test_function(our_cache, our_cache.get(3), -1, {4: 4, 1: 1, 2: 2, 5: 5, 6: 6} )  #-1

#Test case 4, edge case: handle value == -1 to set(key, value)
test_function(our_cache, our_cache.set(6, -1), None,{4: 4, 1: 1, 2: 2, 5: 5, 6: -1})  #None
test_function(our_cache, our_cache.get(6), -1 ,{4: 4,1: 1, 2: 2, 5: 5,6: -1})  #-1 # Value  -1  successfully has been set
test_function(our_cache, our_cache.set(6, 100), None,{4: 4, 1: 1, 2: 2, 5: 5, 6: 100})  #None # Can update the value after -1 setting.


# In[ ]:




