#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
w = int(w)
d = int(d)


# In[2]:

addr = input('Enter ur file destination: ')
df1 = pd.read_csv(f'apple_afrohiphop-week{w}.csv', encoding='utf-8')
df2 = pd.read_csv(f'audio_hiphop-week{w}.csv', encoding='utf-8')
df3 = pd.read_csv(f'youtube_afrohiphop-week{w}.csv', encoding='utf-8')
df4 = pd.read_csv(f'boom_hiphop-week{w}.csv', encoding='utf-8')
df5 = pd.read_csv(f'spotify_afrohiphop-week{w}.csv', encoding='utf-8')
df6 = pd.read_csv(f'deezer_afrohiphop-week{w}.csv', encoding='utf-8')


# In[3]:


df1 = df1[['song', 'artist']]
df2 = df2[['song', 'artist']]
df3 = df3[['song', 'artist']]
df4 = df4[['song', 'artist']]
df5 = df5[['song', 'artist']]
df6 = df6[['song', 'artist']]


# In[1]:


a = list(df1['song'])
a1 = a.copy()
a2 = list(df1['artist'])
x = 0
for i in a:
    i = i.lower()
    if 'ft' in i:
        a[x] = i.replace('ft', '(ft')
    if 'feat' in i:
        a[x] = a[x].replace('feat', '(feat')
    if 'remix' in i:
        a[x] = a[x].replace('remix', '(remix')
    if '  ' in i:
        a[x] = a[x].replace('  ', ' ')
    if '(' in a[x]:
        a[x] = a[x][: a[x].index('(')]
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
    i = i.lower()
    if 'remix' in i:
        b[x] = i.replace('remix', '(remix')
    if 'ft' in i:
        b[x] = b[x].replace('ft', '(ft')
    if 'feat' in i:
        b[x] = b[x].replace('feat', '(feat')
    if '  ' in i:
        b[x] = b[x].replace('  ', ' ')
    if '(' in b[x]:
        b[x] = b[x][: b[x].index('(')]
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
    i = str(i).lower()
    c[x] = str(c[x])
    if 'ft' in i:
        c[x] = i.replace('ft', '(ft')
    if 'feat' in i:
        c[x] = c[x].replace('feat', '(feat')
    if 'remix' in i:
        c[x] = c[x].replace('remix', '(remix')
    if '  ' in i:
        c[x] = c[x].replace('  ', ' ')
    if '(' in c[x]:
        c[x] = c[x][: c[x].index('(')]
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
    i = i.lower()
    if 'ft' in i:
        d[x] = i.replace('ft', '(ft') + ')'
    if 'feat' in i:
        d[x] = d[x].replace('feat', '(feat')
    if 'remix' in i:
        d[x] = d[x].replace('remix', '(remix')
    if '  ' in d[x]:
        d[x] = d[x].replace('  ', ' ')
    x += 1
x = 0
for i in d:
    if '(' in i:
        d[x] = i[: i.index('(')]
    if '\\' in i:
        d[x] = d[x].replace('\\', '') 
    d[x] = d[x].strip().lower()
    x += 1


# In[8]:


e = list(df5['song'])
e1 = e.copy()
e2 = list(df5['artist'])
x = 0
for i in e:
    i = i.lower()
    if 'ft' in i:
        e[x] = e[x].replace('ft', '(ft')
    if 'feat' in i:
        e[x] = e[x].replace('feat', '(feat')
    if 'remix' in i:
        e[x] = e[x].replace('remix', '(remix')
    if '  ' in i:
        e[x] = e[x].replace('  ', ' ')
    if '(' in e[x]:
        e[x] = e[x][: e[x].index('(')]
    if '\\' in i:
        e[x] = e[x].replace('\\', '') 
    e[x] = e[x].strip().lower()
    x += 1


# In[9]:


f = list(df6['song'])
f1 = f.copy()
f2 = list(df6['artist'])
x = 0
for i in f:
    i = i.lower()
    if 'ft' in i:
        f[x] = f[x].replace('ft', '(ft')
    if 'feat' in i:
        f[x] = f[x].replace('feat', '(feat')
    if 'remix' in i:
        f[x] = f[x].replace('remix', '(remix')
    if '  ' in i:
        f[x] = f[x].replace('  ', ' ')
    if '(' in f[x]:
        f[x] = f[x][: f[x].index('(')]
    if '\\' in i:
        f[x] = f[x].replace('\\', '') 
    f[x] = f[x].strip().lower()
    x += 1


# In[10]:


songs = a + b + c + d + e + f
songs = set(songs)


# In[12]:


songs = list(songs)


# In[28]:


final = {}


# In[29]:


x = 0
for i in songs:
    if i in a:
        final[i] = [a.index(i) + 1]
    else:
        final[i] = [400]


# In[30]:


x = 0
for i in songs:
    if i in b:
        final[i].append(b.index(i) + 1)
    else:
        final[i].append(410)


# In[31]:


x = 0
for i in songs:
    if i in c:
        final[i].append(c.index(i) + 1)
    else:
        final[i].append(350)


# In[32]:


x = 0
for i in songs:
    if i in d:
        final[i].append(d.index(i) + 1)
    else:
        final[i].append(450)


# In[33]:


x = 0
for i in songs:
    if i in e:
        final[i].append(e.index(i) + 1)
    else:
        final[i].append(420)


# In[34]:


x = 0
for i in songs:
    if i in f:
        final[i].append(f.index(i) + 1)
    else:
        final[i].append(330)


# In[35]:


x = 0
for i in songs:
    if i in a:
        final[i].append(a2[a.index(i)])
    if i in b and len(final[i]) < 7:
        final[i].append(b2[b.index(i)])
    if i in c and len(final[i]) < 7:
        final[i].append(c2[c.index(i)])
    if i in d and len(final[i]) < 7:
        final[i].append(d2[d.index(i)])
    if i in e and len(final[i]) < 7:
        final[i].append(e2[e.index(i)])
    if i in f and len(final[i]) < 7:
        final[i].append(f2[f.index(i)])
    x += 1


# In[24]:


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
    if k in e:
        keys[x] = e1[e.index(k)]
    if k in f:
        keys[x] = f1[f.index(k)]
    x += 1


# In[25]:


i = 0
k = list(final.keys())
for x in k:
    final[keys[i]] = final.pop(x)
    i += 1


# In[38]:


song = list(final.keys())
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] for x in final.values()]
post6 = [x[5] for x in final.values()]
post7 = [x[6] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x] + post5[x] + post6[x])/6 for x in range(0, len(final))]


# In[39]:


data = {'song':song,'artist':post7,'apple':post1,'audiomark':post2,'youtube':post3, 'boom': post4, 'spotify': post5, 'deezer': post6, 'RT': postT}
df = pd.DataFrame(data)


# In[40]:


df.sort_values(by=['RT'], inplace=True)


# In[41]:


df['rank'] = [x for x in range(1, len(final) + 1)]


# In[42]:


df1 = df[['rank', 'song', 'artist']]
df1 = df1[:50]


# In[43]:


df1 = df1.set_index('rank')
df = df.set_index('rank')


# In[44]:


df1.to_csv(f'week{w}-hiphop50.csv')
df.to_csv(f'week{w}-hiphop.csv')


# In[45]:


df2 = pd.read_csv(f'week{w-1}-hiphop50.csv')


# In[46]:


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


# In[47]:


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


# In[48]:


song = []
for x in b:
    if x in a:
        song.append(a1[a.index(x)])
    else:
        song.append(b1[b.index(x)])


# In[49]:


df1['song'] = song


# In[50]:


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


# In[54]:


df1.to_csv(f'week{w}-hiphop50.csv')
df1.to_csv(f'{addr}\\music-chart\\weekly charts\\weekly\\hiphop50.csv')
df1.to_json(f'{addr}\\webboard\\docs\\hiphop50.json')
df1.to_json(f'{addr}\\webboard\\week{w}\\hiphop50.json')

