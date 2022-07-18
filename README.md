# News Aggregator
I hastily created this small script to retrieve the top ten most recent stories from https://portswigger.net/daily-swig. As such, the software is rather lacking in features, solely scraping links for the articles with BeautifulSoup4 and sending them through the smtplib library. Only the emailComponents.py hardcoded fields should be altered, as the main is only logic based.

## Features

- Scrape article links from https://portswigger.net/daily-swig
- Send links outbound in a formatted email


## Lessons Learnt
By taking this project head on in a small time frame (2 days), I have given myself further confidence in my researching abilities. Alongside this, I have gained experience with web scraping using BS4, making HTTP requests utilising the Requests library, and the sending of emails from a Python script. Furthermore, my grasping of the Python language, and OOP as a whole have improved oncemore. 



## Dependencies

- BeautifulSoup4 (Version 4.11.1)
- Requests (Version 2.22.0)
