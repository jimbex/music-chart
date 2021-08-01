#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
d = int(d)

songs = []
artist = []
html = urllib.request.urlopen('https://music.apple.com/ng/playlist/top-100-nigeria/pl.2fc68f6d68004ae993dadfe99de83877').read()
html = html.decode('utf-8')
soup = bs(html, 'html.parser')
mydivs = soup.find_all("div", {"class": "songs-list-row__song-name"})
mydiv = soup.find_all("div", {"class": "songs-list__col songs-list__col--artist typography-body"})
for x in mydivs:
    songs.append(x.text)
for x in mydiv:
    artist.append(x.text)
i = 0
while i < len(artist):
    artist[i] = artist[i].replace('\\n', '')
    artist[i] = artist[i].replace('\\', '')
    songs[i] = songs[i].replace('\\', '')
    i += 1
i = 0
while i < len(artist):
    artist[i] = artist[i].strip()
    i += 1
data = {'Position': [x for x in range(1,len(songs) + 1)], 'song': songs, 'artist': artist}
df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\{m}{d}.csv')


driver = webdriver.Chrome()
driver.get('https://music.apple.com/ng/browse/top-charts/albums')
time.sleep(5)
elem = driver.find_element_by_css_selector('body')
elem.click()
for x in range(20):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
content1 = driver.page_source
driver.close()

position = []
album = []
artist = []
soup = bs(content1, 'html.parser') 
pos = soup.find_all("div", {'class': 'lockup-ranking'})
alb1 = soup.find_all("a", {'class': 'line lockup__name has-adjacent-link'})
alb2 = soup.find_all("a", {'class': 'line lockup__name'})
art1 = soup.find_all("a", {'class': 'dt-link-to line2 linkable'})
art2 = soup.find_all("div", {'class': 'line2'})
for x in pos:
    position.append(x.text)
for x in alb1:
    album.append(x.text)
for x in alb2:
    album.append(x.text)
for x in art1:
    artist.append(x.text)
for x in art2:
    artist.append(x.text)

i = 0
while i < len(artist):
    artist[i] = artist[i].replace('\\n', '')
    album[i] = album[i].replace('\\n', '')
    artist[i] = artist[i].strip()
    album[i] = album[i].strip()
    i += 1

data = {'Position': [x for x in range(1,len(album) + 1)], 'artist': artist, 'album': album}
df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d}.csv')