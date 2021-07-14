import requests
import sqlite3
from bs4 import BeautifulSoup

db = sqlite3.connect('veritabani.sqlite')
cursor = db.cursor()
#cursor.execute("CREATE TABLE products (id, product, price)")
url = 'https://www.trendyol.com/cep-telefonu-x-c103498'
for i in range(100):
    html_text = requests.get(url,params={'pi': str(i)}).text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.find_all("div", {"class": "p-card-wrppr"})
    for product in products:
        product_id = product['data-id']
        product_name = product.find("div", {"class": "prdct-desc-cntnr-ttl-w two-line-text"}).find("span",{"class": "prdct-desc-cntnr-name"})["title"]
        price = product.find_all("div", {"class": "prc-box-sllng"})[0].text
        cursor.execute("INSERT INTO products VALUES (?,?,?)", (product_id,product_name,price))
        #print(product_id,product_name,price)
    db.commit()
db.close()