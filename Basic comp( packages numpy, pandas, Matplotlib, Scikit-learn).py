#!/usr/bin/env python
# coding: utf-8

# # Packages

# # 1. Numpy & Pandas

# In[1]:


# Import pandas library
import pandas as pd


# In[2]:


get_ipython().system('pip install pandas')


# In[34]:


# Membuat DataFrame
df = pd.DataFrame(columns=['Nama','Mafa'])


# In[35]:


df


# In[36]:


# input data
df = df.append({'Mafa':'nasi ayam','Nama':'hiphip'}, ignore_index=True)
df = df.append({'Nama':'Syauqi','Mafa':'Mie Instant'}, ignore_index=True)
df['Mifa'] = ['Kopi','Es Teh']
df


# In[37]:


# Membuat DataFrame dari Dictionary
data = {'Nama':['hiphip','Syauqi','F'], 'Mafa':['nasi ayam','Mie Instant','Bakso']}
df = pd.DataFrame(data)


# In[39]:


df


# In[40]:


# Import numpy library
import numpy as np


# In[54]:


# Membuat Array
array_1 = np.array([1, 0, 0, 1])
array_2 = np.array([0, 1, 1, 2])
print(array_1.reshape(2,2)) #mengubah bentuk array
print(array_2.reshape(2, 2))


# In[44]:


print(array_1.reshape(4, 3))


# In[49]:


print([1, 0, 0, 1] + [0, 1, 1, 2])


# In[55]:


print(array_1 + array_2)
np.dot(array_1.reshape(1,4), array_2.reshape(4,1)) #perkalian matriks 2 x 2


# In[56]:


# filter
print(array_2)
np.where(array_2 > 0, 'Yes', 'No')


# # 2. MatPlotlip

# In[57]:


# Import matplotlib library
import matplotlib.pyplot as plt


# In[58]:


# Membuat Array
array_1 = np.array(range(-10,11))
array_2 = np.array(list(map(lambda x : x**2, list(array_1))))

# Membuat line plot dari array
plt.plot(array_1, array_2)
plt.show()


# In[59]:


# Membuat bar plot dari array
plt.bar(['nasi ayam', 'Bubur Ayam', 'Mie Instant'], [10, 9, 7])
plt.show()


# In[63]:


random_array_1 = np.random.randint(1, 100, 100)
random_array_2 = np.random.randint(1, 100, 100)

# Membuat scatter plot dari array
plt.scatter(random_array_1, random_array_2)
# plt.scatter(array_1, array_2)
plt.show()


# # 3. Scikit-learn

# In[64]:


# !pip install scikit-learn
# Import scikit-learn library
import sklearn


# In[74]:


import pandas as pd


# In[72]:


# Scaling, Input Values, Create train and testing data
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split


# In[73]:


import sklearn.preprocessing.StandardScaler as ss


# In[67]:


import sklearn.preprocessing as prepro


# In[68]:


prepro.StandardScaler


# In[69]:


StandardScaler


# In[70]:


# Model with variational method from regression, classification, or clustering
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans


# In[71]:


# evaluate and tuning the model using variational method like cross-validation, grid-search
from sklearn.metrics import r2_score, accuracy_score, silhouette_score
from sklearn.model_selection import cross_validate, GridSearchCV, RandomizedSearchCV


# In[ ]:




