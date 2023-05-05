class Product:
    def __init__(self,product_id,brand,model,year,price):
        if len(str(product_id)) < 2:
            self.product_id = 11111111
        else:
            self.product_id=product_id

        self.brand=brand
        self.model=model
        if year>2023 or year<1970:
            self.year = 2020
        else:
            self.year=year
        self.price=price

    def print_me(self):
        return print(f"----{self.product_id}----\nbrand: {self.brand}\nmodel: {self.model}\nyear: {self.year}\nprice: {self.price}",end="")

    def __str__(self):
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"
    def __repr__(self):
        return str(self)

    def Is_popular(self):
        if self.year < 2017 and self.price < 3000:
            return True
        else:
            return False



