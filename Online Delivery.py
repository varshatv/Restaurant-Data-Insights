#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Dataset .csv")


# In[6]:


total_restaurants=len(df)
online_delivery=df["Has Online delivery"].value_counts()


# In[9]:


onlineDelivery_Percentage=(online_delivery/total_restaurants)*100


# In[11]:


print(onlineDelivery_Percentage)


# In[13]:


print(online_delivery)


# In[51]:


has_onlinedelivery=df[df["Has Online delivery"]=="Yes"]


# In[34]:


print(has_onlinedelivery)


# In[23]:


no_onlinedelivery=df[df["Has Online delivery"]=="No"]


# In[24]:


print(no_onlinedelivery)


# In[47]:


average_rating=df.groupby("Has Online delivery")["Votes"].mean()


# In[48]:


print(average_rating)


# In[ ]:




