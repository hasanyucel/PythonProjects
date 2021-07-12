import requests
import sqlite3
from bs4 import BeautifulSoup

db = sqlite3.connect('veritabani.sqlite')
im = db.cursor()
#im.execute("CREATE TABLE urunler (id, urun, fiyat)")
url = 'https://www.trendyol.com/cep-telefonu-x-c103498?pi=2'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
urunler = soup.find_all("div", {"class": "p-card-wrppr"})
i=0
#print(urunler[0].find_all("div", {"class": "price-promotion-container"}))
for urun in urunler:
    i = i + 1
    urun_id = urun['data-id']
    urun_adi = urun.find("div", {"class": "prdct-desc-cntnr-ttl-w two-line-text"}).find("span",{"class": "prdct-desc-cntnr-name"})["title"]
    fiyat = urun.find_all("div", {"class": "prc-box-sllng"})[0].text
    im.execute("INSERT INTO urunler VALUES (?,?,?)", (urun_id,urun_adi,fiyat))
    print(urun_id,urun_adi,fiyat)
db.commit()
db.close()


