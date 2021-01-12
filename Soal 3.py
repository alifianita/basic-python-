#!/usr/bin/env python
# coding: utf-8

# In[9]:


kkm = float(70)


# In[16]:


teori = float(input("nilai teori:"))


# In[22]:


praktek = float(input("nilai praktek:"))


# In[24]:


if praktek >= kkm and teori >= kkm:
    print("Selamat, anda lulus!")
    print("Anda harus mengulang ujian praktek.")
elif teori <= kkm and praktek >= kkm:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")


# In[ ]:




