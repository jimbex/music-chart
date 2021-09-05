#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
w = datetime.today().strftime("%V")
addr = input('Enter your file destination address: ')


# In[ ]:


import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[ ]:

try:
    driver = webdriver.Firefox()
    driver.get('https://www.deezer.com/en/playlist/4728415144')
    time.sleep(4)
    try:
        elem = driver.find_element_by_class_name('cookie-btn-label')
        elem.click()
    except:
        pass
    driver.execute_script("window.scrollTo(0,1200)")
    content1 = driver.page_source
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    content2 = driver.page_source
    driver.close()

    soup = bs(content1, 'html.parser') 
    mydiv1 = soup.find_all("div", {'itemprop': 'track'})
    soup = bs(content2, 'html.parser') 
    mydiv2 = soup.find_all("div", {'itemprop': 'track'})
    mydivs = mydiv1 + mydiv2
    div = []
    for x in mydivs:
        if x not in div:
            div.append(x)
        else:
            continue
        
    position = []
    songs = []
    artist = []
    for x in div:
        soup = bs(str(x), 'html.parser')
        position.append(int(soup.find("span", {'class': 'datagrid-track-number'}).text))
        soup = bs(str(x), 'html.parser')
        songs.append(soup.find("span", {'itemprop': 'name'}).text)
        soup = bs(str(x), 'html.parser')
        artist.append(soup.find("a", {'itemprop': 'byArtist'}).text)

    data = {'Position': position, 'song': songs, 'artist': artist}
    df = pd.DataFrame(data)
    df.to_csv(f'{addr}\\music-chart\\deezer\\afrohiphop-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\hiphop\\deezer_afrohiphop-week{w}.csv')
except:
    pass

# In[ ]:

try:
    driver = webdriver.Firefox()
    driver.get('https://www.deezer.com/en/playlist/1482254815')
    time.sleep(4)
    try:
        elem = driver.find_element_by_class_name('cookie-btn-label')
        elem.click()
    except:
        pass
    driver.execute_script("window.scrollTo(0,1200)")
    content1 = driver.page_source
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    content2 = driver.page_source
    driver.close()

    soup = bs(content1, 'html.parser') 
    mydiv1 = soup.find_all("div", {'itemprop': 'track'})
    soup = bs(content2, 'html.parser') 
    mydiv2 = soup.find_all("div", {'itemprop': 'track'})
    mydivs = mydiv1 + mydiv2
    div = []
    for x in mydivs:
        if x not in div:
            div.append(x)
        else:
            continue
            
    position = []
    songs = []
    artist = []
    for x in div:
        soup = bs(str(x), 'html.parser')
        position.append(int(soup.find("span", {'class': 'datagrid-track-number'}).text))
        soup = bs(str(x), 'html.parser')
        songs.append(soup.find("span", {'itemprop': 'name'}).text)
        soup = bs(str(x), 'html.parser')
        artist.append(soup.find("a", {'itemprop': 'byArtist'}).text)
    
    data = {'Position': position, 'song': songs, 'artist': artist}
    df = pd.DataFrame(data)
    df.to_csv(f'{addr}\\music-chart\\deezer\\afropop-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\afropop\\deezer_afropop-week{w}.csv')
except:
    pass


# In[ ]:


try:
    driver = webdriver.Firefox()
    driver.get('https://www.deezer.com/en/playlist/1440614715')
    time.sleep(4)
    try:
        elem = driver.find_element_by_class_name('cookie-btn-label')
        elem.click()
    except:
        pass
    driver.execute_script("window.scrollTo(0,1200)")
    content1 = driver.page_source
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    content2 = driver.page_source
    driver.close()
    
    soup = bs(content1, 'html.parser') 
    mydiv1 = soup.find_all("div", {'itemprop': 'track'})
    soup = bs(content2, 'html.parser') 
    mydiv2 = soup.find_all("div", {'itemprop': 'track'})
    mydivs = mydiv1 + mydiv2
    div = []
    for x in mydivs:
        if x not in div:
            div.append(x)
        else:
            continue
            
    position = []
    songs = []
    artist = []
    for x in div:
        soup = bs(str(x), 'html.parser')
        position.append(int(soup.find("span", {'class': 'datagrid-track-number'}).text))
        soup = bs(str(x), 'html.parser')
        songs.append(soup.find("span", {'itemprop': 'name'}).text)
        soup = bs(str(x), 'html.parser')
        artist.append(soup.find("a", {'itemprop': 'byArtist'}).text)
    
    data = {'Position': position, 'song': songs, 'artist': artist}
    df = pd.DataFrame(data)
    df.to_csv(f'{addr}\\music-chart\\deezer\\africa-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\africa\\deezer_africa-week{w}.csv')
except:
    pass

