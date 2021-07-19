import requests
import sqlite3
from bs4 import BeautifulSoup
import timeit

db = sqlite3.connect('veritabani.sqlite')
cursor = db.cursor()
cursor.execute("CREATE TABLE products (id, product, link)")
url = 'https://www.trendyol.com/sr?wb=794&wc=110304'
start = timeit.default_timer()
for i in range(40):
    html_text = requests.get(url,params={'pi': str(i)}).text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.find_all("div", {"class": "p-card-wrppr"})
    for product in products:
        product_id = product['data-id']
        product_name = product.find("div", {"class": "prdct-desc-cntnr-ttl-w two-line-text"}).find("span",{"class": "prdct-desc-cntnr-name"})["title"]
        link = product.find('a', href=True)
        link = "https://www.trendyol.com"+link["href"]
        cursor.execute("INSERT INTO products VALUES (?,?,?)", (product_id,product_name,link))
        #print(product_id,product_name,link)
    db.commit()
db.close()
stop = timeit.default_timer()
print('Time: ', stop - start) 