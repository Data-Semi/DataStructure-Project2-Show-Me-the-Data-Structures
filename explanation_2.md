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
The method `os.listdir(path)` has space complexity O(n), and the loop operation `for sub_path in dir_list:` has O(n), other operations have O(1). Thus, this program's space complexity is O(n).  
In method `test_function`, other of mentioned operations above have O(1). Thus, this method's space complexity is O(n).  
In the method `main`, we do not have any loop operation and other of mentioned operations above have O(1). Therefore, this program has space complexity O(n).
