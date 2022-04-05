#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


#Read in csv from fetched data
issues = pd.read_csv('issues.csv',header=0)


# In[22]:


issues.head()


# In[23]:


issues.dtypes


# In[25]:


#convert object type for dates to datetime for two date columns
issues['Closed at'] = pd.to_datetime(issues['Closed at'])
issues['Created at'] = pd.to_datetime(issues['Created at'])


# In[26]:


issues.dtypes


# In[27]:


#convert all object type to strings, integers, or boolean types
issues_converted = issues.convert_dtypes()


# In[28]:


issues_converted.dtypes


# In[29]:


#Slice of top 5 tuples
issues_converted.head()


# In[30]:


from pandas.api.types import CategoricalDtype


# In[31]:


#convert State attribute to categorical
issues_converted.State = issues_converted.State.astype('category')


# In[32]:


#convert State category to numeric ((0= closed, 1= open)
issues_converted.State = issues_converted.State.cat.codes


# In[33]:


issues_converted.head()


# In[34]:


#Frequency of Closed (0) vs Open (1) State of issues
issues_converted['State'].value_counts().plot(kind='bar')
plt.title('Closed vs Open Issues')
plt.xlabel('State')
plt.ylabel('Count')
plt.show()


# In[35]:


#Strip plot of # comments vs closed or open state of issue
sns.stripplot(data=issues_converted, x='State', y = '# of Comments')
plt.title('# of Comments vs. State')
plt.show()


# In[36]:


#Correlation Heatmap for the numeric attributes
plt.figure(figsize=(16,10))
sns.heatmap(issues_converted.corr(), annot=True)
plt.show()


# In[54]:


#Plotting counts of State (closed (0) or open (1)) against # of Labels
issues_converted.hist(column='# of Labels', by='State', sharey=True, sharex=True)
plt.show()


# In[22]:


#Plotting counts of issue State (closed (0) or open (1)) against project lifetime
issues_converted.hist(column='Created at', by='State', bins=12, sharey=True)
# plt.title('Issues By State over Project Lifetime')
plt.show()


# In[21]:


fig,ax = plt.subplots(1,1)
a = np.array(issues_converted['Created at'])
ax.hist(a, bins = 12) #[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
ax.set_title("Issues Over Project Lifetime")
#ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('year')
ax.set_ylabel('no. of issues')
plt.show()


# In[22]:


#Plotting counts of issue State (closed (0) or open (1)) against project lifetime
issues_converted.hist(column='Created at', by='State', bins=12, sharey=True)
# plt.title('Issues By State over Project Lifetime')
plt.show()


# In[41]:


x = np.array(code_size['Date'])
y = np.array(code_size['Code Size'])
plt.scatter(x, y)
plt.title('Code Size vs. Project Life')
plt.xlabel('Date')
plt.ylabel('Code Size')
plt.show()


# In[4]:


#Read in csv from fetched data
code_size = pd.read_csv('code_size.csv',header=0)


# In[5]:


code_size.head()


# In[7]:


code_size.dtypes


# In[10]:


code_size['Date'] = pd.to_datetime(code_size['Date'])


# In[38]:


x = np.array(code_size['Date'])
y = np.array(code_size['Code Size'])
plt.bar(x, y)
plt.title('Code Size vs. Project Life')
plt.xlabel('Date')
plt.ylabel('Code Size')
plt.show()


# In[ ]:




