#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


commits = pd.read_csv('commits.csv',header=0)


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


commits.head()


# In[6]:


commits.dtypes


# In[9]:


commits['Date'] = pd.to_datetime(commits['Date'])


# In[11]:


commits.dtypes


# In[9]:


from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# In[20]:


fig,ax = plt.subplots(1,1)
a = np.array(commits['Date'])
ax.hist(a, bins = 12)#[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
ax.set_title("Commits Over Project Life")
#ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('year')
ax.set_ylabel('no. of commits')
plt.show()


# In[50]:


fig,ax = plt.subplots(1,1)
b = commits.iloc[2211:2835, 0]
ax.hist(b, bins = 12)#[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
ax.set_title("Commits Over First Year")
#ax.set_xticks([0,12])
ax.set_xlabel('date')
ax.set_ylabel('no. of commits')
plt.show()


# In[49]:


fig,ax = plt.subplots(1,1)
b = commits.iloc[0:78, 0]
ax.hist(b, bins = 12)#[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
ax.set_title("Commits Over Most Recent Year")
#ax.set_xticks([0,12])
ax.set_xlabel('date')
ax.set_ylabel('no. of commits')
plt.show()


# In[ ]:




