#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[2]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
addr = input('Enter your destination address: ')


# In[3]:
try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/songs')
    for x in range(11):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    driver.close()
    song = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'music__heading--artist u-d-block u-trunc'})
    mydiv = soup.find_all("span", {'class': 'music__heading--title'})
    for x in mydiv:
        song.append(x.text)
    for x in mydivs:
        artist.append(x.text)


# In[4]:


    if len(song) > len(artist):
        del song[3:7]
    data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\{m}{d}.csv')
except:
    pass

# In[12]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/albums')
    for x in range(20):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    driver.close()


# In[13]:


    album = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'music__heading--artist u-d-block u-trunc'})
    mydiv = soup.find_all("span", {'class': 'music__heading--title'})
    for x in mydiv:
        album.append(x.text)
    for x in mydivs:
        artist.append(x.text)


# In[14]:


    if len(album) > len(artist):
        del album[3:7]
    data = {'Position': [x for x in range(1, len(album) + 1)] ,'album': album, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\album-{m}{d}.csv')
except:
    pass
