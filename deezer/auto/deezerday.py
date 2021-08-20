#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
addr = input('Enter your file destination address: ')


# In[ ]:


import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import js2xml as js
import urllib.request


# In[ ]:


driver = webdriver.Firefox()
driver.get('https://www.deezer.com/en/playlist/1362516565')
time.sleep(2)
elem = driver.find_element_by_class_name('cookie-btn-label')
elem.click()
for x in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(2)
content1 = driver.page_source
driver.execute_script("window.scrollTo(800, 2800)")
time.sleep(2)
content2 = driver.page_source
time.sleep(2)
driver.execute_script("window.scrollTo(2800,4500)")
time.sleep(2)
content3 = driver.page_source
driver.close()


# In[ ]:


soup = bs(content1, 'html.parser') 
mydiv1 = soup.find_all("div", {'itemprop': 'track'})
soup = bs(content2, 'html.parser') 
mydiv2 = soup.find_all("div", {'itemprop': 'track'})
soup = bs(content3, 'html.parser') 
mydiv3 = soup.find_all("div", {'itemprop': 'track'})
mydivs = mydiv1 + mydiv2 + mydiv3
div = []
for x in mydivs:
    if x not in div:
        div.append(x)
    else:
        continue


# In[ ]:


position = []
songs = []
artist = []
for x in div:
    soup = bs(str(x), 'html.parser')
    position.append(int(soup.find("span", {'class': 'datagrid-track-number'}).text))
    soup = bs(str(x), 'html.parser')
    songs.append(soup.find("span", {'itemprop': 'name'}).text)
    soup = bs(str(x), 'html.parser')
    artist.append(soup.find("a", {'itemprop': 'byArtist'}).text)


# In[ ]:


data = {'Position': position, 'song': songs, 'artist': artist}
df = pd.DataFrame(data)
df.to_csv(f'{addr}\\deezer\\{m}{d}.csv')


# In[ ]:


driver = webdriver.Firefox()
driver.get('https://www.deezer.com/en/channels/module/24edc1b8-68cd-411f-b6ef-ce4972b9f671')
time.sleep(4)
elem = driver.find_element_by_class_name('cookie-btn-label')
elem.click()
content3 = driver.page_source
driver.close()

soup = bs(content3, 'html.parser') 
mydiv1 = soup.find_all("div", {'class': 'heading-4'})
mydiv2 = soup.find_all("div", {'class': 'heading-4-sub'})
album = []
artist = []
for x in mydiv1:
    album.append(x.text)
for x in mydiv2:
    artist.append(x.text[3:])

data = {'Position': [x for x in range(1, len(album) + 1)] ,'artist': artist, 'album': album}
df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\deezer\\album-{m}{d}.csv')

