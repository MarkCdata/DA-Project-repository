#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[10]:


Movies.shape


# In[11]:


Movies.info()


# In[12]:


Movies.dtypes


# In[13]:


Movies.isnull().sum()


# In[14]:


Movies.head(50)


# In[15]:


#### This database comes from The Movie Database and contains 780,837 titles across 20 coloumns. 
#The popularity coloumn is rated via The movie Databases own algorithim based on the below parameters
#Number of votes for the day
#Number of views for the day
#Number of users who marked it as a "favourite" for the day
#Number of users who added it to their "watchlist" for the day
#Release date
#Number of total votes
#Previous days score


# In[16]:


Movies.isnull().sum()


# In[17]:


Movies_in_english = Movies[Movies["original_language"].str.contains("en")==True]


# In[18]:


Movies_in_english.info()


# In[19]:


Movies_in_english.isnull().sum()


# In[20]:


###2 dataframes now, Movies and Movies_in_english


# In[21]:


Movies_in_english.head(500)


# In[22]:


Movies_in_english.drop(Movies_in_english[Movies_in_english['budget'] == 0.0].index, inplace = True)


# In[23]:


Movies_in_english.shape


# In[24]:


Movies_in_english.head(500)


# In[25]:


Movies_in_english.drop(Movies_in_english[Movies_in_english['budget'] == 0].index, inplace = True)

Movies_in_english.shape


# In[26]:


Movies_in_english.head(15)


# In[27]:


Movies_in_english.index


# In[28]:


Movies_in_english.reset_index()


# In[29]:


Movies_in_english.iloc[:, 0]


# In[ ]:





# In[ ]:





# In[30]:


#Movies_in_english is the final version that has been cleaned and indexed and ready to try a few visuals!


# In[ ]:





# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


Movies.head(10)


# In[33]:


Movies_in_english.head()


# In[34]:


Movies_in_english.info()


# In[35]:


finance = Movies_in_english[['id','title','popularity','release_date','budget','revenue','runtime']]


# In[36]:


finance.head(10)


# In[37]:


finance.isnull().sum()


# In[38]:


finance.shape


# In[39]:


finance_clean=finance.dropna()


# In[40]:


finance_clean.isnull().sum()


# In[41]:


finance_clean.shape


# In[42]:






# In[ ]:

<<<<<<< HEAD




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:

=======
>>>>>>> parent of ede5903 (Ready for visuals)



