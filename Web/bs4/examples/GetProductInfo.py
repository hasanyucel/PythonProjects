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
    
    def getProductSeller(self):
        if self.soup.find_all("div",attrs={"class","pr-mb-mn"}):
            return self.soup.find_all("div",attrs={"class","pr-mb-mn"})[0].a["title"]
        else:
            return "-"

    def getEvaluationCount(self):
        if self.soup.find_all("a", attrs={"class","rvw-cnt-tx"}):
            evaluation_count = self.soup.find_all("a", attrs={"class","rvw-cnt-tx"})[0].text
            evaluation_count = evaluation_count.split(" ")
            return evaluation_count[0]
        else:
            return "-"

    def getQACount(self):
        if self.soup.find_all("a", attrs={"class","product-questions"}):
            qa_count = self.soup.find_all("a", attrs={"class","product-questions"})[0].text
            qa_count = qa_count.split(" ")
            return qa_count[0]
        else:
            return "-"