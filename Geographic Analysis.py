#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[4]:


df.info()


# In[5]:


plt.figure(figsize=(10,6))
sns.scatterplot(x=df['Longitude'],y=df['Latitude'],alpha=0.5,edgecolor='b')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations")


# In[8]:


plt.figure(figsize=(10,6))
sns.kdeplot(x=df['Longitude'],y=df['Latitude'],cmap="Greens",fill=True,levels=50)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Density")


# In[ ]:




