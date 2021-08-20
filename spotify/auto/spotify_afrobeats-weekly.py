#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
w = datetime.today().strftime("%V")


# In[2]:

addr = input('Enter ur file destination: ')
import pandas as pd
df1 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 6}.csv')
df2 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 5}.csv')
df3 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 4}.csv')
df4 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 3}.csv')
df5 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 2}.csv')
df6 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d - 1}.csv')
df7 = pd.read_csv(f'{addr}\\spotify\\afrobeats-{m}{d}.csv')


# In[3]:


df1 = df1[['song', 'artist']]
df2 = df2[['song', 'artist']]
df3 = df3[['song', 'artist']]
df4 = df4[['song', 'artist']]
df5 = df5[['song', 'artist']]
df6 = df6[['song', 'artist']]
df7 = df7[['song', 'artist']]


# In[4]:


df7['position'] = [x for x in range(1,len(df7['song']) + 1)]
df6['position'] = [x for x in range(1,len(df6['song']) + 1)]
df5['position'] = [x for x in range(1,len(df5['song']) + 1)]
df4['position'] = [x for x in range(1,len(df4['song']) + 1)]
df3['position'] = [x for x in range(1,len(df3['song']) + 1)]
df2['position'] = [x for x in range(1,len(df2['song']) + 1)]
df1['position'] = [x for x in range(1,len(df1['song']) + 1)]


# In[5]:


df7['title'] = [df7['song'][x] + ' - ' + df7['artist'][x] for x in range(0,len(df7['song']))]
df6['title'] = [df6['song'][x] + ' - ' + df6['artist'][x] for x in range(0,len(df6['song']))]
df5['title'] = [df5['song'][x] + ' - ' + df5['artist'][x] for x in range(0,len(df5['song']))]
df4['title'] = [df4['song'][x] + ' - ' + df4['artist'][x] for x in range(0,len(df4['song']))]
df3['title'] = [df3['song'][x] + ' - ' + df3['artist'][x] for x in range(0,len(df3['song']))]
df2['title'] = [df2['song'][x] + ' - ' + df2['artist'][x] for x in range(0,len(df2['song']))]
df1['title'] = [df1['song'][x] + ' - ' + df1['artist'][x] for x in range(0,len(df1['song']))]


# In[6]:


songs = list(df1['title']) + list(df2['title']) + list(df3['title']) + list(df4['title']) + list(df5['title']) + list(df6['title']) + list(df7['title'])
songs = set(songs)
final = {}


# In[7]:


song = list(df1['title'])
for x in songs:
    if x in song:
        final[x] = list(df1['position'][df1['title'] == x])
    else:
        final[x] = [301]


# In[8]:


song1 = list(df2['title'])
for x in songs:
    if x in song1:
        final[x].append(int(df2['position'][df2['title'] == x]))
    else:
        final[x].append(301)


# In[9]:


song2 = list(df3['title'])
for x in songs:
    if x in song2:
        final[x].append(int(df3['position'][df3['title'] == x]))
    else:
        final[x].append(301)


# In[10]:


song3 = list(df4['title'])
for x in songs:
    if x in song3:
        final[x].append(int(df4['position'][df4['title'] == x]))
    else:
        final[x].append(301)


# In[11]:


song4 = list(df5['title'])
for x in songs:
    if x in song4:
        final[x].append(int(df5['position'][df5['title'] == x]))
    else:
        final[x].append(301)


# In[12]:


song5 = list(df6['title'])
for x in songs:
    if x in song5:
        final[x].append(int(df6['position'][df6['title'] == x]))
    else:
        final[x].append(301)


# In[13]:


song6 = list(df7['title'])
for x in songs:
    if x in song6:
        final[x].append(int(df7['position'][df7['title'] == x]))
    else:
        final[x].append(301)


# In[14]:


songs = [x[:x.index('-') - 1 ] for x in final.keys()]
artists = [x[x.index('-') + 2:] for x in final.keys()]
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] for x in final.values()]
post6 = [x[5] for x in final.values()]
post7 = [x[6] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x] + post5[x] + post6[x] + post7[x] )/7 for x in range(0, len(final))]


# In[15]:


data = {'song':songs,'artist':artists,'R1':post1,'R2':post2,'R3':post3,'R4':post4,'R5':post5,'R6':post6,'R7':post7,'RT': postT}
df = pd.DataFrame(data)


# In[16]:


df.sort_values(by=['RT'], inplace=True)


# In[17]:


df['rank'] = [x for x in range(1,len(final) + 1)]
df = df.set_index('rank')


# In[18]:


df.to_csv(f'{addr}\\spotify\\spotify_afrobeats-week{w}.csv')
df.to_csv(f'{addr}\\weekly charts\\afrobeat\\spotify_afrobeats-week{w}.csv')


