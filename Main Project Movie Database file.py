#!/usr/bin/env python
# coding: utf-8

# In[34]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
filename = "Movies.csv"
movies = pd.read_csv(r"C:\Users\markc\desktop\Movies.csv")
movies.head()
movies.shape


# In[35]:



movies.info()


# In[36]:


movies.drop("backdrop_path", inplace=True, axis=1)
movies.drop("recommendations", inplace=True, axis=1)
movies.drop("credits", inplace=True, axis=1)
movies.drop("overview", inplace=True, axis=1)
movies.drop("poster_path", inplace=True, axis=1)


# In[37]:


movies.info()


# In[53]:


movies_budgeted = movies[(movies['budget'] != 0) & (movies['revenue'] != 0)]
movies_budgeted.head(26)


# In[54]:


english_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("en")==True]
english_movies.head(26)


# In[55]:


fr_es_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("fr","es")==True]
fr_es_movies.head(26)


# In[57]:


# movies database tidied into budgeted database which was used to create english_movies & fr_es_movies database


# In[58]:


fr_es_movies.drop_duplicates(subset=['id'])


# In[59]:


english_movies.drop_duplicates(subset=['id'])


# In[61]:


english_movies.info()


# In[62]:


english_movies.isnull().sum()


# In[63]:


fr_es_movies.isnull().sum()


# In[ ]:
print(fr_es_movies)



