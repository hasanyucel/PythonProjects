from GGAPI import GGAPI
api = GGAPI.GGAPI('x','y','z','w')

cargoService = api.getCargoService()
productService = api.getProductService()
saleService = api.getSaleService()
storeService = api.getStoreService()
userMessageService = api.getUserMessageService()                                                      

"""
print(dir(<serviceObject (like cargoService)>))
print(saleService.getActiveSales())
"""

satis = saleService.getSale('SC107774066','en')
print(satis)