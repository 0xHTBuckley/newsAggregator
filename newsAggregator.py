#!/usr/bin/python3

import requests
import bs4
from emailComponents import formatEmail

url = 'https://portswigger.net/daily-swig'
htmlFile = requests.get(url)

def getArticleLinks(html):
    # Create Soup object and find all instances of class, returns array with URLs
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    lists = []
    while True:
        for link in soup.find_all('a', class_ = "noscript-post", href=True):
            lists.append("https://portswigger.net" + link['href'])
        return lists

def getArticleDescriptions(html):
    # Create Soup object and find descriptions of the articles
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    lists = []
    while True:
        for link in soup.find_all('span', class_ = "main"):
            lists.append(link.text)
        return lists
goddamn = getNewsLinks(htmlFile)
desc = getNewssLinks(htmlFile)

email = formatEmail(desc, goddamn)
print(email)

