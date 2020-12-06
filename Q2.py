#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'categories.tsv',sep='\t',names=['article','category'])


# In[3]:


categories = df['category']


# In[4]:


main = [0]*len(categories)


# In[5]:


for i in range(len(categories)):
    main[i] = categories[i].split('.')


# In[6]:


len(main)


# In[7]:


len(categories)


# In[8]:


max_len = 1
for array in main:
    if len(array)>max_len:
        max_len = len(array)


# In[9]:


max_len


# In[10]:


cat = [[],[],[],[]]
maincat = [[],[],[],[]]


# In[11]:


for i in range(4):
    for j in range(len(main)):
        if (i<len(main[j])):
            name = (main[j])[0]
            for loop in range(1,i+1):
                name = name+"."+(main[j])[loop]
            if name not in maincat[i]:
#                 cat[i].append((main[j])[i])
#                 if (main[j])[i] == 'Artists':
#                     print(name)
                maincat[i].append(name)


# In[12]:


maincat[0] = 'subject'


# In[13]:


maincat


# In[14]:


main_cat = ['subject']
for i in range(1,4):
    a = maincat[i]
    a.sort()
    main_cat = main_cat + a


# In[15]:


main_cat


# In[16]:


index = [0]*len(main_cat)
for i in range(len(main_cat)):
    index[i] = 'C'+str(i+1).zfill(4)


# In[17]:


data = {'id':index ,'category':main_cat}


# In[18]:


cat_df = pd.DataFrame(data,columns=['id','category'])


# In[19]:


cat_df


# In[20]:


cat_df.to_csv('category-ids.csv',index=False)


# In[21]:


cat


# In[22]:


cat_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




