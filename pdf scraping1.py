#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tabula as tb
import pandas as pd
import re
#help(tb)

#help(tb.read_pdf)
file = '/Users/Rana/Downloads/New Compressed (zipped) Folder/1247716.pdf'
data = tb.read_pdf(file, stream=True)
print(data)


# In[ ]:




