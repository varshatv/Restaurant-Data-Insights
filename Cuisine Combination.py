#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[4]:


df.info()


# In[5]:


common_cuisines=df["Cuisines"].value_counts()


# In[6]:


common_cuisines


# In[7]:


average_rating=df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)


# In[8]:


average_rating.head()


# In[9]:


top_combinations=average_rating.head(10)
sns.barplot(x=top_combinations.index,y=top_combinations.values,palette='coolwarm')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine Combination')
plt.title('Top 10 Highest Rated Cuisine Combination')
plt.show()


# In[ ]:




