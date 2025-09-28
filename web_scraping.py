import requests
from bs4 import beautifulsoup

def scraping():
    url = "https://www.sensacine.com/noticias/cine/noticias-1000013021"
    response = requests.get(url)
    soup = beautifulsoup(response.text, 'html.parser')
    for item in soup.find_all("h2",class_="bo-h2"):
        print(item.text)