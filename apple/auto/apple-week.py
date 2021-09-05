#!/usr/bin/env python
# coding: utf-8

# In[30]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
d = int(d)

songs = []
artist = []
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/africa-now/pl.a0794db8bc6f45888834fa708a674987').read())
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
addr = input('Enter file destination: ')
df.to_csv(f'{addr}\\music-chart\\apple\\africa-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\africa\\apple_africa-week{w}.csv', encoding='utf-8')
                                  
songs = []
artist = []
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/african-hip-hop/pl.31847c105ecf4d14b34793a3874eb9e9').read())
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
df.to_csv(f'{addr}\\music-chart\\apple\\africahiphop-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\hiphop\\apple_afrohiphop-week{w}.csv', encoding='utf-8')
                                  
songs = []
artist = []
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/african-gospel/pl.c5b1ec8662674e41a3e16044190e9dfa').read())
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
df.to_csv(f'{addr}\\music-chart\\apple\\africagospel-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\gospel\\apple_gospel-week{w}.csv', encoding='utf-8')

                                  
songs = []
artist = []
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/street-anthems/pl.3ff776bc9924419293cce914a8f5a598').read())
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
df.to_csv(f'{addr}\\music-chart\\apple\\street-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\street\\apple_street-week{w}.csv', encoding='utf-8')

                                  
songs = []
artist = []
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/afrobeats-hits/pl.dc349df19c6f410d874c197db63ecfed').read())
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
df.to_csv(f'{addr}\\music-chart\\apple\\afrobeats-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\afrobeat\\apple_afrobeats-week{w}.csv', encoding='utf-8')

                                  
songs = []
artist = []
html = str(urllib.request.urlopen('https://music.apple.com/ng/playlist/alt%C3%A9-cruise/pl.2786e86e72014805bcb2f84d4e68fded').read())
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
df.to_csv(f'{addr}\\music-chart\\apple\\alte-week{w}.csv')
df.to_csv(f'{addr}\\music-chart\\weekly charts\\alte\\apple_alte-week{w}.csv', encoding='utf-8')

