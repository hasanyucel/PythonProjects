import requests
from bs4 import BeautifulSoup

class ParseProduct:
    def __init__(self,link):
        r = requests.get(link)
        source = BeautifulSoup(r.content,"lxml")
        self.partName = source.select('h1.proName')[0].text.strip()
        self.partTitle = source.select('h2.proSubName')[0].text.strip()
        self.cost = (source.select('div.newPrice')[0].find('ins')).text.strip()

