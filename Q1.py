#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'articles.tsv',names=['article'])


# In[3]:


index = [0]*4604


# In[4]:


for i in range(4604):
    index[i] = 'A'+str(i+1).zfill(4)


# In[5]:


index


# In[6]:


df['id'] = (index)


# In[7]:


# del df['index']


# In[8]:


df


# In[9]:


df = df.set_index(['id'])


# In[10]:


df


# In[11]:


df.to_csv('article-ids.csv')


# In[12]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




