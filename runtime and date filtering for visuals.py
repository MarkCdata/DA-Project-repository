#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[4]:


Movies.info()


# In[5]:


Movies.drop(Movies[Movies['budget'] == 0.0].index, inplace = True)
Movies.drop(Movies[Movies['revenue'] == 0.0].index, inplace = True)


# In[6]:


Movies.info()


# In[14]:


Movies['release_date'] = pd.to_datetime(Movies['release_date'],dayfirst=True)


# In[16]:


Movies.head()


# In[17]:


plt.subplots(figsize=(10,5))

plt.plot(Movies['release_date'],Movies['revenue'])


plt.xlabel('Month/Year)')
plt.ylabel('Revenue')
plt.title('best time to relase Movie based on Revenue')


# In[22]:


filtered_Movies_runtime = Movies.loc[(Movies['runtime'] >= 10)
                     & (Movies['runtime'] < 180 )]


# In[18]:


sns.pairplot(Movies)


# In[23]:


sns.pairplot(filtered_Movies_runtime)


# In[24]:


filtered_Movies_runtime.sort_values(by='runtime', ascending=False)


# In[26]:


filtered_Movies = Movies.loc[(Movies['release_date'] >= '1999-12-31')
                     & (Movies['release_date'] < '2022-12-31')] 


# In[27]:


filtered_Movies.loc[(filtered_Movies['runtime'] >= 10)
                     & (filtered_Movies['runtime'] < 180 )]


# In[28]:


sns.pairplot(filtered_Movies)


# In[40]:


filtered_Movies.info()


# In[32]:


sns.catplot(x="genres", y="vote_average", hue="genres", height =10, palette="pastel",
            kind="box", dodge=False, data=filtered_Movies);


# In[36]:


sns.barplot(x= "budget", y= "release_date", data=filtered_Movies)


# In[41]:


Movies['year'] = Movies['release_date'].dt.year
Movies['month'] = Movies['release_date'].dt.month


# Movies.head()

# 

# In[43]:


Movies.head()


# In[46]:


Movies.info()


# In[52]:


Movies['year_month'] = pd.to_datetime(Movies['release_date'], format='%Y%m')


# In[53]:


Movies.info()


# In[54]:


Movies.head()


# In[ ]:




