#!/usr/bin/env python
# coding: utf-8

# In[92]:


import pandas as pd
from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
w = int(w)
d = int(d)


# In[93]:

addr = input('Enter ur file destination: ')
df1 = pd.read_csv(f'apple_street-week{w}.csv', encoding= 'utf-8')
df2 = pd.read_csv(f'youtube_street-week{w}.csv', encoding= 'utf-8')


# In[94]:


df1 = df1[['song', 'artist']]
df2 = df2[['song', 'artist']]


# In[95]:


a = list(df1['song'])
a1 = a.copy()
a2 = list(df1['artist'])
x = 0
for i in a:
    i = i.lower()
    if 'remix' in i:
        a[x] = i.replace('remix', '(remix')
    if '(' in i:
        a[x] = a[x][: a[x].index('(')]
    a[x] = a[x].strip().lower()
    x += 1


# In[96]:


b = list(df2['song'])
b1 = b.copy()
b2 = list(df2['artist'])
x = 0
for i in b:
    if '(' not in i:
        b[x] = i[:i.index('-')]
    if '(' in i:
        if i.index('(') < i.index('-'):
              b[x] = b[x][:i.index('-')]
        else: 
            b[x] = b[x][i.index('-') + 1:]
    if 'Remix' in i:
        b[x] = b[x].replace('Remix', '(Remix')
    if '[' in i:
        b[x] = b[x].replace('[', '(')
    if '(' in b[x]:
        b[x] = b[x][: b[x].index('(')]
    b[x] = b[x].strip().lower()
    x += 1


# In[97]:


songs = a + b
songs = set(songs)


# In[99]:


songs = list(songs)


# In[100]:


final = {}


# In[101]:


x = 0
for i in songs:
    if i in a:
        final[i] = [a.index(i) + 1]
    else:
        final[i] = [250]


# In[102]:


x = 0
for i in songs:
    if i in b:
        final[i].append(b.index(i) + 1)
    else:
        final[i].append(200)


# In[103]:


x = 0
for i in songs:
    if i in a:
        final[i].append(a2[a.index(i)])
    if i in b and len(final[i]) < 3:
        final[i].append(b2[b.index(i)])
    x += 1


# In[105]:


x = 0
keys = list(final.keys())
for k in keys:
    if k in a:
        keys[x] = a1[a.index(k)]
    elif k not in a:
        keys[x] = b1[b.index(k)]
    x += 1


# In[111]:


i = 0
k = list(final.keys())
for x in k:
    final[keys[i]] = final.pop(x)
    i += 1


# In[114]:


song = list(final.keys())
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
postT = [(post1[x] + post2[x]/2) for x in range(0, len(final))]


# In[115]:


data = {'song':song,'artist':post3,'apple':post1,'youtube':post2,'RT': postT}
df = pd.DataFrame(data)


# In[116]:


df.sort_values(by=['RT'], inplace=True)


# In[117]:


df['rank'] = [x for x in range(1, len(final) + 1)]


# In[118]:


df1 = df[['rank', 'song', 'artist']]
df1 = df1[:50]


# In[119]:


df1 = df1.set_index('rank')
df = df.set_index('rank')


# In[120]:


df2 = pd.read_csv(f'street_week{w-1}-50.csv')


# In[121]:


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


# In[122]:


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


# In[123]:


song = []
for x in b:
    if x in a:
        song.append(a1[a.index(x)])
    else:
        song.append(b1[b.index(x)])


# In[124]:


df1['song'] = song


# In[125]:


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
        prev.append('-')
        weeks.append(1)
    i += 1
df1['Previous week'] = prev
df1['weeks on chart'] = weeks


# In[126]:


df1.to_csv(f'street_week{w}-50.csv')
df.to_csv(f'street_week{w}.csv')
df1.to_csv(f'{addr}\\music-chart\\weekly charts\\weekly\\street50.csv')
df1.to_json(f'{addr}\\webboard\\docs\\street50.json')
df1.to_json(f'{addr}\\webboard\\week{w}\\street50.json')

