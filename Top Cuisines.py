#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[4]:


df.head


# In[5]:


df.info()


# In[6]:


df.isna().sum()


# In[7]:


y=df["Cuisines"]


# In[8]:


y


# In[9]:


df["Cuisines"]=df["Cuisines"].str.split(",")


# In[10]:


df=df.explode("Cuisines")


# In[11]:


cuisine_count=df["Cuisines"].value_counts()
top_three_cuisines=cuisine_count.head(3)
print(top_three_cuisines)


# In[12]:


total_restaurants=df["Restaurant ID"].nunique()
cuisine_counts=df.groupby("Cuisines")["Restaurant ID"].nunique()
cuisine_percent=(cuisine_counts/total_restaurants)*100
top_three_cuisine=cuisine_percent.sort_values(ascending=False).head(3)


# In[13]:


print(total_restaurants)


# In[14]:


print(cuisine_counts)


# In[15]:


print(cuisine_count)


# In[16]:


print(cuisine_percent)


# In[17]:


print(top_three_cuisine)


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


plt.figure(figsize=(8,5))
sns.barplot(x=top_three_cuisine.index,y=top_three_cuisine.values,palette='coolwarm')


# In[ ]:




