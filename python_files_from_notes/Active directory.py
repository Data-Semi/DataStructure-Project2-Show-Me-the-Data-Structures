#!/usr/bin/env python
# coding: utf-8

# ## Active Directory
# ### problem description  
# 
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.  
# Write a function that provides an efficient look up of whether the user is in a group.

# ### Analysis
# I decided to use recursion. If there is a subgroup inside a group, recrsively use the method is_user_in_group().
# For better understanding, I made the method print_group_structure() to print out full pathes of every finding in the inputed group.
# Tests includes as below:
# Test case 1: The user is inside the group
# Test case2: The user is not inside the group
# Test case3: No user to find
# Test case4: empty group
# Test case5: Befor and after add a user to a group

# In[1]:


class Group(object):
    def __init__(self, _name=None):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

#Write a function that provides an efficient look up of whether the user is in a group.
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # If any of the input is empty
    if user == "" or group.get_name() is None:
        return False
        
    result = False
    sub_groups = group.get_groups()
    users = group.get_users()
    if user in users:
        return True
    else:
        for sub_group in sub_groups:
            result = is_user_in_group(user,sub_group)
            if result is True:
                break
    return result


# In[2]:


def test_function(func_return,expected_result):
    if (func_return == expected_result):
        print("pass")
        print("The function returned: ", func_return)
    else:
        print("fail")
        print("The function returned: ", func_return)
        
# the group structure is as below:
# group name is follwed by "/"
def print_group_structure(group, parent_path = ""):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.name is None:
        print("It is an empty group.")
        return
    sub_groups = group.get_groups()
    users = group.get_users()
    now_group_path = parent_path + group.get_name() + "/"
    
    print(now_group_path)
    
    path = ""
    
    for user in users:
        print(now_group_path + user)
        
    for sub_group in sub_groups:
        print_group_structure(sub_group, now_group_path)


# In[3]:


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
empty_group = Group()

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

# Test case1: The user is inside the group
test_function(is_user_in_group("sub_child_user", parent), True)  
test_function(is_user_in_group("sub_child_user", child), True)
test_function(is_user_in_group("sub_child_user", sub_child), True)

# Test case2: The user is not inside the group
test_function(is_user_in_group("anyuser", sub_child), False)  
test_function(is_user_in_group("anyuser", parent), False)

# Test case3: No user to find
test_function(is_user_in_group("", parent), False)  

# Test case4: empty group
test_function(is_user_in_group("sub_child_user",empty_group), False)  

# Test case5: Befor and after add a user to a group
test_function(is_user_in_group("parent_user", parent), False) 
parent.add_user("parent_user")
test_function(is_user_in_group("parent_user", parent), True)


# In[4]:


print_group_structure(parent)


# In[5]:


print_group_structure(empty_group)


# In[ ]:




