#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[4]:


Movies.shape


# In[5]:


Movies.info()


# In[6]:


Movies.dtypes


# In[7]:


Movies.isnull().sum()


# In[8]:


Movies.head(50)


# In[9]:


#### This database comes from The Movie Database and contains 780,837 titles across 20 coloumns. 
#The popularity coloumn is rated via The movie Databases own algorithim based on the below parameters
#Number of votes for the day
#Number of views for the day
#Number of users who marked it as a "favourite" for the day
#Number of users who added it to their "watchlist" for the day
#Release date
#Number of total votes
#Previous days score


# In[10]:


Movies.isnull().sum()


# In[11]:


Movies_in_english = Movies[Movies["original_language"].str.contains("en")==True]


# In[12]:


Movies_in_english.info()


# In[13]:


Movies_in_english.isnull().sum()


# In[14]:


###2 dataframes now, Movies and Movies_in_english


# In[15]:


Movies_in_english.head(500)


# In[16]:


Movies_in_english.drop(Movies_in_english[Movies_in_english['budget'] == 0.0].index, inplace = True)


# In[17]:


Movies_in_english.shape


# In[18]:


Movies_in_english.head(5)


# In[19]:


Movies_in_english.dropna(subset = ['budget', 'release_date',])


# In[20]:


Movies_in_english.isnull()


# In[21]:


Movies_in_english.index


# In[22]:


Movies_in_english.reset_index()


# In[23]:


Movies_in_english.iloc[:, 0]


# In[ ]:





# In[ ]:





# In[24]:


#Movies_in_english is the final version that has been cleaned and indexed and ready to try a few visuals!


# In[ ]:





# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[26]:


Movies.head(10)


# In[27]:


Movies_in_english.head()


# In[28]:


Movies_in_english.info()


# In[29]:


finance = Movies_in_english[['id','title','popularity','release_date','budget','revenue','runtime']]


# In[30]:


finance.head(10)


# In[31]:


finance.isnull().sum()


# In[32]:


finance.shape


# In[33]:


finance_clean=finance.dropna()


# In[34]:


finance_clean.isnull().sum()


# In[35]:


finance_clean.shape


# In[38]:


finance_clean.info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




