#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install wordCloud')


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import re


# In[4]:


df=pd.read_csv(r"C:\Users\Uer\Downloads\Cognifyz\Questions\Dataset .csv")


# In[5]:


df.info()


# In[4]:


df.head()


# In[6]:


df=df[['Rating text','Aggregate rating']].dropna()


# In[7]:


nltk.download('stopwords')
stop_words=set(stopwords.words('english'))


# In[ ]:





# In[8]:


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


# In[9]:


df['Cleaned_Rating']=df['Rating text'].apply(clean_text)


# In[14]:


from collections import Counter


# In[15]:


all_words=' '.join(df['Cleaned_Rating']).split()


# In[16]:


word_frequent= Counter(all_words)


# In[17]:


print("Most Common Words in Reviews")
print(word_frequent.most_common(20))


# In[22]:


positive_review = ' '.join(df[df['Aggregate rating']>4]['Cleaned_Rating'])
world_cloud_positive = WordCloud(width=800,height=400,background_color='white').generate(positive_review)


# In[27]:


negtive_review = ' '.join(df[df['Aggregate rating']<2]['Cleaned_Rating'])
world_cloud_negtive = WordCloud(width=800,height=400,background_color='black').generate(negtive_review)


# In[24]:


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(world_cloud_positive,interpolation='bilinear')
plt.axis('off')
plt.title("Common Positive Word")


# In[28]:


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(world_cloud_negtive,interpolation='bilinear')
plt.axis('off')
plt.title("Common Negetive Word")


# In[29]:


df['Review Length']=df['Rating text'].apply(lambda x : len(x.split()))


# In[30]:


avg_review_len = df['Review Length'].mean()


# In[34]:


print('Average Review Length:' ,{avg_review_len})


# In[38]:


plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Review Length'],y=df['Aggregate rating'])
plt.xlabel('Review Length')
plt.ylabel('Rating')
plt.title('Review Length vs Rating')


# In[40]:


correlation = df[['Review Length','Aggregate rating']].corr().iloc[0,1]


# In[41]:


print('Correlation between Review Length and Rating:',{correlation})


# In[ ]:




