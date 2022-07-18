#!/usr/bin/python3

import requests
import bs4
import smtplib
import ssl
from emailComponents import formatEmail, emailMsg, password

scrapeURL = 'https://portswigger.net/daily-swig'
htmlFile = requests.get(scrapeURL)

def getArticleLinks(html):
    # Create Soup object and find all instances of "noscript-post" class, returns array with URLs.
    
    soupObj = bs4.BeautifulSoup(html.content, 'html.parser')
    URLs = []
    
    while True:
        for link in soupObj.find_all('a', class_ = "noscript-post", href=True):
            URLs.append("https://portswigger.net" + link['href'])
        return URLs

def sendEmail(password, email):

    contextDefault = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port = 465, context = contextDefault) as server:
            server.login(email['From'], password)
            server.sendmail(email['From'], email['To'], email.as_string())
    except Exception:
        print("Error with sending email!")

articleLink = getArticleLinks(htmlFile)

emailMsg.set_content(formatEmail(articleLink))

sendEmail(password, emailMsg)