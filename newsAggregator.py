#!/usr/bin/python3

import requests
import bs4

url = 'https://portswigger.net/daily-swig'
htmlFile = requests.get(url)

def getNewsLinks(html):
    # Create Soup object and find all instances of class, returns array with URLs
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    lists = []
    while True:
        for link in soup.find_all('a', class_ = "noscript-post", href=True):
            lists.append("https://portswigger.net" + link['href'])
        return lists
