#!/usr/bin/env python
# coding: utf-8

# In[61]:


import matplotlib.pyplot as plt
import csv

x = []
y = []
  
with open('code_sizes.csv','r') as File:
    lines = csv.reader(File, delimiter=',')
    
    for row in lines:
        x.append(row[0])
        y.append(int(row[2]))
        
x1 = x[::-1]
y1 = y[::-1]

plt.plot(x1, y1, color = 'b')
plt.xticks([0, 800, 1700, 2580], ['2010', '2012', '2014', '2020'])
plt.xlabel('years')
plt.ylabel('KLOC (in 100000\'s)')
plt.title('Code Size Over Project Life')
plt.show()


# In[ ]:




