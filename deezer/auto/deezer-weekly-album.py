#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
w = datetime.today().strftime("%V")


# In[2]:


import pandas as pd
df1 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 6}.csv', encoding='utf-8')
df2 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 5}.csv', encoding='utf-8')
df3 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 4}.csv', encoding='utf-8')
df4 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 3}.csv', encoding='utf-8')
df5 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 2}.csv', encoding='utf-8')
df6 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d - 1}.csv', encoding='utf-8')
df7 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\album-{m}{d}.csv', encoding='utf-8')


# In[3]:


albums = list(df1['album']) + list(df2['album']) + list(df3['album']) + list(df4['album']) + list(df5['album']) + list(df6['album']) + list(df7['album'])
albums = set(albums)
final = {}


# In[4]:


artist1 = list(df1['artist'])
artist2 = list(df2['artist'])
artist3 = list(df3['artist'])
artist4 = list(df4['artist'])
artist5 = list(df5['artist'])
artist6 = list(df6['artist'])
artist7 = list(df7['artist'])


# In[5]:


album = list(df1['album'])
for x in albums:
    if x in album:
        final[x] = list(df1['Position'][df1['album'] == x])
    else:
        final[x] = [301]


# In[6]:


album1 = list(df2['album'])
for x in albums:
    if x in album1:
        x = x.strip()
        final[x].append(album1.index(x) + 1)
    else:
        final[x].append(301)


# In[7]:


album2 = list(df3['album'])
for x in albums:
    if x in album2:
        final[x].append(album2.index(x) + 1)
    else:
        final[x].append(301)


# In[8]:


album3 = list(df4['album'])
for x in albums:
    if x in album3:
        final[x].append(album3.index(x) + 1)
    else:
        final[x].append(301)


# In[9]:


album4 = list(df5['album'])
for x in albums:
    if x in album4:
        final[x].append(album4.index(x) + 1)
    else:
        final[x].append(301)


# In[10]:


album5 = list(df6['album'])
for x in albums:
    if x in album5:
        final[x].append(album5.index(x) + 1)
    else:
        final[x].append(301)


# In[11]:


album6 = list(df7['album'])
for x in albums:
    if x in album6:
        final[x].append(album6.index(x) + 1)
    else:
        final[x].append(301)


# In[13]:


albums = [x for x in final.keys()]
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] for x in final.values()]
post6 = [x[5] for x in final.values()]
post7 = [x[6] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x] + post5[x] + post6[x] + post7[x] )/7 for x in range(0, len(final))]


# In[14]:


artist = []
x = 0
for i in albums:
    if i in album:
        artist.append(artist1[album.index(i)])
    elif i in album1:
        artist.append(artist2[album1.index(i)])
    elif i in album2:
        artist.append(artist3[album2.index(i)])
    elif i in album3:
        artist.append(artist4[album3.index(i)])
    elif i in album5:
        artist.append(artist6[album5.index(i)])
    elif i in album6:
        artist.append(artist7[album6.index(i)])
    elif i in album4:
        artist.append(artist5[album4.index(i)])
    x += 1


# In[15]:


data = {'album':albums,'artist':artist,'R1':post1,'R2':post2,'R3':post3,'R4':post4,'R5':post5,'R6':post6,'R7':post7,'RT': postT}
df = pd.DataFrame(data)


# In[16]:


df.sort_values(by=['RT'], inplace=True)


# In[17]:


df['rank'] = [x for x in range(1,len(final) + 1)]
df = df.set_index('rank')


# In[19]:


df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\deezer\\deezer_album-week{w}.csv')
df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\weekly charts\\album\\deezer_album-week{w}.csv')

