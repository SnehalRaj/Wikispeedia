#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


path = "wikispeedia_paths-and-graph/"
f = open(path+'shortest-path-distance-matrix.txt', 'r')

content = f.read()

ls = content.split('\n')

ls


# In[3]:


(ls[0])[4396]


# In[4]:


df = pd.DataFrame(columns=['from','to'])


# In[5]:


df


# In[6]:


dic = {}
cnt=0
for i in range(4604):
    for j in range(4604):
        name1 = 'A'+str(i+1).zfill(4)
        if (ls[i])[j]=='1':
            name2 = 'A'+str(j+1).zfill(4)
            dic[cnt] = {'from': name1, 'to':name2}
            cnt+=1


# In[7]:


df = pd.DataFrame.from_dict(dic, "index")


# In[8]:


df.to_csv('edges.csv',index=False)


# In[ ]:




