#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[3]:


df.info()


# In[11]:


chain_count=df['Restaurant Name'].value_counts()
restaurant_chains=chain_count[chain_count> 1].index


# In[13]:


chain_df=df[df['Restaurant Name'].isin(restaurant_chains)]


# In[15]:


chain_df.info()


# In[24]:


chain_rating=chain_df.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False)


# In[25]:


print ("Top 10 Highest Rated Restaurant:")
print(chain_rating.head(10))


# In[26]:


chain_popularity=chain_df.groupby('Restaurant Name')['Votes'].sum().sort_values(ascending=False)


# In[27]:


print("Top 10 Most Popular Chains:")
print(chain_popularity.head(10))


# In[ ]:




