wsdl = 'https://api.n11.com/ws/ShipmentService.wsdl'
from zeep import Client, Settings
settings = Settings(strict=False)
key=[{'appKey' : 'x','appSecret' : 'y'}]
client = Client(wsdl=wsdl, settings=settings)
print(client.service.GetShipmentTemplateList(key))

