#!/usr/bin/env python
# coding: utf-8

# ## Overview - Data Compression
# ### problem description  
# In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.
# 
# A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.
# 
# ### A. Huffman Encoding  
# Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
# 
# #### Phase I - Build the Huffman Tree  
# A Huffman tree is built in a bottom-up approach.
# 
# First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.  
# (Unique) Character	Frequency  
# 
# A	7
# B	3
# C	7
# D	2
# E	6
# 
# Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.  
# 
# We would need our list to work as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. The following snapshot will help you visualize the example considered above:  
# 
# 
# Can you come up with other data structures to create a priority queue? How about using a min-heap instead of a list? You are free to choose from anyone.
# 
# Pop-out two nodes with the minimum frequency from the priority queue created in the above step.  
# Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.
# 
# Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a better choice due to the lower complexity of sorting the elements, every time there is an insertion.
# 
# Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.
# 
# 
# For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:
# 
# #### Phase II - Generate the Encoded Data  
# Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.  
# (Unique) Character	Frequency	Huffman Code
# 
# D	2	000
# B	3	001
# E	6	01
# A	7	10
# C	7	11
# 
# Points to Notice
# 
# Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code.  
# Notice that the binary code is shorter for the more frequent character, and vice-versa.  
# The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
# Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.  
# This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101
# 
# ### B. Huffman Decoding  
# Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:
# 
# Declare a blank decoded string  
# Pick a bit from the encoded data, traversing from left to right.  
# Start traversing the Huffman tree from the root.  
# If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.  
# If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.  
# Repeat steps #2 and #3 until the encoded data is completely traversed.  
# You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.
# 
# 

# ### Analysis
# After I complete the huffman encode function and decode function, I wrote a test function to see whether the input string is restored after go through the encode function and the decode function.
# 
# I chose priority queue data structure to reduce encoding method's time complexity. The priority queue has time complexity O(logn) instead of sorting a dictionary which has time complexity O(n).
# 
# We treat the encoded data as a binary data, so the size of the data is much smaller than the original size of data.  
# Note that the input string's storage is 19 x 8 =152 bits (38 bytes), but our encoded string only takes 70bits (18bytes).i.e.,about 54% of data compression.  
# 
# When we use the method sys.getsizeof() to calculate storage size, it will return a size that includes other information data in python. i.e. sys.getsizeof(a_great_sentence)) returns 69 bytes instead of 38 bytes. The sentense sys.getsizeof(int(encoded_data, base=2))) returns 36bytes instead of 18bytes. We can see the data is compressed after encoding.  
# 
# To make the program readable, we have used string class to store the above program's encoded string.    
# 

# In[4]:


import sys
import heapq
from heapq import heappop, heappush

# Creating tree nodes
class Node(object): 
    def __init__(self,char, freq, left=None, right=None):  # the value is a frequency of a charactor or the sum of the chilrens value 
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)
    
    def is_leaf(self):
        if (self.left is None) and (self.right is None):
            return True
        return False
    # Override the __lt__() function to make `Node` work with priority queue
    # such that the highest priority item has the lowest frequency
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        return '%s_%s_%s' % (self.left, self.right, self.char)

class Tree():
    def __init__(self, node):
        self.root = node
        self.left = node.left
        self.right = node.right
        
    def get_root(self):
        return self.root
    
    def is_leaf(self):
        if self.left is None and self.left is None:
            return True
        else:
            return False
      
    def __repr__(self):
        #print("the root value is:", self.root.value)
        return '%s' % (self.root)

def huffman_decoding_char(code_data, tree):
    # base condition, if the tree is a leaf
    if tree.is_leaf():
        return code_data, tree.char
    
    char = ""
    if code_data[0] is '0':
        remain_code_data, char = huffman_decoding_char(code_data[1:],tree.left)
        
    elif code_data[0] is '1':
        remain_code_data, char = huffman_decoding_char(code_data[1:],tree.right)
        
    return remain_code_data, char

#Make the answer string by joining every charactor.
def huffman_decoding(code_data, tree):
    string = ""
    if code_data == None and tree == None:  # the input string was ""
        return ""
    
    elif tree.is_leaf():  # the input only include 1 type of charactor
            string = (tree.get_root().char) * len(code_data)
    else:
        while len(code_data) > 0:
            code_data,char = huffman_decoding_char(code_data,tree)
            string += char
    
    return string
    
# Main function implementing huffman coding
# returns a dictionary includes{charactor:huffman_code}, e.g. {'e': '000', 'h': '001'}
def huffman_code_dict(node, bin_string=''):
    
    if node.is_leaf():  # it is leaf node
        if len(bin_string)>0:  # the huffman tree has only one
            return {node.char: bin_string}
        else:
            return {node.char: '1'}
    (l, r) = node.children()
    code_dict = dict()
    if l is not None:
        code_dict.update(huffman_code_dict(l, bin_string + '0'))
    if r is not None:
        code_dict.update(huffman_code_dict(r, bin_string + '1'))
    return code_dict

# Main function implementing huffman coding
#make a string by join all of the charactors huffman code.
def huffman_encoding(string):
    encoded_data = ""
    # Calculating frequency
    freq = {}
    #freq = {i: text.count(i) for i in set(text)}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    #freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # Create a priority queue to store live nodes of the Huffman tree
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
    
    if len(pq) == 0:  # the input string is None
        return None,None
    elif len(pq) == 1:
        root_node = heappop(pq)
    else:
        # make the tree
        while len(pq) > 1:
            # pickup 2 of the minimum values
            left = heappop(pq)
            right = heappop(pq)   
            sum_freq = left.freq + right.freq  # new parent node. the value is sum of the chilrens value.
            heappush(pq, Node(None, sum_freq, left, right))
        root_node = pq[0]
    tree = Tree(root_node)
    huffmanCode = huffman_code_dict(tree.get_root())
    for char in string:
        encoded_data += huffmanCode[char]
    return encoded_data,tree

#print(' Char | Huffman code ')
#print('----------------------')
#for (char, frequency) in freq:
#    print(' %-4r |%12s' % (char, huffmanCode[char]))


# In[5]:


#get a charactor from the left side of the given huffman code.

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[11]:


def test_function(string):
    encoded_data, tree = huffman_encoding(string)
    decoded_data = huffman_decoding(encoded_data, tree)
    if string == decoded_data:
        print("pass")
        print("Input string:", string)
        print("huffman code: ", encoded_data)
        print("tree:", tree)
        print("After decode:", decoded_data)
    else:
        print("fail")
        print("Input string:", string)
        print("huffman code: ", encoded_data)
        print("tree:", tree)
        print("After decode:", decoded_data)


# In[12]:


#Test case 1, edge case: the input string has only 1 type of letter
test_function("aaaa")  


# In[13]:


#Test case 2, edge case: the input string includes no letter
test_function("")


# In[14]:


#Test case 3, edge case: the input string includes continuously duplicated letter 
test_function("a bb ccc dddd eeee")


# In[15]:


#Test case 4, original problem's example string
test_function("The bird is the word")   


# In[ ]:





# In[ ]:




