#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


check = pd.read_csv('check/category-subtree-paths.csv')
check


# In[3]:


path = "wikispeedia_paths-and-graph/"
df = pd.read_csv(path+'paths_finished.tsv',sep='\t',names=['hashedIpAddress','timestamp','durationInSec','path','rating'])

paths = []

for i in range(len(df)):
    paths.append((df.path[i]).split(';'))


# In[4]:


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


# In[5]:


article_id = pd.read_csv('article-ids.csv')
article_id.head()


# In[6]:


article_id_map = {}
for i in range(len(article_id)):
    index = str(article_id['id'][i])
    article = article_id['article'][i]
    article_id_map[article] = index
    
    
    


# In[7]:


no_back = []
for i in range(len(without_back)):
    row  = []
    for j in without_back[i]:
        row.append(article_id_map[j])
    no_back.append(row)


# In[8]:


edges  = pd.read_csv('edges.csv')


# In[9]:


from collections import defaultdict 
  
# Function to build the graph 
def build_graph(edges): 
#     edges = [ 
#         ["A", "B"], ["A", "E"],  
#         ["A", "C"], ["B", "D"], 
#         ["B", "E"], ["C", "F"], 
#         ["C", "G"], ["D", "E"] 
#     ] 
    graph = defaultdict(list) 
      
        
    # Loop to iterate over every  
    # edge of the graph 
    for edge in edges: 
        a, b = edge[0], edge[1] 
          
        # Creating the graph  
        # as adjacency list 
        graph[a].append(b) 
        graph[b].append(a) 
    return graph


# In[10]:


edges_list = edges.values.tolist()
edges = []
for i in range(len(edges_list)):
    row = []
    for j in edges_list[i]:
        row.append(tuple(j))
    edges.append(row)


# In[11]:


graph = build_graph(edges)


# In[12]:


def BFS_SP(graph, start, goal): 
    explored = [] 
# Queue for traversing the 
# graph in the BFS 
    queue = [[start]] 

# If the desired node is 
# reached 
    if start == goal: 
        print("Same Node") 
        return

    # Loop to traverse the graph 
    # with the help of the queue 
    while queue: 
        path = queue.pop(0)
        node = tuple(path[-1])

        # Codition to check if the 
        # current node is not visited 
        if node not in explored: 
            neighbours = graph[node] 

            # Loop to iterate over the 
            # neighbours of the node 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour ) 
                queue.append(new_path) 

                # Condition to check if the 
                # neighbour node is the goal 
                if neighbour == goal: 
#                     print("Shortest path = ", *new_path) 
                    return (new_path)
            explored.append(node) 

    return None


# In[13]:


ret = BFS_SP(graph, tuple('A0001'), tuple('A0010') ) 
ret


# In[14]:


no_back[0]


# In[15]:


s_paths = []
for i in range(len(no_back)):
    row = BFS_SP(graph, tuple( (no_back[i])[0]), tuple( (no_back[i])[-1] ))
    if(row is not None):
        list_row = []
        for j in row:
            list_row.append(list(j))
        s_paths.append(list_row)


# In[16]:


def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 


# In[17]:


shortest_p = []
for i in range(len(s_paths)):
    row = []
    for j in s_paths[i]:
        row.append(convert(j))
    shortest_p.append(row)


# In[18]:


shortest_p


# In[19]:


import csv

with open('article-categories.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
data = data[1:]
print(data)


# In[20]:


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

    


# In[21]:


parents = {}
for i in category_id_map.keys():
    parents[i] = []
    name = category_id_map[i]
    for j in category_id_map.values():
#         print(j)
        if (name.startswith(j)):
            parents[i].append(category_id_rev_map[j])
parents


# In[22]:


category_count={}
for i in range(146):
    cat = 'C'+str(i+1).zfill(4)
    category_count[cat] = 0


# In[23]:


category_count_human_times = category_count.copy()
category_count_human_paths = category_count.copy()
category_count_short_times = category_count.copy()
category_count_short_paths = category_count.copy()


# In[24]:


for i in range( len(no_back)):
    for j in no_back[i]:
        row = data[int(j[1:]) - 1]
        for k in range(1,len(row)):
            row2 = parents[row[k]]
            for l in range(len(row2)):
                category_count_human_times[row2[l]]+=1


# In[25]:


category_count_human_times


# In[26]:


row_dict = category_count.copy()
for i in range( len(no_back)):
    cats = []
    for j in no_back[i]:
        row = data[int(j[1:]) - 1]
        for k in range(1,len(row)):
            row2 = parents[row[k]]
            for l in range(len(row2)):
                cats.append(row2[l])
    cats = set(cats)
    for elem in cats:
        category_count_human_paths[elem]+= 1


# In[27]:


category_count_human_paths


# In[28]:


for i in range( len(shortest_p)):
    for j in shortest_p[i]:
        row = data[int(j[1:]) - 1]
        for k in range(1,len(row)):
            row2 = parents[row[k]]
            for l in range(len(row2)):
                category_count_short_times[row2[l]]+=1


# In[29]:


row_dict = category_count.copy()
for i in range( len(shortest_p)):
    cats = []
    for j in shortest_p[i]:
        row = data[int(j[1:]) - 1]
        for k in range(1,len(row)):
            row2 = parents[row[k]]
            for l in range(len(row2)):
                cats.append(row2[l])
    cats = set(cats)
    for elem in cats:
        category_count_short_paths[elem]+= 1


# In[30]:


category_count_short_paths


# In[31]:


df = pd.DataFrame(columns=['cat_id','human_times','human_paths','shortest_times','shortest_paths'])

df


cat = []
for i in range(146):
    cat.append('C'+str(i+1).zfill(4))

cat

df['cat_id'] = cat

df['human_times'] = category_count_human_times.values()

df['human_paths'] = category_count_human_paths.values()
df['shortest_times'] = category_count_short_times.values()
df['shortest_paths'] = category_count_short_paths.values()


df.to_csv('category-subtree-paths.csv',index=False)


# In[32]:


df

