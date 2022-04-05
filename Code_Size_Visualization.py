#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np


''' Code Size anomalies: 2017-04-12 04:42:15,ce1dfec6c29cf9f2ceb3c3ad4c3298955b46e31a,4215484
                         2017-04-12 04:39:07,737dc33d056c15cdab1225e9c36845e9d262d8bc,4215477'''

code_size = pd.read_csv('code_sizes.csv',header=0)
code_size.head()
code_size.dtypes
code_size['Date'] = pd.to_datetime(code_size['Date'])

x = np.array(code_size['Date'])
y = np.array(code_size['Code Size'])
plt.bar(x, y)
plt.title('Code Size Over Project Life')
plt.xlabel('year')
plt.ylabel('KLOC (in 100000\'s)')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




