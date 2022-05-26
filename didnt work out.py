#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime


# In[11]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[12]:


Movies['release_date'] = pd.to_datetime(Movies['release_date'],dayfirst=False)


# In[13]:


Movies.info()


# In[14]:


Movies['month_year'] = Movies['release_date'].dt.to_period('M')


# In[15]:


Movies.info()


# In[16]:


Movies.head()


# In[17]:


Movies_cleaned = pd.Movies.drop_duplicates(subset=['id'])
Movies.drop(Movies[Movies['budget'] == 0.0].index, inplace = True)
Movies.drop(Movies[Movies['revenue'] == 0.0].index, inplace = True)
Movies.drop("backdrop_path", inplace=True, axis=1)
Movies.drop("recommendations", inplace=True, axis=1)
Movies.drop("credits", inplace=True, axis=1)
Movies.drop("overview", inplace=True, axis=1)
Movies.drop("poster_path", inplace=True, axis=1)
Movies['budget'] = Movies['budget'].apply(lambda x: f"€{x/1000000:.1f}m") 
Movies['revenue'] = Movies['revenue'].apply(lambda x: f"€{x/1000000:.1f}m")
Movies['revenue'] = Movies['revenue'].str.replace('€', '')
Movies['budget'] = Movies['budget'].str.replace('€', '')
Movies['revenue'] = Movies['revenue'].str.replace('m', '')
Movies['budget'] = Movies['budget'].str.replace('m', '')

Movies[Movies["original_language"].str.contains("en")==True]
Movies.loc[(Movies['release_date'] >= '1999-12-31')
                     & (Movies['release_date'] < '2022-12-31')]


# In[ ]:


sns.barplot(x= "revenue", y= "month_year", data=Movies_cleaned)


# In[ ]:


Movies_cleaned.info()


# In[ ]:





# In[ ]:




