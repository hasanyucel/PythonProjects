import sqlite3
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import timeit
import time

session = HTMLSession()
db = sqlite3.connect('veritabani.sqlite')
cursor = db.cursor()
#cursor.execute("CREATE TABLE product_details (product_id, product_name, brand, seller, evaluation_count,qa_count,favorite,price,discounted_price,basket_price)")
cursor.execute("select * from products")
rows = cursor.fetchall()
start = timeit.default_timer()
for row in rows:
    product_id = row[0]
    product_name = row[1]
    url = row[2]
    html_text = session.get(url)
    html_text.html.render()
    soup = BeautifulSoup(html_text.html.html, 'lxml')
    brand = soup.find_all("h1",attrs={"class","pr-new-br"})[0].a.text
    #------------------------------------------------------------------------------------------
    seller = soup.find_all("div",attrs={"class","merchant-box-wrapper"})
    if seller:
        seller = soup.find_all("div",attrs={"class","merchant-box-wrapper"})[0].a.text
    else:
        seller = "-"
    #------------------------------------------------------------------------------------------
    evaluation_count = soup.find_all("a", attrs={"class","rvw-cnt-tx"})
    if evaluation_count:
        evaluation_count = soup.find_all("a", attrs={"class","rvw-cnt-tx"})[0].text
        evaluation_count = evaluation_count.split(" ")
    else:
        evaluation_count = "-"
    #------------------------------------------------------------------------------------------
    qa_count = soup.find_all("a", attrs={"class","product-questions"})
    if qa_count:
        qa_count = soup.find_all("a", attrs={"class","product-questions"})[0].text
        qa_count = qa_count.split(" ")
    else:
        qa_count = "-"
    #------------------------------------------------------------------------------------------
    favorite = soup.find_all("div", attrs={"class","fv-dt"})
    if favorite:
        favorite = soup.find_all("div", attrs={"class","fv-dt"})[0].text
        favorite = favorite.split(" ")
    else:
        favorite = "-"
    #------------------------------------------------------------------------------------------
    price = soup.find_all("span", attrs={"class","prc-org"})
    if price:
        price = soup.find_all("span", attrs={"class","prc-org"})[0].text
    else:
        price = "-"
    #------------------------------------------------------------------------------------------
    discounted_price = soup.find_all("span", attrs={"class","prc-slg"})
    if discounted_price:
        discounted_price = soup.find_all("span", attrs={"class","prc-slg"})[0].text
    else:
        discounted_price = "-"
    #------------------------------------------------------------------------------------------
    basket_price = soup.find_all("div", attrs={"class","pr-bx-pr-dsc"})
    if basket_price:
        basket_price = soup.find_all("div", attrs={"class","pr-bx-pr-dsc"})[0].span.text
    else:
        basket_price = "-"
    #------------------------------------------------------------------------------------------
    print(product_id, product_name, brand, seller, evaluation_count[0],qa_count[0],favorite[0],price,discounted_price,basket_price)
    cursor.execute("INSERT INTO product_details VALUES (?,?,?,?,?,?,?,?,?,?)", (product_id, product_name, brand, seller, evaluation_count[0],qa_count[0],favorite[0],price,discounted_price,basket_price))
    db.commit()
    #time.sleep(3)
db.close()
stop = timeit.default_timer()
print('Time: ', stop - start) 