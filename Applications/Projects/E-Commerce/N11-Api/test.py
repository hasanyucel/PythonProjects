import zeep
catwsdl  = 'https://api.n11.com/ws/CategoryService.wsdl'
citywsdl = 'https://api.n11.com/ws/CityService.wsdl'
salewsdl = 'https://api.n11.com/ws/OrderService.wsdl'
prodwsdl = 'https://api.n11.com/ws/ShipmentService.wsdl'
client1 = zeep.Client(wsdl=catwsdl)
client2 = zeep.Client(wsdl=citywsdl)
client3 = zeep.Client(wsdl=salewsdl)
client4 = zeep.Client(wsdl=prodwsdl)
key=[{'appKey' : 'x','appSecret' : 'y'}]
#print(client1.service.GetTopLevelCategories(auth=key))
#print(client2.service.GetCity('38'))
#print(client3.service.OrderList(key))
print(client4.service.GetShipmentTemplateList(key))