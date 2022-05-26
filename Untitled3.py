#!/usr/bin/env python
# coding: utf-8

# In[78]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime 


# In[79]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[80]:


Movies['release_date'] = pd.to_datetime(Movies['release_date'],dayfirst=True)


# In[81]:


Movies.drop(Movies[Movies['budget'] == 0.0].index, inplace = True)
Movies.drop(Movies[Movies['revenue'] == 0.0].index, inplace = True)
Movies['budget'] = Movies['budget'].apply(lambda x: f"€{x/1000000:.1f}m") 
Movies['revenue'] = Movies['revenue'].apply(lambda x: f"€{x/1000000:.1f}m") 


# In[82]:


Movies.head(50)


# In[83]:


Movies.info()


# In[84]:


Movies['month_year'] = Movies['release_date'].dt.to_period('M')


# In[85]:


Movies.index


# In[86]:


filtered_Movies = Movies.loc[(Movies['release_date'] >= '1999-12-31')
                     & (Movies['release_date'] < '2022-12-31')]


# In[87]:


filtered_Movies.head()


# In[88]:


filtered_Movies_eng = Movies[Movies["original_language"].str.contains("en")==True]
filtered_Movies_fr = Movies[Movies["original_language"].str.contains("fr")==True]
filtered_Movies_es = Movies[Movies["original_language"].str.contains("es")==True]


# In[89]:


filtered_Movies_es.head(50)


# In[90]:


filtered_Movies_fr.info()


# In[91]:


sns.scatterplot(x='release_date',y='runtime', data=filtered_Movies, size='revenue')


# In[92]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

filtered_Movies_eng['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(10, 10), colors=colors)
plt.title('Pie Chart - Number of Titles by genres')


# In[93]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

filtered_Movies_fr['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(10, 10), colors=colors)
plt.title('Pie Chart - Number of Titles by genres FR')


# In[94]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

filtered_Movies_es['genres'].value_counts().plot(kind='pie', subplots=True, autopct='%1.0f%%', figsize=(10, 10), colors=colors)
plt.title('Pie Chart - Number of Titles by genres ES')


# In[95]:


plt.subplots(figsize=(10,5))

plt.plot(Movies['month_year'],Movies['revenue'])


plt.xlabel('Month/Year)')
plt.ylabel('Revenue')
plt.title('best time to relase Movie based on Revenue')


# In[96]:


Movies.sort_values(by='runtime', ascending=False)


# In[97]:


filtered_Movies_runtime = Movies.loc[(Movies['runtime'] >= 10)
                     & (Movies['runtime'] < 400 )]


# In[98]:


filtered_Movies_runtime.sort_values(by='runtime', ascending=False)


# In[99]:


filtered_Movies_runtime['revenue'].apply(type).value_counts()


# In[105]:


filtered_Movies_runtime = pd.to_numeric(filtered_Movies_runtime.replace('[^0-9\.-]''',regex=True))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




