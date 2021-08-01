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
df1 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 6}.csv', encoding='utf-8')
df2 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 5}.csv', encoding='utf-8')
df3 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 4}.csv', encoding='utf-8')
df4 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 3}.csv', encoding='utf-8')
df5 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 2}.csv', encoding='utf-8')
df6 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d - 1}.csv', encoding='utf-8')
df7 = pd.read_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\afropop-{m}{d}.csv', encoding='utf-8')


# In[3]:


df7['title'] = [df7['song'][x] + ' - ' + df7['artist'][x] for x in range(0,len(df7['song']))]
df6['title'] = [df6['song'][x] + ' - ' + df6['artist'][x] for x in range(0,len(df6['song']))]
df5['title'] = [df5['song'][x] + ' - ' + df5['artist'][x] for x in range(0,len(df5['song']))]
df4['title'] = [df4['song'][x] + ' - ' + df4['artist'][x] for x in range(0,len(df4['song']))]
df3['title'] = [df3['song'][x] + ' - ' + df3['artist'][x] for x in range(0,len(df3['song']))]
df2['title'] = [df2['song'][x] + ' - ' + df2['artist'][x] for x in range(0,len(df2['song']))]
df1['title'] = [df1['song'][x] + ' - ' + df1['artist'][x] for x in range(0,len(df1['song']))]


# In[4]:


songs = list(df1['title']) + list(df2['title']) + list(df3['title']) + list(df4['title']) + list(df5['title']) + list(df6['title']) + list(df7['title'])
songs = set(songs)
final = {}


# In[5]:


song = list(df1['title'])
for x in songs:
    if x in song:
        final[x] = [song.index(x) + 1]
    else:
        final[x] = [201]


# In[6]:


song1 = list(df2['title'])
for x in songs:
    if x in song1:
        final[x].append(song1.index(x) + 1)
    else:
        final[x].append(201)


# In[7]:


song2 = list(df3['title'])
for x in songs:
    if x in song2:
        final[x].append(song2.index(x) + 1)
    else:
        final[x].append(201)


# In[8]:


song3 = list(df4['title'])
for x in songs:
    if x in song3:
        final[x].append(song3.index(x) + 1)
    else:
        final[x].append(201)


# In[9]:


song4 = list(df5['title'])
for x in songs:
    if x in song4:
        final[x].append(song4.index(x) + 1)
    else:
        final[x].append(201)


# In[10]:


song5 = list(df6['title'])
for x in songs:
    if x in song5:
        final[x].append(song5.index(x) + 1)
    else:
        final[x].append(201)


# In[11]:


song6 = list(df7['title'])
for x in songs:
    if x in song6:
        final[x].append(song6.index(x) + 1)
    else:
        final[x].append(201)


# In[12]:


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


# In[13]:


data = {'song':songs,'artist':artists,'R1':post1,'R2':post2,'R3':post3,'R4':post4,'R5':post5,'R6':post6,'R7':post7,'RT': postT}
df = pd.DataFrame(data)


# In[14]:


df.sort_values(by=['RT'], inplace=True)


# In[15]:


df['rank'] = [x for x in range(1,len(final) + 1)]
df = df.set_index('rank')


# In[16]:


df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\boom\\boom_afropop-week{w}.csv')
df.to_csv(f'C:\\Users\\faree\\Desktop\\music charts\\weekly charts\\afropop\\boom_afropop-week{w}.csv')


