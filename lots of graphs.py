#!/usr/bin/env python
# coding: utf-8

# In[116]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime


# In[117]:


filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")
Movies.head()


# In[118]:


Movies.info()


# In[119]:


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
Movies['release_date'] = pd.to_datetime(Movies['release_date'],dayfirst=False)
Movies['budget'] = Movies['budget'].astype('float')
Movies['revenue'] = Movies['revenue'].astype('float')


# In[120]:


Movies.info()


# In[121]:


Movies['release_date'] =Movies['release_date'].dt.strftime('%m/%Y')


# In[122]:


Movies['release_date'] = pd.to_datetime(Movies['release_date'],yearfirst=False)


# In[123]:


Movies.info()


# In[124]:


Movies.head()


# In[125]:


Movies_2000s = Movies.loc[(Movies['release_date'] >= '1999-12-31')
                     & (Movies['release_date'] < '2022-12-31')]


# In[126]:


filtered_Movies = Movies_2000s.loc[(Movies_2000s['runtime'] >= 45)
                     & (Movies_2000s['runtime'] < 250)] 


# In[127]:


filtered_Movies_cash = filtered_Movies.loc[(filtered_Movies['budget'] > 45)
                                        & (filtered_Movies['budget'] < 250)] 
                   


# In[128]:


filtered_Movies_cash.info()


# In[129]:


filtered_Movies.info()


# In[130]:


plt.scatter(filtered_Movies_cash['budget'], filtered_Movies_cash['revenue'], s=2)


# In[131]:


filtered_Movies_cash.plot.scatter('budget', 'revenue', s=4)


# In[132]:


sns.scatterplot(x='revenue',y='vote_average', data=filtered_Movies_cash, hue='popularity', size='budget')


# In[133]:


filtered_Movies_cash.groupby(['budget','revenue','runtime']).mean()


# In[134]:


filtered_Movies_cash.describe(include= "all",datetime_is_numeric=True)


# In[ ]:





# In[135]:



sns.scatterplot(x='release_date',y='revenue', data=filtered_Movies_cash, hue='runtime')


# In[136]:


sns.set(rc={'figure.figsize':(11.7,8.5)})
sns.scatterplot(x='release_date',y='revenue', data=filtered_Movies_cash, hue='runtime')


# In[137]:


filtered_Movies_cash.sort_values(by='revenue', ascending=False).head(20)


# In[138]:


Movies_cleaned_cash = filtered_Movies_cash.drop_duplicates(subset=['id'])


# In[139]:


Movies_cleaned_cash.sort_values(by='revenue', ascending=False).head(20)


# In[140]:


sns.set(rc={'figure.figsize':(11.7,10)})
sns.scatterplot(x='release_date',y='revenue', data=Movies_cleaned_cash, hue='runtime')


# In[141]:


Movies_cleaned_cash.sort_values(by='revenue', ascending=False).head(20)


# In[142]:


sns.set(rc={'figure.figsize':(15.7,6)})
sns.lineplot(x = "release_date", y = "revenue", data = Movies_cleaned_cash)
plt.show()


# In[143]:


filtered_Movies_00to10 = filtered_Movies.loc[(filtered_Movies['release_date'] >= '1999-12-31')
                                        & (filtered_Movies['release_date'] < '2009-12-31')]
filtered_Movies_10to21 = filtered_Movies.loc[(filtered_Movies['release_date'] > '2009-12-31')
                                        & (filtered_Movies['release_date'] < '2021-12-31')]
filtered_Movies_10to15 = filtered_Movies.loc[(filtered_Movies['release_date'] > '2009-12-31')
                                        & (filtered_Movies['release_date'] < '2014-12-31')]


# In[144]:


sns.set(rc={'figure.figsize':(15.7,6)})
sns.lineplot(x = "release_date", y = "revenue", data = filtered_Movies_00to10)
plt.show()


# In[145]:


sns.set(rc={'figure.figsize':(15.7,6)})
sns.lineplot(x = "release_date", y = "revenue", data = filtered_Movies_10to21)
plt.show()


# In[146]:


sns.set(rc={'figure.figsize':(15.7,6)})
sns.lineplot(x = "release_date", y = "revenue", data = filtered_Movies_10to15)
plt.show()


# In[147]:


#There appears to be a lull in revenue generated in approx the 1st quater of each year and a massive jump in revenue generated for movies release Easter/Summer/halloween/christmas


# In[148]:


filtered_Movies_10to15.info()


# In[149]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

filtered_Movies_10to15['genres'].value_counts().plot(kind='pie', subplots=True,autopct='%1.1f%%', figsize=(8, 8), colors=colors)
plt.title('Pie Chart - ')


# In[150]:


cmap = plt.get_cmap('Pastel1')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

filtered_Movies['genres'].value_counts().plot(kind='pie', subplots=True,autopct='%1.1f%%', figsize=(8, 8), colors=colors)
plt.title('Pie Chart - ')


# In[151]:


plt.figure(1, figsize=(10,10))
filtered_Movies['vote_average'].value_counts().plot.pie(autopct="%1.1f%%")


# In[159]:


filtered_Movies["runtime"].value_counts()


# In[160]:


filtered_Movies["runtime"].value_counts().plot.pie(autopct='%1.1f%%',figsize=(10,10))
plt.title('Top 10 runtime of Movies')


# In[161]:


filtered_Movies["runtime"].mean()


# In[162]:


filtered_Movies["revenue"].mean()


# In[163]:


filtered_Movies["budget"].mean()


# In[164]:


profit = 72.9 - 25.9
print(profit)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




