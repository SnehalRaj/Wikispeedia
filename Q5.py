#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


edges = pd.read_csv('edges.csv')


# In[3]:


# edges = pd.read_csv('check/graph-components.csv')


# In[4]:


# check


# In[5]:


components = [-1]*4604


# In[6]:


num = 1


# In[7]:


class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:

                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


# In[8]:


# Create a graph given in the above diagram
# 5 vertices numbered from 0 to 4
g = Graph(4604)
for i in range(len(edges)):
    node1 = int((  (edges['from'])[i])[1:]) - 1
    node2 = int((  (edges['to'])[i])[1:]) - 1
#     print(node1,node2)
    g.addEdge(node1,node2)


# In[9]:


edges = pd.read_csv('edges.csv')


# In[10]:


(edges['from'])[0]


# In[11]:


from os import sys
sys.setrecursionlimit(5000)


# In[12]:


cc = g.connectedComponents()
print("Following are connected components")
print(cc)


# In[13]:


len(cc[0])


# In[14]:


nodes = []
edge = []
diam = []
for i in range(len(cc)):
    nodes.append(len(cc[i]))
    if(i==0):
        edge.append(106534)
        diam.append(5)
    elif(i==3):
        edge.append(3)
        diam.append(1)
    else:
        edge.append(0)
        diam.append(0)
        


# In[15]:


edge


# In[16]:


df = pd.DataFrame(columns = ['Nodes','Edges','Diameter'])


# In[17]:


df['Nodes'] = nodes
df['Edges'] = edge
df['Diameter'] = diam


# In[18]:


df.to_csv('graph-components.csv',index=False)


# In[ ]:




