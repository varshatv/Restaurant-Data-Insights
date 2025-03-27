#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Dataset .csv")


# In[3]:


y=df["City"]


# In[4]:


y


# In[5]:


city_counts=df.groupby("City")["Restaurant ID"].nunique()


# In[6]:


print(city_counts)


# In[9]:


top_city=city_counts.sort_values(ascending=False).head()


# In[10]:


print(top_city)


# In[16]:


average_rating=df.groupby("City")["Votes"].mean()


# In[17]:


average_rating=average_rating.sort_values(ascending=False)


# In[18]:


print(average_rating)


# In[ ]:




