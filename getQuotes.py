import requests
from bs4 import BeautifulSoup
from random import randrange

def getQuote():
    url = 'https://www.brainyquote.com/topics/random-quotes'
   
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    quotes = soup.find_all("div", attrs={'class':'clearfix'})
    q = quotes[randrange(len(quotes))]
    q_text = q.find("a", attrs={'title':'view quote'}).text
    q_author = q.find("a", attrs={'title':'view author'}).text
    
    fmt_text = "{} ~ {}".format(q_text, q_author)

    return fmt_text