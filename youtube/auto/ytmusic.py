#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ytmusicapi import YTMusic
import pandas as pd

ytmusic = YTMusic()


# In[2]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
addr = input('Enter your file destination: ')


# In[3]:


song = []
artist = []
street = ytmusic.get_playlist('RDCLAK5uy_lE4Fbjb8nOw2qxSeZds9mfpTTS37k9Pxs')
for x in street['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\street-{m}{d}.csv')


# In[4]:


song = []
artist = []
beats = ytmusic.get_playlist('RDCLAK5uy_kmq8ZD0NbHbKkZZ6frtlEjd8khfeZrAd0')
for x in beats['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\afrobeats-{m}{d}.csv')


# In[5]:


song = []
artist = []
pop = ytmusic.get_playlist('RDCLAK5uy_nKKDoXkBvkqq7jfjQSUUCUeDk5tWTgqIw')
for x in pop['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\afropop-{m}{d}.csv')


# In[6]:


song = []
artist = []
gospel = ytmusic.get_playlist('RDCLAK5uy_nt_rV4HSIclVcjSe9sOdwr279gx-seLQs')
for x in gospel['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\gospel-{m}{d}.csv')


# In[7]:


song = []
artist = []
hiphop = ytmusic.get_playlist('RDCLAK5uy_kGgoKYMbZN3uiYZL0dtWaDkLrVPvrxwPg')
for x in hiphop['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\hiphop-{m}{d}.csv')


# In[8]:


song = []
artist = []
r_b = ytmusic.get_playlist('RDCLAK5uy_n3qkemHBD9k_a0B_pX2VWB0RPvebkR7uU')
for x in r_b['tracks']:
    song.append(x['title'])
    artist.append(x['artists'][0]['name'])
    
data = {'Position': [x for x in range(1,len(song) + 1)] ,'song': song, 'artist': artist}

df = pd.DataFrame(data)
df = df.set_index('Position')
df.to_csv(f'{addr}\\youtube\\R&B-{m}{d}.csv')

