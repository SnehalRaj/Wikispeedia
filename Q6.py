#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'paths_finished.tsv',sep='\t',names=['hashedIpAddress','timestamp','durationInSec','path','rating'])


# In[3]:


article_id = pd.read_csv('article-ids.csv')


# In[4]:


paths = []

for i in range(len(df)):
    paths.append((df.path[i]).split(';'))


# In[5]:


paths


# In[6]:


path = "wikispeedia_paths-and-graph/"
f = open(path+'shortest-path-distance-matrix.txt', 'r')

content = f.read()

ls = content.split('\n')

ls


# In[7]:


no_back = {}
back = {}
cnt=0
for i in range(len(paths)):
    
    source = (paths[i])[0]
    dest = (paths[i])[-1]
    source_id = (article_id.loc[article_id['article'] == source]).index.values.astype(int)[0]
    dest_id = (article_id.loc[article_id['article'] == dest]).index.values.astype(int)[0]
    if (ls[source_id][dest_id])!='_' and (ls[source_id][dest_id])!='0':
        shortest_path = int(ls[source_id][dest_id])
        human_path_backlink = len(paths[i]) - 1
        back_link_count=0
        for j in paths[i]:
            if(j=='<'):
                back_link_count+=1
        human_path_no_backlink = len(paths[i]) - 1 - 2*back_link_count
        ratio1 = round(human_path_no_backlink/shortest_path,2)
        ratio2 = round(human_path_backlink/shortest_path,2)
        no_back[cnt] = {'Human_Path_Length':human_path_no_backlink,'Shortest_Path_Length':shortest_path,'Ratio':ratio1}
        back[cnt] = {'Human_Path_Length':human_path_backlink,'Shortest_Path_Length':shortest_path,'Ratio':ratio2}
        cnt+=1


# In[8]:


df_no_back = pd.DataFrame.from_dict(no_back, "index")
df_back = pd.DataFrame.from_dict(back, "index")


# In[9]:


df_no_back.to_csv('finished-paths-no-back.csv',index=False)
df_back.to_csv('finished-paths-back.csv',index=False)


# In[ ]:





# In[ ]:




