#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df["C"] = df["C"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
filename = "Movies.csv"
movies = pd.read_csv(r"C:\Users\markc\desktop\Movies.csv")
movies.head()
movies.shape


# In[5]:


movies.head()


# In[6]:


from babel.numbers import format_currency


# In[7]:


movies["budget"] = movies["budget"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[8]:


movies.head()


# In[ ]:





# In[9]:


movies["revenue"] = movies["revenue"].apply(lambda x: format_currency(x, currency="EUR", locale="nl_NL"))


# In[10]:


movies.head()


# In[11]:


pd.to_datetime(movies['release_date'], dayfirst=True)


# In[12]:


movies.info()


# In[13]:


movies.head()


# In[14]:


movies["release_date"] = pd.to_datetime(movies["release_date"])
movies.info()


# In[15]:


movies.info()


# In[16]:


movies.drop_duplicates(subset=['id'])


# In[17]:


movies[(movies['release_date'] > 1999) & (movies['release_date'] < 2022)]


# In[18]:


movies.info()


# In[19]:


english_movies = movies[movies["original_language"].str.contains("en")==True]


# In[20]:


fr_es_movies = movies[movies["original_language"].str.contains("fr","es")==True]


# In[21]:


sns.scatterplot(x='release_date',y='revenue', data=fr_es_movies, hue='runtime', size='vote_average')


# In[22]:


sns.scatterplot(x='release_date',y='revenue', data=english_movies, hue='runtime', size='vote_average')


# In[23]:


movies.set_index('release_date', inplace=True)


# In[24]:


movies.head()


# In[25]:


english_movies.groupby(['release_date',"title",'budget','revenue',])


# In[26]:


english_movies.info()


# In[27]:


english_movies['genres'].value_counts().head(15)


# In[28]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

english_movies['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(10, 10), colors=colors)
plt.title('Pie Chart - Number of Titles by genres')


# In[29]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

fr_es_movies['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(15, 15), colors=colors)
plt.title('Pie Chart - Number of Titles by genres not taking revenue into account')


# In[30]:


fr_es_movies.head() 


# In[31]:


sns.relplot(x="release_date", y="runtime", data=fr_es_movies)


# In[32]:


sns.relplot(x="release_date", y="runtime", data=english_movies)


# In[33]:


english_movies.info()


# In[34]:


english_movies['release_date'] = pd.to_datetime(english_movies['release_date']).dt.date


# In[ ]:





# In[ ]:




