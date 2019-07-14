
# coding: utf-8

# In[6]:


import scipy.io as sio
from spherecluster import VonMisesFisherMixture # using spherecluster package : https://pypi.org/project/spherecluster/0.1.2/


# In[10]:


train = sio.loadmat('./vmf_data.mat') # load segmented frames or superframes
data=train['ps']
print(data.shape)


# In[11]:


vmf_soft = VonMisesFisherMixture(n_clusters=15, posterior_type='soft')
vmf_soft.fit(data)


# In[15]:


mean_directions=vmf_soft.cluster_centers_
print(mean_directions.shape)


# In[18]:


concen=vmf_soft.concentrations_
ind=concen.argsort()[-10:][::-1]
print(concen)
print(ind)
mean_directions=mean_directions[ind,:]
print(mean_directions.shape)


# In[ ]:


sio.savemat('./mean_directions.mat', {'mean_directions':mean_directions}, do_compression=True)

