#!/usr/bin/env python
# coding: utf-8

# In[7]:


print ("FIBONACCI SERIES")
n = int(input("Number of terms required ")) #getting desired number of terms from user
s1 = 0 #number 1
s2 = 1 #number 2
terms = 0
print ("Your requested sequence is ")
while terms < n:
    print(s1)
    add = s1 + s2 
    s1 = s2       
    s2 = add      
    terms += 1
    
    


# In[ ]:





# In[ ]:




