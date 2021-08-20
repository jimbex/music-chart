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
    df.to_csv(f'{addr}\\audiomack\\{m}{d}.csv')
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
    df.to_csv(f'{addr}\\audiomack\\album-{m}{d}.csv')
except:
    pass

# In[8]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/afro-hip-hop')
    a = driver.find_element_by_tag_name('time')
    a = a.text.split(' ')
    b = int(a[1][:-1])
    if b == d and m == a[0]:
        driver.execute_script("window.scrollTo(0, 600)") 
        button = driver.find_element_by_class_name('button__arrow')
        button.click()
        content = driver.page_source
        soup = bs(content, 'html.parser') 
        song = []
        artist = []
        mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
        mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
        for x in mydiv:
            song.append(x.text)
        for x in mydivs:
            artist.append(x.text)
        data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
        df = pd.DataFrame(data)
        df = df.set_index('Position')
        df.to_csv(f'{addr}\\audiomack\\afrohiphop-{m}{d}.csv')
    driver.close()
except:
    pass


# In[9]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/verified-afrobeats')
    a = driver.find_element_by_tag_name('time')
    a = a.text.split(' ')
    b = int(a[1][:-1])
    if b == d and m == a[0]:
        driver.execute_script("window.scrollTo(0, 600)") 
        button = driver.find_element_by_class_name('button__arrow')
        button.click()
        content = driver.page_source
        soup = bs(content, 'html.parser') 
        song = []
        artist = []
        mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
        mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
        for x in mydiv:
            song.append(x.text)
        for x in mydivs:
            artist.append(x.text)
        data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
        df = pd.DataFrame(data)
        df = df.set_index('Position')
        df.to_csv(f'{addr}\\audiomack\\afrobeat-{m}{d}.csv')
    driver.close()
except:
    pass



# In[10]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/alte-sounds')
    a = driver.find_element_by_tag_name('time')
    a = a.text.split(' ')
    b = int(a[1][:-1])
    if b == d and m == a[0]:
        driver.execute_script("window.scrollTo(0, 600)") 
        button = driver.find_element_by_class_name('button__arrow')
        button.click()
        content = driver.page_source
        soup = bs(content, 'html.parser') 
        song = []
        artist = []
        mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
        mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
        for x in mydiv:
            song.append(x.text)
        for x in mydivs:
            artist.append(x.text)
        data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
        df = pd.DataFrame(data)
        df = df.set_index('Position')
        df.to_csv(f'{addr}\\audiomack\\alte-{m}{d}.csv')
    driver.close()
except:
    pass

# In[11]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/afro-pop-hits')
    a = driver.find_element_by_tag_name('time')
    a = a.text.split(' ')
    b = int(a[1][:-1])
    if b == d and m == a[0]:
        driver.execute_script("window.scrollTo(0, 600)") 
        button = driver.find_element_by_class_name('button__arrow')
        button.click()
        content = driver.page_source
        soup = bs(content, 'html.parser') 
        song = []
        artist = []
        mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
        mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
        for x in mydiv:
            song.append(x.text)
        for x in mydivs:
            artist.append(x.text)
        data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
        df = pd.DataFrame(data)
        df = df.set_index('Position')
        df.to_csv(f'{addr}\\audiomack\\afropop-{m}{d}.csv')
    driver.close()
except:
    pass

# In[ ]:




