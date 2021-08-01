#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
w = datetime.today().strftime("%V")


# In[3]:


import pandas as pd
df1 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 6}.csv', encoding='utf-8')
df2 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 5}.csv', encoding='utf-8')
df3 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 4}.csv', encoding='utf-8')
df4 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 3}.csv', encoding='utf-8')
df5 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 2}.csv', encoding='utf-8')
df6 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d - 1}.csv', encoding='utf-8')
df7 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\album_{m}{d}.csv', encoding='utf-8')


# In[4]:


df1 = df1[['album', 'artist']]
df2 = df2[['album', 'artist']]
df3 = df3[['album', 'artist']]
df4 = df4[['album', 'artist']]
df5 = df5[['album', 'artist']]
df6 = df6[['album', 'artist']]
df7 = df7[['album', 'artist']]


# In[5]:


df7['position'] = [x for x in range(1,len(df7['album']) + 1)]
df6['position'] = [x for x in range(1,len(df6['album']) + 1)]
df5['position'] = [x for x in range(1,len(df5['album']) + 1)]
df4['position'] = [x for x in range(1,len(df4['album']) + 1)]
df3['position'] = [x for x in range(1,len(df3['album']) + 1)]
df2['position'] = [x for x in range(1,len(df2['album']) + 1)]
df1['position'] = [x for x in range(1,len(df1['album']) + 1)]


# In[6]:


df7['title'] = [df7['album'][x] + ' - ' + df7['artist'][x] for x in range(0,len(df7['album']))]
df6['title'] = [df6['album'][x] + ' - ' + df6['artist'][x] for x in range(0,len(df6['album']))]
df5['title'] = [df5['album'][x] + ' - ' + df5['artist'][x] for x in range(0,len(df5['album']))]
df4['title'] = [df4['album'][x] + ' - ' + df4['artist'][x] for x in range(0,len(df4['album']))]
df3['title'] = [df3['album'][x] + ' - ' + df3['artist'][x] for x in range(0,len(df3['album']))]
df2['title'] = [df2['album'][x] + ' - ' + df2['artist'][x] for x in range(0,len(df2['album']))]
df1['title'] = [df1['album'][x] + ' - ' + df1['artist'][x] for x in range(0,len(df1['album']))]


# In[7]:


albums = list(df1['title']) + list(df2['title']) + list(df3['title']) + list(df4['title']) + list(df5['title']) + list(df6['title']) + list(df7['title'])
albums = set(albums)
final = {}


# In[8]:


album = list(df1['title'])
for x in albums:
    if x in album:
        final[x] = list(df1['position'][df1['title'] == x])
    else:
        final[x] = [401]


# In[9]:


album1 = list(df2['title'])
for x in albums:
    if x in album1:
        final[x].append(int(album1.index(x) + 1))
    else:
        final[x].append(401)


# In[10]:


artist1 = list(df1['artist'])
artist2 = list(df2['artist'])
artist3 = list(df3['artist'])
artist4 = list(df4['artist'])
artist5 = list(df5['artist'])
artist6 = list(df6['artist'])
artist7 = list(df7['artist'])


# In[12]:


album2 = list(df3['title'])
for x in albums:
    if x in album2:
        final[x].append(int(album2.index(x) + 1))
    else:
        final[x].append(401)


# In[13]:


album3 = list(df4['title'])
for x in albums:
    if x in album3:
        final[x].append(int(album3.index(x) + 1))
    else:
        final[x].append(401)


# In[14]:


album4 = list(df5['title'])
for x in albums:
    if x in album4:
        final[x].append(int(album4.index(x) + 1))
    else:
        final[x].append(401)


# In[15]:


album5 = list(df6['title'])
for x in albums:
    if x in album5:
        final[x].append(int(album5.index(x) + 1))
    else:
        final[x].append(401)


# In[16]:


album6 = list(df7['title'])
for x in albums:
    if x in album6:
        final[x].append(int(album6.index(x) + 1))
    else:
        final[x].append(401)


# In[17]:


len(final)


# In[18]:


albums = [x[:x.index('-') - 1] for x in final.keys()]
artists = [x[x.index('-') + 2:] for x in final.keys()]
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] for x in final.values()]
post6 = [x[5] for x in final.values()]
post7 = [x[6] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x] + post5[x] + post6[x] + post7[x] )/7 for x in range(0, len(final))]


# In[19]:


len(artists)


# In[20]:


data = {'album':albums,'artist':artists,'R1':post1,'R2':post2,'R3':post3,'R4':post4,'R5':post5,'R6':post6,'R7':post7,'RT': postT}
df = pd.DataFrame(data)


# In[21]:


df.sort_values(by=['RT'], inplace=True)


# In[22]:


df['rank'] = [x for x in range(1,len(final) + 1)]
df = df.set_index('rank')


# In[23]:


df


# In[24]:


df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\apple\\apple_album-week{w}.csv')
df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\weekly charts\\album\\apple_album-week{w}.csv')


# In[ ]:




