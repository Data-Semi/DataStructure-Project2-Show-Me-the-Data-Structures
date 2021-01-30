## Program structure
### Methods
I wrote a test function to see whether the input string is restored after go through the encode function and the decode function.

The reason I chose priority queue data structure in encoding method `huffman_encoding(string)` is because a priority queue has time complexity O(logn). It is much more small than sorting a dictionary has time complexity O(n).

To make the program readable, I have used string class to store the above program's encoded string.  
If we treat the encoded data as a binary data, the size of the data is much smaller than the original size of data. Note that the input string's storage is 19 x 8 =152 bits (38 bytes), but our encoded string only takes 70bits (18bytes). i.e.,about 54% of data compression.  

I used the method `sys.getsizeof()` to calculate storage size. And, we can see the data is compressed after encoding.
The returned size from `sys.getsizeof()` includes not only the size of data itself, but also other information data in python. i.e. `sys.getsizeof(a_great_sentence))` returns 69 bytes instead of 38 bytes. The sentense `sys.getsizeof(int(encoded_data, base=2)))` returns 36bytes instead of 18bytes.   


