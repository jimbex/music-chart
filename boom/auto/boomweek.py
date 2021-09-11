#!/usr/bin/env python
# coding: utf-8

# In[ ]:


songs = []
artist = []
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
html = str(urllib.request.urlopen('https://www.boomplay.com/share/playlist/850210').read())
soup = bs(html, 'html.parser')
mydiv = soup.find_all("p", {"class": "singerName"})
mydivs = soup.find_all("strong", {"class": "songName"})
for x in mydivs:
    songs.append(x.text)
for y in mydiv:
    artist.append(y.text)

from datetime import datetime
w = datetime.today().strftime("%V")

i = 0
for x in artist:
    artist[i] = x[:x.index('-') - 1] 
    i += 1
i = 0
for x in songs:
    if '\\' in x:
        songs[i] = x.replace('\\', '')
    i += 1
boom = {'artist': artist, 'song': songs}
addr = input('Enter your file destination address: ')
df = pd.DataFrame(boom)
df.to_csv(f'{addr}\\music-chart\\boom\\week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\Weekly charts\\songs\\boom_week{w}.csv')

songs = []
artist = []
html = str(urllib.request.urlopen('https://www.boomplay.com/playlists/880218?from=charts').read())
soup = bs(html, 'html.parser')
mydiv = soup.find_all("a", {"class": "artistName"})
mydivs = soup.find_all("a", {"class": "songName"})
for x in mydivs:
    songs.append(x.text)
for y in mydiv:
    artist.append(y.text)
i = 0
for x in songs:
    if '\\' in x:
        songs[i] = x.replace('\\', '')
    i += 1
songs = songs[:-1]
boom1 = {'artist': artist, 'song': songs}
df = pd.DataFrame(boom1)
df.to_csv(f'{addr}\\music-chart\\boom\\week{w}-africa.csv')
df.to_csv(f'{addr}\\music-chart\\Weekly charts\\africa\\boom_week{w}-africa.csv')

html = str(urllib.request.urlopen('https://www.boomplay.com/more/charts?id=138&name=Weekly+Top+Albums').read())
album = []
soup = bs(html, 'html.parser')
mydiv = soup.find_all('strong')
for x in mydiv:
    album.append(x.text)
album = album[1:-8]
boom2 = {'position': [x for x in range(1,len(album) + 1)], 'album': album}
df = pd.DataFrame(boom2)
df = df.set_index('position')
df.to_csv(f'{addr}\\music-chart\\boom\\week{w}-album.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\album\\boom_album-week{w}.csv')

songs = []
artist = []
html = str(urllib.request.urlopen('https://www.boomplay.com/playlists/29990?from=home').read())
soup = bs(html, 'html.parser')
mydiv = soup.find_all("a", {"class": "artistName"})
mydivs = soup.find_all("a", {"class": "songName"})
for x in mydivs:
    songs.append(x.text)
for y in mydiv:
    artist.append(y.text)
i = 0
for x in songs:
    if '\\' in x:
        songs[i] = x.replace('\\', '')
    i += 1
songs = songs[:-1]
boom3 = {'artist': artist, 'song': songs}
import pandas as pd
df = pd.DataFrame(boom3)
df.to_csv(f'{addr}\\music-chart\\boom\\boom_gospel-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\gospel\\boom_gospel-week{w}.csv')

