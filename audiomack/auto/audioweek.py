# In[8]:

import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[2]:


from datetime import datetime
m = datetime.today().strftime('%B')
d = datetime.today().strftime('%d')
d = int(d)
w = datetime.today().strftime("%V")

addr = input('Enter your destination address: ')

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/afro-hip-hop')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 600)") 
    button = driver.find_element_by_class_name('button__arrow')
    button.click()
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    song = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
    mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
    for x in mydiv:
        song.append(x.text)
    for x in mydivs:
    	artist.append(x.text)
    data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\afrohiphop-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\hiphop\\audio_hiphop-week{w}.csv')
    driver.close()
except:
    pass



# In[9]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/verified-afrobeats')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 600)") 
    button = driver.find_element_by_class_name('button__arrow')
    button.click()
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    song = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
    mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
    for x in mydiv:
        song.append(x.text)
    for x in mydivs:
        artist.append(x.text)
    data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\afrobeat-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\afrobeat\\audio_afrobeat-week{w}.csv')
    driver.close()
except:
    pass



# In[10]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/alte-sounds')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 600)") 
    button = driver.find_element_by_class_name('button__arrow')
    button.click()
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    song = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
    mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
    for x in mydiv:
        song.append(x.text)
    for x in mydivs:
        artist.append(x.text)
    data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\alte-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\alte\\audio_alte-week{w}.csv')
    driver.close()
except:
    pass

# In[11]:

try:
    driver = webdriver.Firefox()
    driver.get('https://audiomack.com/audiomack-africa/playlist/afro-pop-hits')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 600)") 
    button = driver.find_element_by_class_name('button__arrow')
    button.click()
    content = driver.page_source
    soup = bs(content, 'html.parser') 
    song = []
    artist = []
    mydivs = soup.find_all("span", {'class': 'tracklist__track-artist u-trunc'})
    mydiv = soup.find_all("span", {'class': 'u-d-block u-trunc'})
    for x in mydiv:
        song.append(x.text)
    for x in mydivs:
        artist.append(x.text)
    data = {'Position': [x for x in range(1, len(song) + 1)] ,'song': song, 'artist': artist}
    df = pd.DataFrame(data)
    df = df.set_index('Position')
    df.to_csv(f'{addr}\\music-chart\\audiomack\\afropop-week{w}.csv')
    df.to_csv(f'{addr}\\music-chart\\weekly charts\\afropop\\audio_afropop-week{w}.csv')
    driver.close()
except:
    pass

# In[ ]:



