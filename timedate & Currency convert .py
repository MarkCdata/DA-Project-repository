#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[3]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[4]:


Movies.info()


# In[5]:


from babel.numbers import format_currency

Movies["budget"] = Movies["budget"].apply(lambda x: format_currency(x, currency="USD", locale="en_US"))
Movies["revenue"] = Movies["revenue"].apply(lambda x: format_currency(x, currency="USD", locale="en_US"))


# In[6]:


Movies.head()


# In[33]:


Movies['release_date'] = pd.to_datetime(Movies['release_date'],format='%Y-%m-%d')


# In[34]:


Movies.info()


# In[35]:


import datetime 


# In[36]:


Movies['month_year'] = Movies['release_date'].dt.to_period('M')


# In[15]:


Movies.head()


# In[37]:


Movies.drop("backdrop_path", inplace=True, axis=1)
Movies.drop("recommendations", inplace=True, axis=1)
Movies.drop("credits", inplace=True, axis=1)
Movies.drop("overview", inplace=True, axis=1)
Movies.drop("poster_path", inplace=True, axis=1)
Movies.head()


# In[38]:


Movies[(Movies['month_year'] >= 1999) & (Movies['month_year'] < 2020)]


# In[18]:


Movies.info()


# In[27]:


Movies.set_index('id', inplace=True)
Movies.info()


# In[28]:


Movies.index


# In[39]:


filtered_Movies = Movies.loc[(Movies['release_date'] >= '1999-12-31')
                     & (Movies['release_date'] < '2022-12-31')]


# In[41]:


filtered_Movies.head(35)


# In[64]:


filtered_Movies.dropna(subset=['budget'])


# In[56]:


filtered_Movies.reset_index()


# In[53]:


filtered_Movies.head(56)


# In[58]:


filtered_Movies.info()


# In[62]:


filtered_Movies['budget'] = filtered_Movies['budget'].apply(lambda x: f"${x/1000:.1f}k")


# In[63]:


Movies['budget'] = Movies['budget'].apply(lambda x: f"${x/1000:.1f}k")              


# In[ ]:




