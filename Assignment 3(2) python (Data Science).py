#!/usr/bin/env python
# coding: utf-8

# Q1. Create a python program to sort the given list of tuples based on integer value using a
# lambda function.
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[75]:


l= [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
l.sort(key = lambda x: x[1])


# In[76]:


print(l)


# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
# lambda and map functions.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[1]:


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[2]:


map(lambda x: x**2,l )


# In[3]:


list(map(lambda x: x**2,l ))


# 2nd method

# In[21]:


def sq(l):
    l2=[]
    for i in l:
        l2.append(i**2)
    return l2


# In[24]:


sq(l)


# 3rd method

# In[26]:


def sq(x):
    return x**2


# In[27]:


list(map(sq,l))


# Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
# lambda functions
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[28]:


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[40]:


def convert(l):                  
    return tuple(l)


# In[41]:


convert(l)


# In[52]:


d = lambda l: tuple(l)


# In[55]:


d(l)


# Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.

# In[64]:


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


# In[65]:


from functools import reduce


# In[68]:


reduce(lambda x,y:x*y,l)


# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
# filter function.
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

# In[ ]:





# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
# ['python', 'php', 'aba', 'radar', 'level']

# In[73]:


l =['python', 'php', 'aba', 'radar', 'level']
print("Given List",l)


# In[70]:


result= list(filter(lambda x: (x == "".join(reversed(x))), l)) 


# In[74]:


print("List of palindromes",result)


# In[ ]:




