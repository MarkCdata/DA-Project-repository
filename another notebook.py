#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[24]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[25]:


Movies.drop(Movies[Movies['budget'] == 0.0].index, inplace = True)
Movies.drop(Movies[Movies['revenue'] == 0.0].index, inplace = True)


# In[26]:


Movies['budget'] = Movies['budget'].apply(lambda x: f"${x/1000000:.1f}m") 
Movies['revenue'] = Movies['revenue'].apply(lambda x: f"${x/1000000:.1f}m") 


# In[ ]:





# In[27]:


Movies.head(100)


# In[32]:


Movies.drop(Movies[Movies['revenue'] == 0.0].index, inplace = True)


# In[33]:


Movies.head(100)


# In[30]:


Movies.info()


# In[39]:


Movies.to_datetime(Movies['release_date'], dayfirst=False)


# In[ ]:




