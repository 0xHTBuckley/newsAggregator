#!/usr/bin/python3

import requests
import re
from bs4 import BeautifulSoup

url = 'https://portswigger.net/daily-swig'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.find_all('a', class_ = "noscript-post").get('href'))

for link in soup.find_all('a', class_ = "noscript-post", attrs={'href': re.compile("^/")}):
    # display the actual urls
    print(link.get('href')) 

    