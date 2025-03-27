#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.isna().sum()


# In[7]:


df['Votes']=pd.to_numeric(df['Votes'],errors="coerce")
df['Aggregate rating']=pd.to_numeric(df['Aggregate rating'],errors="coerce")


# In[18]:


highest_votes=df.loc[df['Votes'].idxmax()]
print("\nRestaurant with Highest Votes:\n",highest_votes)


# In[14]:


df_non_zero_votes=df[df['Votes']>0]


# In[17]:


if not df_non_zero_votes.empty:
    lowest_votes=df_non_zero_votes.loc[df_non_zero_votes['Votes'].idxmin()]
    print("\nRestaurant with Lowest Votes:\n",lowest_votes)
else:
    print("No Restaurants with non zero votes find")


# In[20]:


plt.figure(figsize=(10,5))
sns.scatterplot(x=df["Aggregate rating"],y=df["Votes"])
plt.xlabel('Restaurant Rating')
plt.ylabel('Votes')
plt.title("Votes vs Rating")


# In[28]:


corre_matrix=df[["Votes","Aggregate rating"]].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corre_matrix,annot=True,cmap='coolwarm',fmt=".2f")
plt.title("Correlation Between Votes and Ratings")


# In[22]:


from scipy.stats import pearsonr


# In[34]:


corr,p_value=pearsonr(df["Votes"].dropna(),df["Aggregate rating"].dropna())
alpha=0.05
print(f"\nPearson Correlation Coefficient:{corr}")
print(f"p_Value:{p_value}")


# In[36]:


if p_value<alpha:
    print("Statistically Significant Correlation Found")
else:
    print("No Correlat")


# In[ ]:




