import requests, json, re

class GetProducts:

    global data
    
    def __init__(self,link):
        r = requests.get(link)
        self.data = json.loads(re.search(r'__SEARCH_APP_INITIAL_STATE__=(.*?\}\});', r.text).group(1))

    def getAllData(self):
        return self.data

    def getTotalProductCount(self):
        return self.data["totalCount"]

    def getAllProductIdUrlDict(self):
        ids = dict()
        for i in range (len(self.data["products"])):
            ids.update({str(self.data["products"][i]["id"]):'https://www.trendyol.com'+self.data["products"][i]["url"]})
        return ids