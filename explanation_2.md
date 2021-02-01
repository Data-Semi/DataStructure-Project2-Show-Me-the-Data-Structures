## Program structure
### Methods
This program can find all files under a directory (and all directories beneath it) that end with any specified suffix.   
The method `find_files(suffix, path)`is used recursively. Every time found a subdirectory it will recursively call itself, otherwise, it will judge whether the path match the inputted suffix or not.  
Every matched path will append to the path list as output.  

### Tests
Tests include below:  
Test case 1: Find *.c files  
Test case 2: Find *.h files  
Test case 3: Edge case, list all files inside the directory  
Test case 4: Edge case, there is no such directory  

## Time complextity
All operation takes O(1) and a for-loop inside `find_files(suffix, path)` enumerates subdirectories in inputted path, the time complexity is O(n).  
Therefore, The total time complexity is O(n).

## Space complexity  

`find_files(suffix, path)`: It saves all the file path strings we insert in `answer` list which has a Space Complexity of O(n). It is also internally having fixed number of variables, and the sizes of the variables are independent of the size of the `answer` list, hence it is constant in nature. Therefore, this method has a Space Complexity of O(n).

