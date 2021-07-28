from GetProductInfo import *
from GetProducts import *
import sqlite3,timeit,json
from rich import print

#Kategori linklerini alır sqlite dbye
##----------------------------------------------------------------------------
#url = "https://www.trendyol.com/cep-telefonu-x-c103498"
#products = GetProducts(url)
#productCount = products.getTotalProductCount()
#productPage = productCount / 24 
#db = sqlite3.connect('veritabani.sqlite')
#cursor = db.cursor()
##cursor.execute("CREATE TABLE products (id, url)")
#start = timeit.default_timer()
#urls = []
#for i in range(1,int(productPage)+2):
#    urls.append(url+"?pi="+str(i))
#for url in urls:
#    products = GetProducts(url)
#    idAndUrl = products.getAllProductIdUrlDict()
#    for x in idAndUrl:
#        cursor.execute("INSERT INTO products VALUES (?,?)", (x,idAndUrl[x]))
#    db.commit()
#db.close()
#stop = timeit.default_timer()
#print('Time: ', stop - start) 
##----------------------------------------------------------------------------

url = "https://www.trendyol.com/gamepower/jin-siyah-7-1-kulakustu-kulaklik-p-85885621?boutiqueId=559106&merchantId=133183"
product = GetProductInfo(url)
print(product.getProductBarcode())
