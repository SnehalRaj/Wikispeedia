#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'paths_unfinished.tsv',sep='\t',names=['hashedIpAddress','timestamp','durationInSec','path','target','type'])

df
paths_u = []

for i in range(len(df)):
    paths_u.append((df.path[i]).split(';'))


# In[3]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'paths_finished.tsv',sep='\t',names=['hashedIpAddress','timestamp','durationInSec','path','rating'])

paths = []

for i in range(len(df)):
    paths.append((df.path[i]).split(';'))


# In[4]:


without_back_u = []
for i in range(len(paths_u)):
    array = paths_u[i]
    update = []
    for j in range(len(array)):
        if(array[j]!='<'):
            update.append(array[j])
        else:
            del update[-1]
    without_back_u.append(update)


# In[5]:


without_back = []
for i in range(len(paths)):
    array = paths[i]
    update = []
    for j in range(len(array)):
        if(array[j]!='<'):
            update.append(array[j])
        else:
            del update[-1]
    without_back.append(update)


# In[6]:


article_id = pd.read_csv('article-ids.csv')
article_id.head()


# In[7]:


article_id_map = {}
for i in range(len(article_id)):
    index = str(article_id['id'][i])
    article = article_id['article'][i]
    article_id_map[article] = index
    
    
    


# In[8]:


no_back_u = []
for i in range(len(without_back_u)):
    row  = []
    for j in without_back_u[i]:
        row.append(article_id_map[j])
    no_back_u.append(row)


# In[9]:


no_back = []
for i in range(len(without_back)):
    row  = []
    for j in without_back[i]:
        row.append(article_id_map[j])
    no_back.append(row)


# In[10]:


no_back


# In[11]:


import csv

with open('article-categories.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
data = data[1:]
print(data)


# In[12]:


category_id = pd.read_csv('category-ids.csv')
category_id.head()

category_id_map = {}
category_id_rev_map = {}
for i in range(len(category_id)):
    index = str(category_id['id'][i])
    category = category_id['category'][i]
    category_id_map[index] = category
    category_id_rev_map[category] = index
category_id_map    

    


# In[13]:


df2 = pd.read_csv('category-pairs.csv')
col_from = df2['from']


# In[14]:


parents = {}
for i in category_id_map.keys():
    parents[i] = []
    name = category_id_map[i]
    for j in category_id_map.values():
#         print(j)
        if (name.startswith(j)):
            parents[i].append(category_id_rev_map[j])
parents


# In[15]:


category_pairs_unfinished = [[0]*146]*146
category_pairs_finished = [[0]*146]*146


# In[16]:


# category_pairs


# In[17]:


col_to = df2['to']


# In[18]:


u =df2['unfinished']


# In[19]:


u


# In[20]:


for i in range( len(no_back_u)):
    source = (no_back_u[i])[0]
    dest = (no_back_u[i])[-1]
    s_id = int(source[1:])-1
    d_id = int(dest[1:])-1
    s_cats = (data[s_id])[1:]
    d_cats = (data[d_id])[1:]
    s = []
    d = []
    for cat in s_cats:
        for elem in parents[cat]:
            s.append(elem)
    for cat in d_cats:
        for elem in parents[cat]:
            d.append(elem)
    s= set(s)
    d= set(d)
    for start in s:
        for end in d:
            category_pairs_unfinished[int(start[1:])-1][int(end[1:])-1]+=1


# In[21]:


for i in range( len(no_back)):
    source = (no_back[i])[0]
    dest = (no_back[i])[-1]
    s_id = int(source[1:])-1
    d_id = int(dest[1:])-1
    s_cats = (data[s_id])[1:]
    d_cats = (data[d_id])[1:]
    s = []
    d = []
    for cat in s_cats:
        for elem in parents[cat]:
            s.append(elem)
    for cat in d_cats:
        for elem in parents[cat]:
            d.append(elem)
    s= set(s)
    d= set(d)
    for start in s:
        for end in d:
            category_pairs_finished[int(start[1:])-1][int(end[1:])-1]+=1


# In[22]:


category_pairs_finished


# In[23]:


f = df2['finished']


# In[24]:


col_from = []
col_to = []
u = []
f = []
for i in range(146):
    for j in range(146):
        col_from.append('C'+str(i+1).zfill(4))
        col_to.append('C'+str(j+1).zfill(4))
        u.append(category_pairs_unfinished[i][j])
        f.append(category_pairs_finished[i][j])


# In[25]:


df = pd.DataFrame(columns=['from','to','unfinished','finished'])


# In[26]:


df2 = pd.read_csv('category-pairs.csv')


# In[27]:


df['from'] = col_from


# In[28]:


df['to'] = col_to


# In[29]:


df['unfinished'] = u


# In[30]:


df['finished'] = f


# In[31]:


df.to_csv('category-pairs.csv',index=False)


# In[ ]:




