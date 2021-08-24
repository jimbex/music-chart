#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import pandas as pd
from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
w = int(w)
d = int(d)


# In[2]:

addr = input('Enter ur file destination: ')
df1 = pd.read_csv(f'apple_africa-week{w}.csv', encoding='utf-8')
df2 = pd.read_csv(f'boom_week{w}-africa.csv', encoding='utf-8')
df3 = pd.read_csv(f'spotify_africa-week{w}.csv', encoding='utf-8')
df4 = pd.read_csv(f'deezer_africa-week{w}.csv', encoding='utf-8')


# In[3]:


df1 = df1[['song', 'artist']]
df2 = df2[['song', 'artist']]
df3 = df3[['song', 'artist']]
df4 = df4[['song', 'artist']]


# In[4]:


a = list(df1['song'])
a1 = a.copy()
a2 = list(df1['artist'])
x = 0
for i in a:
    if '(' in i:
        a[x] = i[: i.index('(')]
    if '\\' in i:
        a[x] = a[x].replace('\\', '') 
    a[x] = a[x].strip().lower()
    x += 1


# In[5]:


b = list(df2['song'])
b1 = b.copy()
b2 = list(df2['artist'])
x = 0
for i in b:
    if 'ft' in i:
        b[x] = i.replace('ft', '(ft') + ')'
    x += 1
x = 0
for i in b:
    if '(' in i:
        b[x] = i[: i.index('(')]
    if '\\' in i:
        b[x] = b[x].replace('\\', '') 
    b[x] = b[x].strip().lower()
    x += 1


# In[6]:


c = list(df3['song'])
c1 = c.copy()
c2 = list(df3['artist'])
x = 0
for i in c:
    if '(' in i:
        c[x] = i[: i.index('(')]
    if '\\' in i:
        c[x] = c[x].replace('\\', '') 
    c[x] = c[x].strip().lower()
    x += 1


# In[7]:


d = list(df4['song'])
d1 = d.copy()
d2 = list(df4['artist'])
x = 0
for i in d:
    if '(' in i:
        d[x] = i[: i.index('(')]
    if '\\' in i:
        d[x] = d[x].replace('\\', '') 
    d[x] = d[x].strip().lower()
    x += 1


# In[8]:


songs = a + b + c + d
songs = set(songs)


# In[9]:


len(songs)


# In[10]:


songs = list(songs)


# In[11]:


final = {}


# In[12]:


x = 0
for i in songs:
    if i in a:
        final[i] = [a.index(i) + 1]
    else:
        final[i] = [200]


# In[13]:


x = 0
for i in songs:
    if i in b:
        final[i].append(b.index(i) + 1)
    else:
        final[i].append(250)


# In[14]:


x = 0
for i in songs:
    if i in c:
        final[i].append(c.index(i) + 1)
    else:
        final[i].append(225)


# In[15]:


x = 0
for i in songs:
    if i in d:
        final[i].append(d.index(i) + 1)
    else:
        final[i].append(270)


# In[16]:


x = 0
for i in songs:
    if i in a:
        final[i].append(a2[a.index(i)])
    if i in b and len(final[i]) < 5:
        final[i].append(b2[b.index(i)])
    if i in c and len(final[i]) < 5:
        final[i].append(c2[c.index(i)])
    if i in d and len(final[i]) < 5:
        final[i].append(d2[d.index(i)])
    x += 1


# In[18]:


x = 0
keys = list(final.keys())
for k in keys:
    if k in a:
        keys[x] = a1[a.index(k)]
    if k in b:
        keys[x] = b1[b.index(k)]
    if k in c:
        keys[x] = c1[c.index(k)]
    if k in d:
        keys[x] = d1[d.index(k)]
    x += 1


# In[19]:


i = 0
k = list(final.keys())
for x in k:
    final[keys[i]] = final.pop(x)
    i += 1


# In[20]:


len(final)


# In[21]:


song = list(final.keys())
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x])/4 for x in range(0, len(final))]


# In[22]:


data = {'song':song,'artist':post5,'apple':post1,'boom':post2,'spotify':post3, 'deezer': post4, 'RT': postT}
df = pd.DataFrame(data)


# In[23]:


df.sort_values(by=['RT'], inplace=True)


# In[24]:


df['rank'] = [x for x in range(1, len(final) + 1)]


# In[25]:


df1 = df[['rank', 'song', 'artist']]
df1 = df1[:100]


# In[26]:


df1 = df1.set_index('rank')
df = df.set_index('rank')


# In[27]:


df1.to_csv(f'africa_week{w}-song100.csv')
df.to_csv(f'africa_week{w}.csv')


# In[28]:


df2 = pd.read_csv(f'africa_week{w - 1}-song100.csv')


# In[29]:


a = list(df2['song'])
a1 = a.copy()
x = 0
for i in a:
    if 'ft' in i:
        a[x] = i.replace('ft', '(ft') + ')'
    x += 1
x = 0
for i in a:
    if '(' in i:
        a[x] = i[: i.index('(')]
    a[x] = a[x].strip().lower()
    x += 1


# In[30]:


b = list(df1['song'])
b1 = b.copy()
x = 0
for i in b:
    if 'ft' in i:
        b[x] = i.replace('ft', '(ft') + ')'
    x += 1
x = 0
for i in b:
    if '(' in i:
        b[x] = i[: i.index('(')]
    b[x] = b[x].strip().lower()
    x += 1


# In[31]:


song = []
for x in b:
    if x in a:
        song.append(a1[a.index(x)])
    else:
        song.append(b1[b.index(x)])


# In[32]:


df1['song'] = song


# In[33]:


a = list(df2['song'])
b = list(df1['song'])
c = list(df2['weeks on chart'])
i = 0
prev = []
weeks = []
for x in b:
    if x in a:
        prev.append(a.index(x) + 1)
        weeks.append(c[i] + 1)
    else:
        prev.append(0)
        weeks.append(1)
    i += 1
df1['Previous week'] = prev
df1['weeks on chart'] = weeks


# In[34]:
newpath = f'{addr}\\webboard\\week{w}' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

df1.to_csv(f'africa_week{w}-song100.csv')
df1.to_csv(f'{addr}\\music-chart\\weekly charts\\weekly\\africa100.csv')
df1.to_json(f'{addr}\\webboard\\docs\\africa100.json')
df1.to_json(f'{addr}\\webboard\\week{w}\\africa100.json')

