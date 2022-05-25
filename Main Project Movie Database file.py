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


# In[64]:


movies.info()


# In[65]:


movies.drop("backdrop_path", inplace=True, axis=1)
movies.drop("recommendations", inplace=True, axis=1)
movies.drop("credits", inplace=True, axis=1)
movies.drop("overview", inplace=True, axis=1)
movies.drop("poster_path", inplace=True, axis=1)


# In[66]:


movies.info()


# In[67]:


movies_budgeted = movies[(movies['budget'] != 0) & (movies['revenue'] != 0)]
movies_budgeted.head(26)


# In[68]:


english_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("en")==True]
english_movies.head(26)


# In[69]:


fr_es_movies = movies_budgeted[movies_budgeted["original_language"].str.contains("fr","es")==True]
fr_es_movies.head(26)


# In[70]:


# movies database tidied into budgeted database which was used to create english_movies & fr_es_movies database


# In[71]:


fr_es_movies.drop_duplicates(subset=['id'])


# In[72]:


english_movies.drop_duplicates(subset=['id'])


# In[73]:


english_movies.info()


# In[74]:


english_movies.isnull().sum()


# In[75]:


fr_es_movies.isnull().sum()


# In[76]:


eng_movies = english_movies.dropna(subset=['release_date', 'runtime'])


# In[77]:


eng_movies.isnull().sum()


# In[78]:


plt.scatter(eng_movies['budget'], eng_movies['revenue'], s=2)
plt.show()


# In[79]:


plt.scatter(eng_movies['revenue'], eng_movies['release_date'], s=2)
plt.show()


# In[80]:


sns.scatterplot(x='release_date',y='runtime', data=eng_movies, hue='revenue', size='popularity')


# In[81]:



eng_movies.loc[6]
eng_movies.info()


# In[82]:


sns.scatterplot(x='release_date',y='runtime', data=eng_movies, hue='popularity', size='revenue')


# In[83]:


eng_movies.head(25)


# In[84]:


eng_movies.info()


# In[85]:


movies.info()


# In[86]:


pd.to_datetime(movies['release_date'], dayfirst=True)


# In[63]:





# In[ ]:




