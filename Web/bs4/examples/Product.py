class Product:
    def __init__(self,product_id, product_name, brand, seller, evaluation_count,qa_count,favorite,price,discounted_price,basket_price):
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.seller = seller
        self.evaluation_count = evaluation_count
        self.qa_count = qa_count
        self.favorite = favorite
        self.price = price
        self.discounted_price = discounted_price
        self.basket_price = basket_price