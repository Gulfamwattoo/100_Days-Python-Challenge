#!/usr/bin/env python
# coding: utf-8

# # Day-01

# In[1]:


print("Hello! I am starting my 100-days challenge")


# In[3]:


num1=int(input("Enter the First num:"))
num2=int(input("Enter the Second num:"))
print(f"Multiplacation of {num1} and {num2} is:",num1*num2)


# In[4]:


print('''I am asking from "all of you" is it right way to display!''')


# In[5]:


print("I have found \"another way\" to display the string, hope you will like it!")


# String Manuplation

# In[8]:


print("I am Gulfam\nI am Gulfam")


# In[10]:


print("Hello"+"Gulfam")
print("Hello "+ "Gulfam")
print("Hello"+" "+ "Gulfam")


# ## Input() Function

# In[12]:


#input() Function is used to take input from user(console)

input("What's your name?")


# In[14]:


print("Hello "+ input("What's your name")+ "!")


# In[16]:


count_len=len(input())
print(count_len)


# In[17]:


print(input())
print(input())
print(input())


# In[19]:


#Swap two variables-this will use for any type of data

a=input()
b=input()
#create a third variable to swap value
c=a
a=b
b=c
print("a:",a)
print("b:",b)


# In[21]:


#swap two numbers only in the form of integer
a=int(input())
b=int(input())
#create a third variable to swap value
c=a+b
a=c-a
b=c-b
print("a:",a)
print("b:",b)


# # Day-1 Project 

# In[30]:


#Brand Name Generator 
print("Welcome to the Brand Name Generatorn")
#Take input from the user
city=input("What's the name of city you grew up?\n")
pet=input("What's you pet Name?\n")

#output of the given input 
print(f"Your Band name could be {city} {pet}")


# In[ ]:




