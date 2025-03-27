#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import statsmodels.api as sm


# In[34]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[35]:


df.columns


# In[36]:


df['Price range'].unique()


# In[37]:


df['Has Table booking'].unique()


# In[38]:


df['Has Online delivery'].unique()


# In[40]:


df['Has Table booking']=df['Has Table booking'].map({"Yes":1,"No":0})
df['Has Online delivery']=df['Has Online delivery'].map({"No":0,"Yes":1})


# In[41]:


df['Has Online delivery'].unique()


# In[42]:


sns.countplot(x="Price range",data=df,palette="coolwarm")
plt.title("Count of Restaurants by Price Range")


# In[43]:


service_availability=df.groupby('Price range')[['Has Table booking','Has Online delivery']].mean()
print(service_availability)


# In[44]:


service_availability.plot(kind="bar",stacked=True,color=("blue","red"))
plt.ylabel("Percentage")
plt.title("Percentage of Restaurants offering Services by Price Range")


# In[45]:


tablebooking_cont=pd.crosstab(df["Price range"],df["Has Table booking"])
onlinedelivery_cont=pd.crosstab(df["Price range"],df["Has Online delivery"])


# In[46]:


print(tablebooking_cont)


# In[53]:


chi2_tb,p_tb,_,_=chi2_contingency(tablebooking_cont)
chi2_od,p_od,_,_=chi2_contingency(onlinedelivery_cont)


# In[54]:


print(f"Chi2 Test for Table Booking:p_value={p_tb}")
print(f"Chi2 Test for Online Delivery:p_value={p_od}")


# In[55]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[56]:


df.columns


# In[60]:


X=df[['Price range']]
y_tb=df['Has Table booking']
y_od=df['Has Online delivery']


# In[61]:


X_train,X_test,y_tb_train,y_tb_test=train_test_split(X,y_tb,test_size=0.2,random_state=42)
X_train,X_test,y_od_train,y_od_test=train_test_split(X,y_od,test_size=0.2,random_state=42)


# In[62]:


model_tb=LogisticRegression()
model_tb.fit(X_train,y_tb_train)
pred_tb=model_tb.predict(X_test)


# In[63]:


model_od=LogisticRegression()
model_od.fit(X_train,y_od_train)
pred_od=model_od.predict(X_test)


# In[68]:


print(f"Table Booking Prediction Accuracy:{accuracy_score(y_tb_test,pred_tb)}")
print(f"Online Delivery Prediction Accuracy:{accuracy_score(y_od_test,pred_od)}")


# In[ ]:




