#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials as scc 
auth = scc(client_id = 'c866706bac4b40149dcc6723f7957239', 
           client_secret = 'aeb967e927e9458b8561f64f8c4cecf5')
sp = spotipy.Spotify(auth_manager = auth)


# In[2]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
addr = input('Enter your file destination: ')

# In[3]:


art = []
art1 = {}
play = sp.user_playlist('patrickimoh', '75GeX247deNdTX7zdyZDnU')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)


# In[4]:


art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1
    


# In[5]:


import pandas as pd
song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\{m}{d}.csv')


# In[6]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DWYkaDif7Ztbp')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1


# In[7]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\africa-{m}{d}.csv')


# In[8]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DWYs2pvwxWA7l')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1


# In[9]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\afropop-{m}{d}.csv')


# In[10]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DXdl8xYyG9Dm1')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1


# In[11]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\afrohiphop-{m}{d}.csv')


# In[12]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DX9lAYMw7KoAO')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1


# In[13]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\gospel-{m}{d}.csv')


# In[14]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DWT6SJaitNDax')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    a = x['artists']
    art1[x['name']] = a[0]['name']
    if len(a) > 1:
        while i < len(a):
            art1[x['name']] += ', ' +  a[i]['name']
            i += 1


# In[15]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\afrobeats-{m}{d}.csv')


# In[16]:


art = []
art1 = {}
play = sp.user_playlist('spotify', '37i9dQZF1DX5ja5oV6Kto0')
for i in play['tracks']['items']:
    track = i['track']
    art.append(track)
art1 = {}
i = 1
for x in art:
    try:
        a = x['artists']
        art1[x['name']] = a[0]['name']
        if len(a) > 1:
            while i < len(a):
                art1[x['name']] += ', ' +  a[i]['name']
                i += 1
    except:
        continue


# In[17]:


song = art1.keys()
artist = art1.values()
spot = {'Position': [x for x in range(1,len(song) + 1)], 'song':song, 'artist':artist}
df = pd.DataFrame(spot)
df = df.set_index('Position')
df.to_csv(f'{addr}\\spotify\\alternative-{m}{d}.csv')

