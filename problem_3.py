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

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

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

#Test case 1, edge case: the input string has only 1 type of letter
test_function("aaaa")  

#Test case 2, edge case: the input string includes no letter
test_function("")

#Test case 3, edge case: the input string includes continuously duplicated letter 
test_function("a bb ccc dddd eeee")

#Test case 4, original problem's example string
test_function("The bird is the word")