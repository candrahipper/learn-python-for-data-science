#!/usr/bin/env python
# coding: utf-8

# # 1. variabel dan type data

# In[1]:


# Assign data ke variable
x = 1995
y = "Hall-o dunyia"
z = 4.5


# In[3]:


# print variable
print(x)
print(y, z)
print(x, y, z)


# In[4]:


# penamaan variable tidak bisa didahului angka pasti eror
1 = 1990


# In[5]:


# penamaan variable tidak bisa dengan spasi
x_y = 1


# In[13]:


# penamaan dua variable atau lebih, bisa dalam satu baris
x, y, m, n = 1900, "Hall-o dunyia", 'yuk', 1.5 


# In[14]:


# string
nama = "Hello World!"
angka = "4.5"
nol = 'hayo 0'

jumat = "jum'at"
rata_rata = 'rata"'


# In[15]:


print(nama, angka, nol, jumat, rata_rata)


# In[17]:


# integer
satu = 1


# In[18]:


# float
satu_koma_lima = 1.5


# In[26]:


lima = 1.


# In[27]:


print(lima)


# In[28]:


# Boolean
Betul = false
komparasi = satu == 1


# In[31]:


satu ==1


# In[33]:


# list
biodata = ["hip hip", 165, 36.8]
biodata[2]


# In[34]:


biodata[2] = 37


# In[35]:


print(biodata)


# In[36]:


# Tuple
biodata = ("hip hip", 165, 37.8)


# In[37]:


biodata[2] = 38


# In[40]:


# Set
biodata = {"hip hip", 165, 35.4, "hip hip"}


# In[41]:


biodata


# In[43]:


# Dictionary
biodata = {"Nama":"hip hip", "Tinggi":165, "umur":28}


# In[44]:


biodata.keys()


# In[49]:


biodata.values()


# In[53]:


biodata ['Nama']


# In[69]:


biodata ['Nama'] = 'nad nad'


# In[72]:


biodata


# In[ ]:




