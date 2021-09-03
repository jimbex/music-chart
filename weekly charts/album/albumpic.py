from ytmusicapi import YTMusic
import spotipy
import pandas as pd
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials as scc 
auth = scc(client_id = 'c866706bac4b40149dcc6723f7957239', 
           client_secret = 'aeb967e927e9458b8561f64f8c4cecf5')
sp = spotipy.Spotify(auth_manager = auth)
yt = YTMusic()
m = datetime.today().strftime('%B')
w = datetime.today().strftime('%V')
addr = input('Enter ur file destination: ')

df = pd.read_csv(f'week{w}-album100.csv', encoding = 'utf-8')
song = list(df['album'])
artist = list(df['artist'])
pos = list(df['rank'])

url = {}
a = 0
for i in song:
  e = artist[a].lower()
  if ' ' in  e:
    y = e[:e.index(' ')]
  else:
    y = e
  f = song[a]
  if ('(') in f:
    f = f[:f.index('(') - 1]
  if 'ft' in f:
    f = f[:f.index('ft') - 1]
  b = sp.search(q = f, type='album')
  z = -1
  for x in b['albums']['items']:
    z += 1
    c = b['albums']['items'][z]['artists'][0]['name'].lower()
    if ' ' in c:
      c = c.replace(' ', '')
    if ' ' in e:
      j = e
      k = e.split()
      e = e.replace(' ', '')
    if c == e:
      url[pos[a]] = b['albums']['items'][z]['images'][0]['url']
      break
    if c != e:
      if ' ' in j and j.count(' ') > 1:
        if k[0] in c and k[1] in c:
          url[pos[a]] = b['albums']['items'][z]['images'][0]['url']
          break
        elif k[0] in c or k[1] in c:
          url[pos[a]] = b['albums']['items'][z]['images'][0]['url']
          break
    else:
      break
  else:
    b = yt.search(f + ' ' + e, 'albums')
    url[pos[a]] = b[0]['thumbnails'][0]['url']


  a += 1

data = {'rank': url.keys(), 'image': url.values()}
df1 = pd.DataFrame(data)
df1 = df1.set_index('rank')

df1.to_csv(f'week{w}-picalbum100.csv', encoding='utf-8')
df1.to_json(f'{addr}\\webboard\\docs\\albumpic.json')