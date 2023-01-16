#!/usr/bin/env python
# coding: utf-8

# # 2. Aritmatika & logika

# In[5]:


# KaBaTaKu
print(1990 - 1.5)
print("Hello" + " World")
print("hey" * 15)


# In[7]:


#katabaku pt2
y = 67 - 75 * 15 + 100
print(y)


# In[10]:


# pangkat
p = 2**3
print(p) #hasilnya akan keluar 8


# In[11]:


# modulo
print(10 % 3) #hasilnya akan keluar 1
print(2 % 2) #hasilnya akan keluar 0


# In[12]:


print(10 / 3) #hasilnya akan keluar 3.333
# floor
print(10 // 3) #hasilnya akan keluar 3


# In[13]:


# IF
nilai = 70
if nilai >= 75:
    print("Kamu Lulus!")


# In[14]:


# IF - ELSE
nilai = 75
if nilai >= 75:
    print("Kamu Lulus!")
else:
    print("Kamu Tidak Lulus!")


# In[15]:


# for Loop
my_list = [1, 20, 300, 4000]
for i in my_list:
    print(i**2)


# In[16]:


# for loop
a = 2
b = 3
un = a
for i in range(0, 10):
    print(i)
    un = un + b
    
print(un)


# In[17]:


# while loop
cnt = 0
while cnt<8:
    cnt += 1
    print(cnt)


# In[18]:


# while loop
a = 2
b = 3
un = a
while (un <= 30):
    un = un + b
print(un)


# In[ ]:




