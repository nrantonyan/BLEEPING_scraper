import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.bleepingcomputer.com/")

soup = BeautifulSoup(req.content, 'html.parser')


top_articles = []

articles = soup.find_all('div', class_='bc_latest_news_text')

for a in articles:
    a_name = a.h4.text

    print(a_name)
