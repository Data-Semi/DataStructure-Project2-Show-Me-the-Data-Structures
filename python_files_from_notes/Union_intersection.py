#!/usr/bin/env python
# coding: utf-8

# ## Union and Intersection of Two Linked Lists
# ### problem description  
# Your task for this problem is to fill out the union and intersection functions.  
# The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.  
# 
# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.  
# Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.  

# ### Analysis
# Assume that the input sets A and B only includes numbers which can be sorted.   
# For save searching time, I choose to use ordered linked list. The method addNode_acceding_order() has one loop, therefore, the Big O is O(n).  
# The ordered linked list allowes me to stop search before reach to the end of linked list, but it didn't change the time complexity. Both of the method union() and intersection() has two loops, therefor, the Big O is O(n^2).  
# Therefore, This program has time complexity O(n^2 + n).  

# In[66]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    def to_list(self):  # Change to list object. This is for test_function
        data = []
        curr = self.head
        while curr is not None:
            data.append(curr.value)
            curr = curr.next
        return data

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def append_node(self, new_node):

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node
    
    def addNode_acceding_order(self, value):  # Add node in accending order
        curr = self.head
        if curr is None:
            self.head = Node(value)
            return

        if curr.value >= value:
            n = Node(value)
            n.next = curr
            self.head = n
            return

        while curr.next is not None:  # Big O is O(n)
            if curr.next.value >= value:
                break
            curr = curr.next
        n = Node(value)
        n.next = curr.next
        curr.next = n
        return    
        
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # if not found the same element in llist_2, append node1 to union_list, finally link to llist_2
    union_list =  LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    
    if node1 is None:
        return llist_2
    if node2 is None:
        return llist_1
    
    while node1 is not None:
        while node2 is not None:
            if node1.value == node2.value:
                #Found the same value
                # I can shorten the search length in llist2, next search will start from this node2
                break
            elif node1.value < node2.value:
                # I can not find same value after this node2 in llist2.
                new_node = Node(node1.value)
                union_list.append_node(new_node)
                # Let's do next node1. reset node2 from the head
                node2 = llist_2.head
                break
            elif node1.value > node2.value and node2.next is None:
                # Reach the end of llist2 , but still didn't found
                new_node = Node(node1.value)
                union_list.append_node(new_node)
                # lets do next node1. reset node2 from the head
                node2 = llist_2.head
                break
            else:
                #continue
                node2 = node2.next             
        node1 = node1.next
        
    new_node.next = llist_2.head
    return union_list

def intersection(llist_1, llist_2):
    # If found the same element in llist_2, 
    # append node1 to intersection_list, 
    # next start is from next element in llist_2
    
    intersection_list =  LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head

    if node1 is None or node2 is None:
        return intersection_list
    
    while node1 is not None:
        while node2 is not None:
            if node1.value == node2.value:
                #Found the same value
                # I can shorten the search length in llist2, next search will start from this node2
                intersection_list.append(node1.value)
                node2 = node2.next
                break
            elif node1.value < node2.value:
                # I can not find same value after this node2 in llist2.
                # Let's do next node1. reset node2 from the head
                node2 = llist_2.head
                break
            elif node1.value > node2.value and node2.next is None:
                # Reach the end of llist2 , but still didn't found
                # Let's do next node1. reset node2 from the head
                node2 = llist_2.head
                break
            else:
                #Continue
                node2 = node2.next             
        node1 = node1.next

    return intersection_list


# In[67]:


def test_function(func_return, expected_result):
    if (func_return.to_list() == expected_result):
        print("pass")
        print("The function returned llist: ", func_return)        
    else:
        print("fail")
        print("The function returned llist: ", func_return)


# In[68]:


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    #linked_list_1.append(i)
    linked_list_1.addNode_acceding_order(i)

for i in element_2:
    #linked_list_2.append(i)
    linked_list_2.addNode_acceding_order(i)

test_function(union(linked_list_1,linked_list_2), [2, 3, 3, 35, 65, 1, 1, 4, 6, 6, 9, 11, 21, 32])
test_function(intersection(linked_list_1,linked_list_2), [4, 6, 6, 21])   

# Test case 2
# edge case: No intersection

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test_function(union(linked_list_3,linked_list_4), [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1, 7, 8, 9, 11, 21, 1])
test_function(intersection(linked_list_3,linked_list_4), [])


# In[72]:


# Test case 3
# edge case: input an empty llist

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,3,2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

test_function(union(linked_list_5,linked_list_6), [1, 3, 2])
test_function(intersection(linked_list_4,linked_list_5), [])

