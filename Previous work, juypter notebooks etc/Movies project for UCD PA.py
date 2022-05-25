#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\PycharmProjects\pythonProject\UCD PA DA Project\Movies.csv")

Movies.head()


# In[4]:


Movies.shape


# In[5]:


Movies.head(10)


# In[6]:


Movies.info()


# In[9]:


Movies.drop("poster_path", inplace=True, axis=1)


# In[10]:


Movies.info()


# In[12]:


Movies.drop("backdrop_path", inplace=True, axis=1)


# In[13]:


Movies.drop("recommendations", inplace=True, axis=1)


# In[14]:


Movies.drop("production_companies", inplace=True, axis=1)


# In[15]:


Movies.info()


# In[17]:


Movies.head()


# In[18]:


movies = Movies


# In[19]:


movies.head()


# In[37]:


movies.dtypes


# In[26]:


movies.isnull().sum()


# In[31]:


##


# In[54]:


movies_released = movies[movies["status"].str.contains("In Production")==False]


# In[55]:


movies_released.head(50)


# In[56]:


### movies_released is the new DF


# In[58]:


movies_released.head(50)


# In[62]:


movies_released.shape


# In[63]:


movies_releasedeng = movies_released[movies_released["original_language"].str.contains("en")==True]


# In[64]:


movies_releasedeng.shape


# In[65]:


### movies_releasedeng is new DF


movies_releasedeng.shape





