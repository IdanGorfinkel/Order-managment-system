from Product import Product

class Shirts(Product):

    def __init__(self,product_id,product_name,price,unit_in_stock):
        super().__init__(product_id,"SuperStore", "",2023,price)
        self.product_name = product_name
        self.unit_in_stock = unit_in_stock

    def __str__(self):
        return f"{super().__str__()},{self.product_name},{self.unit_in_stock}"

    def __repr__(self):
        old_repr=super().__repr__()
        return old_repr+str(self)

