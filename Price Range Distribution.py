#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Dataset .csv")


# In[5]:


df.info()


# In[16]:


len(df)


# In[24]:


Price_Count=df["Price range"].value_counts()
total_restaurants=len(df)


# In[27]:


price_percentages=(Price_Count/total_restaurants)*100


# In[29]:


print(price_percentages)


# In[34]:


plt.figure(figsize=(8,4))
plt.bar(Price_Count.index,Price_Count.values,color=['green','blue','red','pink'])


# In[ ]:




