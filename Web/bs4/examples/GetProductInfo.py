from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Product:
    global session
    global html_text
    
    def __init__(self,link):
        session = HTMLSession()
        html_text = session.get(link)
        html_text.html.render()
        self.soup = BeautifulSoup(html_text.html.html, 'lxml')

    def getProductName(self):
        if self.soup.find_all("h1", {"class": "pr-new-br"}):
            return self.soup.find_all("h1",attrs={"class","pr-new-br"})[0].span.text
        else:
            return "-"

    def getProductBrand(self):
        if self.soup.find_all("h1",attrs={"class","pr-new-br"}):
            return self.soup.find_all("h1",attrs={"class","pr-new-br"})[0].a.text
        else:
            return "-"
    
    