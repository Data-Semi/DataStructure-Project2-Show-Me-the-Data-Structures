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
        if self.capacity == 0:
            return -1
        else:
            if (self.cashe.get(key) == None) and (len(self.cashe) == self.capacity):
                first_key = next(iter(self.cashe))
                del self.cashe[first_key]  # delete the first key , it is the least used item
            self.cashe[key] = value
            return None

def test_function(our_cache,func_return,expected_result,expected_cashe):
    if (func_return == expected_result) and (our_cache.cashe == expected_cashe):
        print("pass")
        print("The function returned: ", func_return)
        print("The cashe is: ", our_cache.cashe)
    else:
        print("fail")
        print("The function returned: ", func_return)
        print("The cashe is: ", our_cache.cashe)

def main():
    our_cache = LRU_Cache(5)
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

    #Test case 5, edge case: handle cashe capacity is 0.
    our_cache = LRU_Cache(0)
    test_function(our_cache, our_cache.get(6), -1 ,{}) 
    test_function(our_cache, our_cache.set(6, 100), -1,{})  #can not set anything 

if __name__ == "__main__":
    main()

