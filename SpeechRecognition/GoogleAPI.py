#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import os
import re
import pandas as pd


# In[2]:


dosya_yolu = input("Lutfen klasorun yolunu giriniz : ")
dosya_yolu = dosya_yolu.strip('"')


# In[3]:


r = sr.Recognizer()


# In[9]:


speech_to_text_list= []
with os.scandir(dosya_yolu) as files:
    for ses_dosyasi in files:
        with sr.AudioFile(dosya_yolu+"/"+ses_dosyasi.name) as source:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
                result = r.recognize_google(audio)
                text = result.lower()
                text = re.sub("[^a-zA-Z\s]","",text)
                speech_to_text_list.append(text)
            except Exception as error:
                speech_to_text_list.append(type(error).__name__)
         

# In[11]:


data = {"speech_to_text" : speech_to_text_list}


# In[12]:


df = pd.DataFrame(data)
df.to_excel("speech_to_text_GoogleAPI.xlsx", index=False)
print("İşlem tamamlandı.")

# In[ ]:




