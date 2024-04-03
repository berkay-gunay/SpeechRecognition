#!/usr/bin/env python
# coding: utf-8

# In[14]:


import whisper
import re
import os
import pandas as pd


# In[9]:


dosya_yolu = input("Lutfen klasorun yolunu giriniz : ")
dosya_yolu = dosya_yolu.strip('"')


# In[10]:


liste = []
with os.scandir(str(dosya_yolu)) as wavs:
    for ses_dosyasi in wavs:
        try:
            model = whisper.load_model("base.en")
            result = model.transcribe(dosya_yolu+"/"+ses_dosyasi.name)
            text = result["text"].strip().lower()
            text = re.sub("[^a-zA-Z\s]","",text)
            liste.append(text)
        except Exception as e:
            liste.append(type(e).__name__)


# In[12]:


data = {"speech_to_text" : liste}


# In[16]:


df = pd.DataFrame(data)
df.to_excel("speech_to_text_Base.en.xlsx", index=False)
print("İşlem tamamlandı.")

# In[ ]:




