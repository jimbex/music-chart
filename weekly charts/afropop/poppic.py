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

df = pd.read_csv(f'week{w}-afropop50.csv', encoding = 'utf-8')
song = list(df['song'])
artist = list(df['artist'])
pos = list(df['rank'])

url = {}
a = 0
for i in song:
  e = artist[a].lower()
  f = song[a]
  if ' ' in e and e.count(' ') > 1:
    j = e[:e.index(' ')]
  else:
    j = e
  if ('(') in f:
    f = f[:f.index('(') - 1]
  if 'ft' in f:
    f = f[:f.index('ft') - 1]
  f = f + ' ' + j
  b = sp.search(q = f, type='track')
  for x in b['tracks']['items']:
    z = 0
    c = b['tracks']['items'][z]['album']['artists'][z]['name'].lower()
    if ' ' in c:
      c = c.replace(' ', '')
    if ' ' in e:
      j = e
      k = e.split()
      e = e.replace(' ', '')
    if c == e:
      url[pos[a]] = b['tracks']['items'][z]['album']['images'][0]['url']
      break
    else:
      url[pos[a]] = b['tracks']['items'][0]['album']['images'][0]['url']
      break
        
  else:
    b = yt.search(f + ' ' + j, 'songs')
    url[pos[a]] = b[0]['thumbnails'][0]['url']
  a += 1

data = {'rank': url.keys(), 'image': url.values()}
df1 = pd.DataFrame(data)

df1 = df1.set_index('rank')

df1.to_csv(f'week{w}-picpop.csv', encoding='utf-8')
df1.to_json(f'{addr}\\webboard\\docs\\afropoppic.json')