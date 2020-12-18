#!/usr/bin/env python
# coding: utf-8

# In[15]:


print ("Enter 6 numbers with both positive and negative values")
#getting input from user
n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
n3 = float(input("Enter third number:"))
n4 = float(input("Enter fourth number:"))
n5 = float(input("Enter fifth number:"))
n6 = float(input("Enter sixth number:"))
#gathering them into one variable

l1 = (n1,n2,n3,n4,n5,n6)
print("your values were ",l1)
print("Following are the positive values ")
#filtering positive values
for x in(l1):
    
    if x>0:
        
        print(x)


# In[ ]:





# In[ ]:




