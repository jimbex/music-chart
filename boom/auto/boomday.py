#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)


# In[ ]:


songs = []
artist = []
import urllib.request
from bs4 import BeautifulSoup as bs
html = str(urllib.request.urlopen('https://www.boomplay.com/playlists/2491655?from=charts').read())
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
boom4 = {'artist': artist, 'song': songs}
addr = input('Enter your file destination address: ')
import pandas as pd
df = pd.DataFrame(boom4)
df.to_csv(f'{addr}\\boom\\afropop-{m}{d}.csv')


# In[ ]:


songs = []
artist = []
html = str(urllib.request.urlopen('https://www.boomplay.com/playlists/2491652?from=charts').read())
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
boom5 = {'artist': artist, 'song': songs}
import pandas as pd
df = pd.DataFrame(boom5)
df.to_csv(f'{addr}\\boom\\hiphop-{m}{d}.csv')


# In[ ]:


songs = []
artist = []
import urllib.request
from bs4 import BeautifulSoup as bs
html = str(urllib.request.urlopen('https://www.boomplay.com/playlists/27121605').read())
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
boom5 = {'artist': artist, 'song': songs}
import pandas as pd
df = pd.DataFrame(boom5)
df.to_csv(f'{addr}\\boom\\afrobeat-{m}{d}.csv')

