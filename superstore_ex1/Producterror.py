class Product:
    def __init__(self, product_id, brand, model, year, price):
        try:
            if type(product_id) != int:
                raise ValueError("Product ID must be an integer")
            if len(str(product_id)) != 8:
                raise TypeError("The length must contain 8 char")
            self.product_id = product_id
        except TypeError as e:
            print(f"{e}, producd ID changed to default")
            self.product_id = 11111111
        except ValueError as e:
            print(f"{e}, producd ID changed to default")
            self.product_id = 11111111

        try:
            if type(brand) != str:
                raise ValueError("Product Brand must be an string")
            self.brand = brand
        except ValueError as e:
            print(f"{e}, producd Brand changed to default")
            self.brand = "Iphone"
        try:
            if type(model) != str:
                raise ValueError("Product model must be an string")
            self.model = model
        except ValueError as e:
            print(f"{e}, producd model changed to default")
            self.model = "XXX5g"

        try:
            if type(year) != int:
                raise ValueError("Product year must be an int")
            if  year > 2022 or year < 2000:
                raise TypeError("Product year not in range")
            self.year = year
        except ValueError as e:
            print(f"{e}, producd year changed to default")
            self.year = 2020
        except TypeError as e:
            print(f"{e}, producd year changed to default")
            self.year = 2020

        self.price = price

    def print_me(self):
        return print(
            f"----{self.product_id}----\nbrand: {self.brand}\nmodel: {self.model}\nyear: {self.year}\nprice: {self.price}",
            end="")

    def __str__(self):
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"

    def __repr__(self):
        return str(self)

    def Is_popular(self):
        if self.year < 2017 and self.price < 3000:
            return True
        else:
            return False


p1 = Product(5555555, "apple", 555, 2012, 2500)
print(p1)
