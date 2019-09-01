from bs4 import BeautifulSoup
import requests
from datetime import datetime

post = {
    "title": '',
    "date": '',
    "url": '',
    "imgUrl": '',
    "author": ''
}


url = "https://www.reddit.com/r/dankmemes/"

page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) 
soup = BeautifulSoup(page.content, 'html.parser')


for link in soup.findAll("div", class_ = "sitetable linklisting"):
    print(link.get('id'))
