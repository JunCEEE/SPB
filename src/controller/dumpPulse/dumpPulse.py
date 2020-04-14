#!/usr/bin/env python
# coding: utf-8

# In[4]:


import SimEx
from SimEx import *
import matplotlib.pyplot as plt


# In[2]:


prop_path = '/gpfs/exfel/data/user/juncheng/SPBProject/data/simulation/2nip_9fs/prop_5kev_9s_Yoon2016_source.h5'
source_analysis = XFELPhotonAnalysis(input_path=prop_path)


# In[3]:


xs_mf, int0_mean = source_analysis.plotTotalPower()


# In[27]:


dt = (xs_mf.max() - xs_mf.min())/(len(xs_mf) - 1)
dt = dt*1e15
# print (dt,'fs')


# In[35]:


for i,data in enumerate(zip(xs_mf*1e15, int0_mean)):
    if i == 5:
        break
    print('history',i,'{:.5e}'.format(data[1]),1e-15)
    print('tv',data[0],1)
    print('tv',data[0]+dt,1)

