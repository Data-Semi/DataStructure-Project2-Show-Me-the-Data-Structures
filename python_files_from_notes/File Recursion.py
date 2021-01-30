#!/usr/bin/env python
# coding: utf-8

# ## Finding Files
# ### problem description  
# For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
# 
# Here is an example of a test directory listing, which can be downloaded here:
# 
# ./testdir
# ./testdir/subdir1
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3
# ./testdir/subdir3/subsubdir1
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h  
# 
# Python's os module will be useful—in particular, you may want to use the following resources:
# 
# os.path.isdir(path)
# 
# os.path.isfile(path)
# 
# os.listdir(directory)
# 
# os.path.join(...)
# 
# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

# ### Analysis
# This program can find all files under a directory (and all directories beneath it) that end with any specified suffix.  
# The method is using recursively. Everytime when the method found an subdirectory it will recursively call itself,   
# otherwise it will judge whether the path macth the suffix or not.  
# Every matched answer will append to the answer list to output.  

# In[1]:


# recursion
#get a path list inside the path, and loop inside 
# if it is a file,
    #check if this file has the suffix
# elif it is a subdirectory, 
    #call the function recursively
    
import os

answer=[]
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    #Base condition
    if os.path.exists(path):  # if the path is exists
        if os.listdir(path) == []:  # inside the path is empty
            return None
    else:  # if the path is not exists
        return None
    
    answer = []
    dir_list = os.listdir(path)  # ['subdir1', 'subdir2', 'subdir3', 'subdir4', 'subdir5', 't1.c', 't1.h']
    for sub_path in dir_list:
        fullpath = path + "/" + sub_path
        if os.path.isfile(fullpath):  # os.path.isfile("./testdir/"+"subdir3")
            if sub_path.endswith(suffix):
                answer.append(fullpath)
        else:
            small_output = find_files(suffix,fullpath)
            answer.extend(small_output)
    return answer


# In[15]:


def test_function(func_return,expected_result):
    if (func_return == expected_result):
        print("pass")
        print("The function returned: ",func_return)
    else:
        print("fail")
        print("The function returned: ",func_return)


# In[16]:


#Test case 1, find *.c files
test_c = find_files(".c","./testdir")
answer_c =['./testdir/subdir1/a.c',
 './testdir/subdir3/subsubdir1/b.c',
 './testdir/subdir5/a.c',
 './testdir/t1.c']
test_function(test_c, answer_c)


# In[17]:


#Test case 2, find *.h files
test_h = find_files(".h","./testdir")
answer_h =['./testdir/subdir1/a.h',
 './testdir/subdir3/subsubdir1/b.h',
 './testdir/subdir5/a.h',
 './testdir/t1.h']
test_function(test_h, answer_h)


# In[18]:


#Test case 3, edge case, list all files inside the derectory
test_all = find_files("","./testdir")
answer_all = ['./testdir/subdir1/a.c',
 './testdir/subdir1/a.h',
 './testdir/subdir2/.gitkeep',
 './testdir/subdir3/subsubdir1/b.c',
 './testdir/subdir3/subsubdir1/b.h',
 './testdir/subdir4/.gitkeep',
 './testdir/subdir5/a.c',
 './testdir/subdir5/a.h',
 './testdir/t1.c',
 './testdir/t1.h']
test_function(test_all, answer_all)


# In[19]:


#Test case 4, edge case, there is no such directory
test_None = find_files("","")
answer_None = None
test_function(test_None, answer_None)


# In[ ]:




