## Program structure
### Methods
This program can find all files under a directory (and all directories beneath it) that end with any specified suffix.   
The method `find_files(suffix, path)`is used recursively. Everytime found a subdirectory it will recursively call itself, otherwise it will judge whether the path macth the inputed suffix or not.  
Every matched path will append to the path list as output.  

## Time complextity
All operation takes O(1) and a for-loop inside `find_files(suffix, path)` enumelates subdirectoties in inputed path, the time complexity is O(n).  
Therefor, The total time complexity is O(n).