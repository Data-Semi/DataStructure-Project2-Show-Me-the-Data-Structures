## Program structure
### Methods
I have written a test function to see whether the input string is restored after go through the encode function and the decode function.  

### Tests
Tests include below:  
Test case 1, edge case: The input string has only 1 type of letter  
Test case 2, edge case: The input string includes no letter  
Test case 3, edge case: The input string includes continuously duplicated letter  
Test case 4: Original problem's example string  

## Time complextity
The reason I chose priority queue data structure in the encoding method `huffman_encoding(string)` is because a priority queue has time complexity O(logn). It is much smaller than sorting a dictionary has time complexity O(n).  

To make the program readable, I have used string class to store the above program's encoded string.  
If we treat the encoded data as binary data, the size of the data is much smaller than the original size of data. Note that the input string's storage is 19 x 8 =152 bits (38 bytes), but our encoded string only takes 70bits (18bytes). i.e.,about 54% of data compression.  

I used the method `sys.getsizeof()` to calculate storage size. And, we can see the data is compressed after encoding.  
The returned size from `sys.getsizeof()` includes not only the size of data itself, but also other information data in python. i.e. `sys.getsizeof(a_great_sentence))` returns 69 bytes instead of 38 bytes. The sentense `sys.getsizeof(int(encoded_data, base=2)))` returns 36bytes instead of 18bytes.   

## Space complexity  

Class `Node` and Class `Tree`: Internally having fixed number of variables constant in nature, hence the Space Complexity is O(1).  

`huffman_decoding_char`: It saves remained huffman code strings in `remain_code_data` list which has a Space Complexity of O(n). It is also internally having fixed number of variables, and the sizes of the variables are independent of the size of the `remain_code_data` list, hence it is constant in nature. Therefore, this method has a Space Complexity of O(n).  

`huffman_decoding`: the function only access the `code_data` list and return a single value regardless of the size of the `code_data`, hence it is constant in nature and hence it is O(1).  

`huffman_code_dict`: It saves all the elements we insert in a dictionary `code_dict` which has a Space Complexity of O(n). It is also internally having fixed number of variables, and the sizes of the variables are independent of the size of the `code_dict` list, hence it is constant in nature. Therefore, this method has a Space Complexity of O(n).  

`huffman_encoding`: The variables `freq`, `pq`, `encoded_data`, `huffmanCode` save data and the data sizes are depend on inputted string size. Thus, every one of the variables has a Space Complexity of O(n). It is also internally having fixed number of variables, and the sizes of the variables are independent of the size of the inputted string size, hence it is constant in nature. Therefore, this method has a Space Complexity of O(4n).
