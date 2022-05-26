#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
filename = "Movies.csv"
movies = pd.read_csv(r"C:\Users\markc\desktop\Movies.csv")
movies.head()
movies.shape


# In[4]:


movies.info()


# In[5]:


movies.drop("backdrop_path", inplace=True, axis=1)
movies.drop("recommendations", inplace=True, axis=1)
movies.drop("credits", inplace=True, axis=1)
movies.drop("overview", inplace=True, axis=1)
movies.drop("poster_path", inplace=True, axis=1)


# In[6]:


movies.info()


# In[7]:


movies_budgeted = movies[(movies['budget'] != 0) & (movies['revenue'] != 0)]
movies_budgeted.head(26)


# In[8]:


english_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("en")==True]
english_movies.head(26)


# In[ ]:


fr_es_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("fr","es")==True]
fr_es_movies.head(5)


# In[10]:


# movies database tidied into budgeted database which was used to create english_movies & fr_es_movies database


# In[11]:


fr_es_movies.drop_duplicates(subset=['id'])


# In[12]:


english_movies.drop_duplicates(subset=['id'])


# In[13]:


english_movies.info()


# In[14]:


english_movies.isnull().sum()


# In[15]:


fr_es_movies.isnull().sum()


# In[16]:


eng_movies = english_movies.dropna(subset=['release_date', 'runtime'])


# In[17]:


eng_movies.isnull().sum()


# In[18]:


plt.scatter(eng_movies['budget'], eng_movies['revenue'], s=2)
plt.show()


# In[19]:


plt.scatter(eng_movies['revenue'], eng_movies['release_date'], s=2)
plt.show()


# In[20]:


sns.scatterplot(x='release_date',y='runtime', data=eng_movies, hue='revenue', size='popularity')


# In[21]:



eng_movies.loc[6]
eng_movies.info()


# In[22]:


sns.scatterplot(x='release_date',y='runtime', data=eng_movies, hue='popularity', size='revenue')


# In[23]:


eng_movies.head(25)


# In[24]:


eng_movies.info()


# In[25]:


movies.info()


# In[26]:


movies.to_datetime(movies['release_date'], dayfirst=False)


# In[ ]:





# In[ ]:




