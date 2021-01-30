#!/usr/bin/env python
# coding: utf-8

# ## Blockchain
# ### problem description  
# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.  
# 
# Use your knowledge of linked lists and hashing to create a blockchain implementation.  
# We can break the blockchain down into three main parts.  
# 
# First is the information hash:   
# import hashlib  
# 
# def calc_hash(self):  
#       sha = hashlib.sha256()  
# 
#       hash_str = "We are going to encode this string of data!".encode('utf-8')
# 
#       sha.update(hash_str)
# 
#       return sha.hexdigest()  
# We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.  
# 
# The next main component is the block on the blockchain:  
# 
# class Block:  
# 
#     def __init__(self, timestamp, data, previous_hash):  
#       self.timestamp = timestamp
#       self.data = data
#       self.previous_hash = previous_hash
#       self.hash = self.calc_hash()  
#       
# Above is an example of attributes you could find in a Block class.    
# 
# Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!  
# 
# 

# ### Analysis
# The block chain is a linked list, and every node is an object of a Block class.
# The hash value inside a block node includes Greenwich Mean Time timestamp, data and the hash value of previous block node.
# 

# In[1]:


import hashlib
import datetime
import json

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp  # Greenwich Mean Time
        self.data = data
        self.previous_hash = previous_hash
        self.now_hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        
    # join the block data to prepare encoding
        joined_data = {
            'timestamp'        : str(self.timestamp),\
            'data'             : self.data,\
            'previous_hash'    : self.previous_hash
        }
        json_text = json.dumps(joined_data, sort_keys=True)
        hash_str = json_text.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return str(self.timestamp) + str(" | ") +        str(self.data) + str(" | ") + str(self.previous_hash) +        str(" | ") + str(self.now_hash)

class BlockChain(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def appendBlock(self, data):
        if data is None or data =="":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.now_hash)
            self.tail = self.tail.next
        return
    
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out


# In[2]:


def main():
    # Test Case 1 normal uses
    bl = BlockChain()
    data1 = "Data: First Blockchain block"
    data2 = "Data: Second Blockchain block"
    data3 = "Data: Third Blockchain block"
    bl.appendBlock(data1)
    bl.appendBlock(data2)
    bl.appendBlock(data3)
    print("|time | data | previous hash | hash|")
    for lists in bl.toList(): # Print block chain
         print(lists)
            
    # Test Case 2 no data has been passed
    bl1 = BlockChain()
    bl1.appendBlock("")
    bl1.appendBlock("")
    print(bl1.toList())  # empty block chain
    
    #Test Case 3 no data has been passed
    bl2 = BlockChain()
    bl2.appendBlock(None)
    bl2.appendBlock(None)
    print(bl2.toList())  # empty block chain
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




