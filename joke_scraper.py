from bs4 import BeautifulSoup
import requests
import random
source = requests.get('https://bestlifeonline.com/hilariously-silly-jokes/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

def getJoke():
    articles = soup.find("div", class_="main-content")

    jokes = articles.find_all('p')
    jokes_text = []
    for i in range(1,len(jokes), 2):
        # print(jokes[i].text)
        jokes_text.append(jokes[i].text)

    bot_joke = jokes_text[random.randint(0,len(jokes_text) - 1)]
    return bot_joke

