# The project get contributions count of a github user

from bs4 import BeautifulSoup 
import requests

def get_contributions(username):
    r = requests.get('https://github.com/'+username+'')
    source = BeautifulSoup(r.content,"lxml")

    a = (source.find_all('h2')[1]).text

    if(a.split()[0] == 'Popular'):
        a = (source.find_all('h2')[2]).text
        return a.split()[0]
    elif(a.split()[0] == 'Pinned'):
        a = (source.find_all('h2')[2]).text
        return a.split()[0]
    else:
        a = (source.find_all('h2')[1]).text
        return a.split()[0]

    # return a.split()

print(get_contributions('hasanyucel'))