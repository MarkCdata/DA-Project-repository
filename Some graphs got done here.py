#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df["C"] = df["C"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
filename = "Movies.csv"
movies = pd.read_csv(r"C:\Users\markc\desktop\Movies.csv")
movies.head()
movies.shape


# In[2]:


movies.head()


# In[41]:


from babel.numbers import format_currency


# In[43]:


movies["budget"] = movies["budget"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[44]:


movies.head()


# In[ ]:





# In[6]:


movies["revenue"] = movies["revenue"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[7]:


movies.head()


# In[8]:


pd.to_datetime(movies['release_date'], dayfirst=True)


# In[9]:


movies.info()


# In[11]:


movies.head()


# In[15]:


movies["release_date"] = pd.to_datetime(movies["release_date"])
movies.info()


# In[17]:


movies.info()


# In[25]:


movies.drop_duplicates(subset=['id'])


# In[30]:


movies[(movies['release_date'] > 1999) & (movies['release_date'] < 2022)]


# In[31]:


movies.info()


# In[34]:


english_movies = movies[movies["original_language"].str.contains("en")==True]


# In[35]:


fr_es_movies = movies[movies["original_language"].str.contains("fr","es")==True]


# In[36]:


sns.scatterplot(x='release_date',y='revenue', data=fr_es_movies, hue='runtime', size='vote_average')


# In[37]:


sns.scatterplot(x='release_date',y='revenue', data=english_movies, hue='runtime', size='vote_average')


# In[45]:


movies.set_index('release_date', inplace=True)


# In[46]:


movies.head()


# In[51]:


english_movies.groupby(['release_date',"title",'budget','revenue',])


# In[56]:


english_movies.info()


# In[66]:


english_movies['genres'].value_counts().head(15)


# In[67]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

english_movies['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(10, 10), colors=colors)
plt.title('Pie Chart - Number of Titles by genres')


# In[68]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

fr_es_movies['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(15, 15), colors=colors)
plt.title('Pie Chart - Number of Titles by genres')


# In[70]:


fr_es_movies.head() 


# In[75]:


sns.relplot(x="release_date", y="runtime", data=fr_es_movies)


# In[76]:


sns.relplot(x="release_date", y="runtime", data=english_movies)


# In[77]:


english_movies.info()


# In[78]:


english_movies['release_date'] = pd.to_datetime(english_movies['release_date']).dt.date


# In[ ]:




