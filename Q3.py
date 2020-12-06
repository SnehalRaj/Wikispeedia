#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


article_id = pd.read_csv('article-ids.csv')
category_id = pd.read_csv('category-ids.csv')


# In[3]:


category_id


# In[4]:


path = "wikispeedia_paths-and-graph/"
categories = pd.read_csv(path+'categories.tsv',sep='\t',names=['article','category'])
categories


# In[5]:


article = pd.merge(categories, article_id, on='article')


# In[6]:


category = pd.merge(article,category_id,on='category')


# In[7]:


final =category.sort_values('id_x')


# In[8]:


final = (final[['id_x','id_y']]).reset_index(drop=True)


# In[9]:


final


# In[10]:


final_dict = dict(zip(final.id_x, final.id_y))


# In[11]:


final_dict['A1212']


# In[12]:


len(final)


# In[13]:


(final.id_x)[0]


# In[14]:


new_dict = {}
cnt=0
cnt2=0
for i in range(len(final)):
    name =  'A'+str(cnt+1).zfill(4)
    name2 = 'A'+str(cnt+2).zfill(4)
    if ((final.id_x)[i]==name or (final.id_x)[i]==name2):
        cat = (final.id_y)[i]
        if (final.id_x)[i]==name:
            new_dict[cnt2] = {'Article_ID':name , 'Category_ID':cat}
        else:
            new_dict[cnt2] = {'Article_ID':name2 , 'Category_ID':cat}
            cnt+=1
        cnt2+=1
        
    else:
        print((final.id_x)[i])
        cat = (final.id_y)[i]
        new_dict[cnt2] = {'Article_ID':name2 , 'Category_ID':cat}
        cnt+=1
        cnt2+=1
        
        


# In[15]:


pd.DataFrame.from_dict(new_dict,"index")


# In[16]:


# check


# In[ ]:




