#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


for col in check.columns: 
    print( "df[ \' " + col + "\'] = ") 

no_back_data = pd.read_csv('finished-paths-no-back.csv')

no_back_data.head()

equal = 0
larger = [0]*10
large = 0
for i in range(len(no_back_data)):
    h_length = (no_back_data['Human_Path_Length'])[i]
    s_length = (no_back_data['Shortest_Path_Length'])[i]
    if(h_length == s_length):
        equal+=1
    else:
        diff = h_length - s_length
        if(diff>10):
            large+=1
        else:
            larger[diff-1]+=1
            

total = len(no_back_data)
larger[0]

df = pd.DataFrame(columns=[ 'Equal_Length' ,  'Larger_by_1' , 'Larger_by_2' , ' Larger_by_3' , ' Larger_by_4' , ' Larger_by_5' , 'Larger_by_6' , 'Larger_by_7' , 'Larger_by_8' , 'Larger_by_9' , 'Larger_by_10' , 'Larger_by_more_than_10'  ])

df[ 'Equal_Length'] = [equal/total]
df[ 'Larger_by_1'] = [larger[0]/total]
df[ 'Larger_by_2'] = [larger[1]/total]
df[ 'Larger_by_3'] = [larger[2]/total]
df[ 'Larger_by_4'] = [larger[3]/total]
df[ 'Larger_by_5'] = [larger[4]/total]
df[ 'Larger_by_6'] = [larger[5]/total]
df[ 'Larger_by_7'] = [larger[6]/total]
df[ 'Larger_by_8'] = [larger[7]/total]
df[ 'Larger_by_9'] = [larger[8]/total]
df[ 'Larger_by_10'] = [larger[9]/total]
df[ 'Larger_by_more_than_10'] = [large/total]

df

df.to_csv('percentage-paths-no-back.csv',index=False)


# In[43]:



no_back_data = pd.read_csv('finished-paths-back.csv')

no_back_data.head()

equal = 0
larger = [0]*10
large = 0
for i in range(len(no_back_data)):
    h_length = (no_back_data['Human_Path_Length'])[i]
    s_length = (no_back_data['Shortest_Path_Length'])[i]
    if(h_length == s_length):
        equal+=1
    else:
        diff = h_length - s_length
        if(diff>10):
            large+=1
        else:
            larger[diff-1]+=1
            

total = len(no_back_data)
larger[0]

df = pd.DataFrame(columns=[ 'Equal_Length' ,  'Larger_by_1' , 'Larger_by_2' , ' Larger_by_3' , ' Larger_by_4' , ' Larger_by_5' , 'Larger_by_6' , 'Larger_by_7' , 'Larger_by_8' , 'Larger_by_9' , 'Larger_by_10' , 'Larger_by_more_than_10'  ])

df[ 'Equal_Length'] = [equal/total]
df[ 'Larger_by_1'] = [larger[0]/total]
df[ 'Larger_by_2'] = [larger[1]/total]
df[ 'Larger_by_3'] = [larger[2]/total]
df[ 'Larger_by_4'] = [larger[3]/total]
df[ 'Larger_by_5'] = [larger[4]/total]
df[ 'Larger_by_6'] = [larger[5]/total]
df[ 'Larger_by_7'] = [larger[6]/total]
df[ 'Larger_by_8'] = [larger[7]/total]
df[ 'Larger_by_9'] = [larger[8]/total]
df[ 'Larger_by_10'] = [larger[9]/total]
df[ 'Larger_by_more_than_10'] = [large/total]

df

df.to_csv('percentage-paths-back.csv',index=False)


# In[44]:


df


# In[ ]:




