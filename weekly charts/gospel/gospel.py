#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
w = int(w)
d = int(d)


# In[5]:

addr = input('Enter ur file destination: ')
df1 = pd.read_csv(f'apple_gospel-week{w}.csv')
df2 = pd.read_csv(f'boom_gospel-week{w}.csv')
df3 = pd.read_csv(f'youtube_gospel-week{w}.csv')


# In[6]:


df1 = df1[['song', 'artist']]
df2 = df2[['song', 'artist']]
df3 = df3[['song', 'artist']]


# In[7]:


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


# In[8]:


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


# In[9]:


c = list(df3['song'])
c1 = c.copy()
c2 = list(df3['artist'])
x = 0
for i in c:
    i = i.lower()
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


# In[10]:


songs = a + b + c
songs = set(songs)


# In[17]:


songs = list(songs)


# In[18]:


final = {}


# In[24]:


x = 0
for i in songs:
    if i in a:
        final[i] = [a.index(i) + 1]
    else:
        final[i] = [500]


# In[25]:


x = 0
for i in songs:
    if i in b:
        final[i].append(b.index(i) + 1)
    else:
        final[i].append(510)


# In[26]:


x = 0
for i in songs:
    if i in c:
        final[i].append(c.index(i) + 1)
    else:
        final[i].append(450)


# In[27]:


x = 0
for i in songs:
    if i in a:
        final[i].append(a2[a.index(i)])
    if i in b and len(final[i]) < 5:
        final[i].append(b2[b.index(i)])
    if i in c and len(final[i]) < 5:
        final[i].append(c2[c.index(i)])
    #if i in d and len(final[i]) < 5:
     #   final[i].append(d2[d.index(i)])
    x += 1


# In[29]:


x = 0
keys = list(final.keys())
for k in keys:
    if k in a:
        keys[x] = a1[a.index(k)]
    if k in b:
        keys[x] = b1[b.index(k)]
    if k in c:
        keys[x] = c1[c.index(k)]
    #if k in d:
     #   keys[x] = d1[d.index(k)]
    x += 1


# In[30]:


i = 0
k = list(final.keys())
for x in k:
    final[keys[i]] = final.pop(x)
    i += 1


# In[32]:


song = list(final.keys())
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
#post5 = [x[4] for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x])/3 for x in range(0, len(final))]


# In[33]:


data = {'song':song,'artist':post4,'apple':post1,'boom':post2,'youtube':post3,'RT': postT}
df = pd.DataFrame(data)


# In[34]:


df.sort_values(by=['RT'], inplace=True)


# In[35]:


df['rank'] = [x for x in range(1, len(final) + 1)]


# In[36]:


df1 = df[['rank', 'song', 'artist']]
df1 = df1[:50]


# In[37]:


df1 = df1.set_index('rank')
df = df.set_index('rank')


# In[38]:


df1.to_csv(f'week{w}-gospel50.csv')
df.to_csv(f'week{w}-gospel.csv')


# In[39]:


df2 = pd.read_csv(f'week{w-1}-gospel50.csv')


# In[40]:


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


# In[41]:


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


# In[42]:


song = []
for x in b:
    if x in a:
        song.append(a1[a.index(x)])
    else:
        song.append(b1[b.index(x)])


# In[43]:


df1['song'] = song


# In[44]:


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


# In[46]:


df1.to_csv(f'week{w}-gospel50.csv')
df1.to_csv(f'{addr}\\music-chart\\weekly charts\\weekly\\gospel50.csv')
df1.to_json(f'{addr}\\webboard\\docs\\gospel50.json')
df1.to_json(f'{addr}\\webboard\\week{w}\\gospel50.json')

