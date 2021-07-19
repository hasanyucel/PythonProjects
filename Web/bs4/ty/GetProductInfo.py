import requests, json, re, os

class GetProductInfo:

    global data
    
    def __init__(self,link):
        r = requests.get(link)
        self.data = json.loads(re.search(r'PRODUCT_DETAIL_APP_INITIAL_STATE__=(.*?\}\});', r.text).group(1))
        
    def getProductID(self):
        return self.data["product"]["id"]

    def saveImages(self):
        images = ['https://www.trendyol.com' + img for img in self.data['product']['images']]
        if not os.path.exists('images/'+str(self.data["product"]["id"])+''):
            os.makedirs('images/'+str(self.data["product"]["id"])+'')
        i = 1
        for image in images:
            response = requests.get(image)
            file = open('images/'+str(self.data["product"]["id"])+'/'+str(i)+'.jpg', 'wb')
            file.write(response.content)
            file.close()
            i = i + 1

    def getProductName(self):
        return self.data["product"]["name"]

    def getProductOrginalPrice(self):
        return self.data["product"]["price"]["originalPrice"]["value"]

    def getProductSellingPrice(self):
        return self.data["product"]["price"]["sellingPrice"]["value"]
    
    def getProductDiscountedPrice(self):
        return self.data["product"]["price"]["discountedPrice"]["value"]

    def getProductBrand(self):
        return self.data["product"]["metaBrand"]["name"]

    def getProductSellerName(self):
        return self.data["product"]["merchant"]["name"]
    
    def getProductSellerScore(self):
        return self.data["product"]["merchant"]["sellerScore"]

    def getProductSellerCityName(self):
        return self.data["product"]["merchant"]["cityName"]

    def getProductSellerOfficialName(self):
        return self.data["product"]["merchant"]["officialName"]
    
    def getProductSellerTaxNumber(self):
        return self.data["product"]["merchant"]["taxNumber"]

    def getProductURL(self):
        return 'https://www.trendyol.com'+self.data["product"]["url"]

    def getProductRatingCount(self):
        return self.data["product"]["ratingScore"]["totalRatingCount"]

    def getProductAverageRating(self):
        return self.data["product"]["ratingScore"]["averageRating"]

    def getProductTotalCommentCount(self):
        return self.data["product"]["ratingScore"]["totalCommentCount"]

    def getProductFavoriteCount(self):
        return self.data["product"]["favoriteCount"]

    def getAllProductData(self):
        return self.data["product"]

    def getProductMerhactCount(self):
        return len(self.data["product"]["otherMerchants"]) + 1

    def getProductAllMerchantNames(self):
        merchants = ""
        count = len(self.data["product"]["otherMerchants"])
        for i in range (count):
            merchants = merchants + "," + self.data["product"]["otherMerchants"][i]["merchant"]["name"]
        return self.data["product"]["merchant"]["name"]+merchants
    