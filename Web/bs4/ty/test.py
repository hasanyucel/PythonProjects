from GetProductInfo import *
import sqlite3,timeit,json
from rich import print

#db = sqlite3.connect('../veritabani.sqlite')
#cursor = db.cursor()
#cursor.execute("select * from products")
#rows = cursor.fetchall()
#start = timeit.default_timer()
#for row in rows:
#    product = GetProductInfo(row[2])
#    #print(product.getProductID())
#    
#db.close()
#stop = timeit.default_timer()
#print('Time: ', stop - start)

product = GetProductInfo("https://www.trendyol.com/apple/iphone-11-64gb-siyah-cep-telefonu-apple-turkiye-garantili-aksesuarsiz-kutu-p-64074791")
print(product.getAllProductData())