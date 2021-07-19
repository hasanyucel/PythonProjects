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

product = GetProductInfo("https://www.trendyol.com/apple/iphone-12-pro-max-512gb-mavi-cep-telefonu-apple-turkiye-garantili-p-65276594")
print(product.getProductAllMerchantNames())


#import requests, json, re, os
#
#r = requests.get("https://www.trendyol.com/cep-telefonu-x-c103498")
#data = json.loads(re.search(r'__SEARCH_APP_INITIAL_STATE__=(.*?\}\});', r.text).group(1))
#print(data)