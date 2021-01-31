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
All methods inside class `Node` and  `Tree` have space complexity O(1).  
In method `huffman_decoding_char`, the recursion operation has space complexity O(n), other operations have O(1). Thus, this method's space complexity is O(n).  
In method `huffman_decoding`, a while loop has space complexity O(n), other operations have O(1).
In method `huffman_code_dict`, the recursion operation has space complexity O(n), other operations have O(1). Thus, this method's space complexity is O(n).  
In method `huffman_encoding` has 3 loop operations, and all of them have space complexity O(n). The operation `heapq.heapify`, `heappop`, `heappush` has space complexity O(n). other operations have O(1). Thus, this method's space complexity is O(n).  
Therefore, This program's space complexity is O(n).  
In method `test_function`, other of mentioned operations above have O(1). Thus, this method's space complexity is O(n).  
In the method `main`, we do not have any loop operation and other of mentioned operations above have O(1). Therefore, this program has space complexity O(n).

 

