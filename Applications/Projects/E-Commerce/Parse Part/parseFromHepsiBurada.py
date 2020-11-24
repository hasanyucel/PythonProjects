import requests
from bs4 import BeautifulSoup

def main():
    
    try:
        productPage = 'https://www.hepsiburada.com/philips-uyumlu-powerpro-city-compact-hepa-filtre-seti-p-hbv00000om9o4'
        page = requests.get(productPage)
        print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        parent = soup.find(id='offering-price')
        beforePoint = parent.select('span')[0]
        afterPoint = parent.select('span')[1]
        print (beforePoint.get_text() + '.' + afterPoint.get_text() + ' TL')
    except:
        print ("Price couldn't be scraped!")


main()