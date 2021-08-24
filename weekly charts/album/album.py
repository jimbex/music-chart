#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
w = datetime.today().strftime('%V')
w = int(w)
d = int(d)


# In[79]:

addr = input('Enter ur file destination: ')
df1 = pd.read_csv(f'apple_album-week{w}.csv', encoding='utf-8')
df2 = pd.read_csv(f'audiomack_album-week{w}.csv', encoding='utf-8')
df3 = pd.read_csv(f'deezer_album-week{w}.csv', encoding='utf-8')
df4 = pd.read_csv(f'boom_album-week{w}.csv', encoding='utf-8')


# In[80]:


df1 = df1[['album', 'artist']]
df2 = df2[['album', 'artist']]
df3 = df3[['album', 'artist']]


# In[81]:


a = list(df1['album'])
a1 = a.copy()
a2 = list(df1['artist'])
x = 0
for i in a:
    i = i.lower()
    if '  ' in i:
        a[x] = a[x].replace('  ', ' ')
    if ',' in i:
        a[x] = a[x].replace(',', '')
    if '-' in i:
        a[x] = a[x].replace('-', '(-')
    if '(' in i:
        a[x] = i[: i.index('(')]
    if '\\' in i:
        a[x] = a[x].replace('\\', '') 
    a[x] = a[x].strip().lower()
    x += 1


# In[82]:


b = list(df2['album'])
b1 = b.copy()
b2 = list(df2['artist'])
x = 0
for i in b:
    i = i.lower()
    if ' ep' in i:
        if '- ep' in i:
            b[x] = i.replace('- ep', ' (ep')
        else:
            b[x] = i.replace(' ep', ' (ep')
    if '  ' in i:
        b[x] = b[x].replace('  ', ' ')
    if '\\' in i:
        b[x] = b[x].replace('\\', '') 
    if ',' in i:
        b[x] = b[x].replace(',', '')
    if '-' in i:
        b[x] = b[x].replace('-', '(-')
    if '(' in b[x]:
        b[x] = b[x][: b[x].index('(')]
    b[x] = b[x].strip().lower()
    x += 1


# In[83]:


c = list(df3['album'])
c1 = c.copy()
c2 = list(df3['artist'])
x = 0
for i in c:
    i = i.lower()
    if ' ep' in i:
        if '- ep' in i:
            c[x] = i.replace('- ep', ' (ep')
        else:
            c[x] = i.replace(' ep', ' (ep')
    if '  ' in i:
        c[x] = c[x].replace('  ', ' ')
    if '\\' in i:
        c[x] = c[x].replace('\\', '') 
    if ',' in i:
        c[x] = c[x].replace(',', '')
    if '-' in i:
        c[x] = c[x].replace('-', '(-')
    if '(' in c[x]:
        c[x] = c[x][: c[x].index('(')]
    c[x] = c[x].strip().lower()
    x += 1


# In[84]:


d = list(df4['album'])
d1 = d.copy()
x = 0
for i in d:
    i = i.lower()
    if ' ep' in i:
        if '- ep' in i:
            d[x] = i.replace('- ep', ' (ep')
        else:
            d[x] = i.replace(' ep', ' (ep')
    if '  ' in d[x]:
        d[x] = d[x].replace('  ', ' ')
    if '\\' in i:
        d[x] = d[x].replace('\\', '') 
    if ',' in i:
        d[x] = d[x].replace(',', '') 
    if '-' in i:
        d[x] = d[x].replace('-', '(-')
    if '(' in d[x]:
        d[x] = d[x][: d[x].index('(')]
    
    d[x] = d[x].strip().lower()
    x += 1


# In[85]:


albums = a + b + c + d
albums = set(albums)


# In[87]:


len(albums)


# In[88]:


albums = list(albums)


# In[89]:


final = {}


# In[90]:


x = 0
for i in albums:
    if i in a:
        final[i] = [a.index(i) + 1]
    else:
        final[i] = [500]


# In[91]:


x = 0
for i in albums:
    if i in b:
        final[i].append(b.index(i) + 1)
    else:
        final[i].append(510)


# In[92]:


x = 0
for i in albums:
    if i in c:
        final[i].append(c.index(i) + 1)
    else:
        final[i].append(450)


# In[93]:


x = 0
for i in albums:
    if i in d:
        final[i].append(d.index(i) + 1)
    else:
        final[i].append(520)


# In[94]:


x = 0
for i in albums:
    if i in a:
        final[i].append(a2[a.index(i)])
    if i in b and len(final[i]) < 6:
        final[i].append(b2[b.index(i)])
    if i in c and len(final[i]) < 6:
        final[i].append(c2[c.index(i)])
    x += 1


# In[96]:


x = 0
keys = list(final.keys())
for k in keys:
    if k in a:
        keys[x] = a1[a.index(k)]
    if k in b:
        keys[x] = b1[b.index(k)]
    if k in c:
        keys[x] = c1[c.index(k)]
    x += 1


# In[97]:


i = 0
k = list(final.keys())
for x in k:
    final[keys[i]] = final.pop(x)
    i += 1


# In[98]:


len(final)


# In[99]:


album = list(final.keys())
post1 = [x[0] for x in final.values()]
post2 = [x[1] for x in final.values()]
post3 = [x[2] for x in final.values()]
post4 = [x[3] for x in final.values()]
post5 = [x[4] if len(x) > 4 else 'NA' for x in final.values()]
postT = [(post1[x] + post2[x] + post3[x] + post4[x]/4) for x in range(0, len(final))]


# In[100]:


data = {'album':album,'artist':post5,'apple':post1,'audiomark':post2,'deezer':post3, 'boom': post4, 'RT': postT}
df = pd.DataFrame(data)


# In[101]:


df.sort_values(by=['RT'], inplace=True)


# In[102]:


df['rank'] = [x for x in range(1,len(final) + 1)]


# In[103]:


df1 = df[['rank', 'album', 'artist']]
df1 = df1[:100]


# In[104]:


df1 = df1.set_index('rank')
df = df.set_index('rank')


# In[105]:


df2 = pd.read_csv(f'week{w-1}-album100.csv')


# In[106]:


a = list(df2['album'])
b = list(df1['album'])
c = list(df2['weeks on chart'])
i = -1
prev = []
weeks = []
for x in b:
    i += 1
    if x in a:
        prev.append(a.index(x) + 1)
        weeks.append(c[a.index(x)] + 1)
    else:
        prev.append(0)
        weeks.append(1)
df1['Previous week'] = prev
df1['weeks on chart'] = weeks


# In[107]:


df1.to_csv(f'week{w}-album100.csv')
df.to_csv(f'week{w}.csv')
df1.to_csv(f'{addr}\\music-chart\\weekly charts\\weekly\\album100.csv')
df1.to_json(f'{addr}\\webboard\\docs\\album100.json')
df1.to_json(f'{addr}\\webboard\\week{w}\\album100.json')

