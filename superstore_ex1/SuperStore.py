from __future__ import annotations
from Client import Client
from Product import Product
import csv
from Laptop import Laptop
from Smartphone import Smartphone
from statistics import mean
from Shirts import Shirts
from Order import Order
from ClientNotFoundError import ClientNotFoundError
from ShirtNotFoundError import ShirtNotFoundError

class SuperStore:

    def __init__(self, products, clients,shirts,orders):

        with open(products, "r", newline="") as file_products:
            reader_product = csv.reader(file_products)
            next(reader_product)

            self.products: list[Smartphone | Laptop | Shirts] = []
            for row_p in reader_product:
                if row_p[1] == "laptop":
                    row_p0 = int(row_p[0])
                    row_p4 = int(row_p[4])
                    row_p5 = float(row_p[5])
                    row_p7 = float(row_p[7])
                    row_p8 = float(row_p[8])
                    row_p = [Laptop(row_p0, row_p[2], row_p[3], row_p4, row_p5,row_p[6],row_p7,row_p8)]
                    self.products +=row_p
                elif row_p[1] == "smartphone":
                    row_p0 = int(row_p[0])
                    row_p4 = int(row_p[4])
                    row_p5 = float(row_p[5])
                    row_p10 = int(row_p[10])
                    row_p11 = float(row_p[11])
                    row_p = [Smartphone(row_p0, row_p[2], row_p[3], row_p4, row_p5,row_p[9],row_p10,row_p11)]
                    self.products+=row_p

        with open(shirts, "r", newline="") as file_shirts:
            reader_shirts = csv.reader(file_shirts)
            next(reader_shirts)

            for row_s in reader_shirts:
                row_s0 = int(row_s[0])
                row_s2 = float(row_s[2])
                row_s3 = int(row_s[3])
                row_s = [Shirts(row_s0,row_s[1],row_s2,row_s3)]
                self.products +=row_s



        with open(clients, "r", newline="") as file_clients:
            reader_client = csv.reader(file_clients)
            next(reader_client)

            self.clients = []
            for row_c in reader_client:
                row_c0 = int(row_c[0])
                row_c = Client(row_c0, row_c[1], row_c[2], row_c[3], row_c[4], row_c[5])
                self.add_client(row_c)

        with open(orders, "r",newline="") as file_orders:
            reader_orders = csv.reader(file_orders)
            next(reader_orders)

            self.orders=[]
            for row_o in reader_orders:
                row_o0 = int(row_o[0])
                row_o1 = int(row_o[1])
                row_o2 = int(row_o[2])
                row_o3 = int(row_o[3])
                row_o = Order(row_o0,row_o1,row_o2,row_o3)
                self.add_order_from_csv(row_o)


    def print_products(self):
        for pro in self.products:
            print(pro)

    def print_orders(self):
        for order in self.orders:
            print(order)

    def get_product(self, product_id:int):
        for product in self.products:
            if product_id == product.product_id:
                return product
        return None

    # def add_product(self, new_product):
    #     for pro in self.products:
    #         if pro.product_id == new_product.product_id:
    #             return False
    #     self.products.append(new_product)
    #     return True


    def remove_product(self, product_remove_id:int):
        for pro in self.products:
            if pro.product_id == product_remove_id:
                self.products.remove(pro)
                return True
        return False

    def get_all_by_brand(self, brand_name: str):
        brand_lst = []
        for pro in self.products:
            if pro.brand == brand_name:
                brand_lst.append(pro)
        return brand_lst

    def get_all_by_price_under(self,max_price:int):
        in_price_value =[]
        for product in self.products:
            if product.price<max_price:
                in_price_value.append(product)
        return in_price_value

    def get_most_expensive_product(self):
        prices = []
        for product in self.products:
            prices.append(product.price)
        high_value = max(prices)
        for pro in self.products:
            if high_value == pro.price:
                return pro

    def print_clients(self):
        for client in self.clients:
            print(client)

    def get_client(self, client_id:int):
        for client in self.clients:
            if client_id == client.client_id:
                return client
        return None

    def add_client(self, new_client:Client):
        for client in self.clients:
            if client.client_id == new_client.client_id:
                return False
        self.clients.append(new_client)
        return True

    def remove_client(self, client_remove_id:int):
        for client in self.clients:
            if client.client_id == client_remove_id:
                self.clients.remove(client)
                return True
        return False

    def get_all_phones(self):
        all_phones =[]
        for p in self.products:
            if type(p) is Smartphone:
                all_phones.append(p)
        return all_phones

    def get_all_leptops(self):
        all_leptop = []
        for l in self.products:
            if type(l) is Laptop:
                all_leptop.append(l)
        return all_leptop

    def phone_average_price(self):
        prices = []
        for phone in self.get_all_phones():
            prices.append(phone.price)
        return mean(prices)

    def get_max_screen(self):
        screen_lst =[]
        for s in self.get_all_leptops():
            screen_lst.append(s.screen)
        return max(screen_lst)

    def get_common_cam(self):
        res =[]
        for r in self.get_all_phones():
            res.append(r.cam_res)
        return max(res,key=res.count)

    def list_popular(self):
        popular =[]
        for p in self.products:
            if p.Is_popular():
                popular.append(p)
        return popular

    def __iadd__(self, other:Smartphone | Laptop | Shirts):
        for pro in self.products:
            if pro.product_id == other.product_id:
                return self
        self.products.append(other)
        return self

    def __len__(self):
        return len(self.products)


    def get_shirt(self,shirt_id : int):
        for shirt in self.products:
            if shirt.product_id == shirt_id and type(shirt) == Shirts:
                return shirt
        return None

    def get_max_order_id(self):
        orders_id = []
        for i in self.orders:
            orders_id.append(i.order_id)
        return max(orders_id)

    def add_order_from_csv(self, new_order:Order):
        for order in self.orders:
            if order.order_id == new_order.order_id:
                return False
        self.orders.append(new_order)
        return True

    def print_all_shirts(self):
        for shirt in self.products:
            if type(shirt) == Shirts:
                print(shirt)

    def get_all_shirts(self):
        shirt_lst=[]
        for shirt in self.products:
            if type(shirt) == Shirts:
                shirt_lst.append(shirt)
        return shirt_lst

    def print_all_orders(self):
        for order in self.orders:
            print(order)

    def add_order(self,client_id: int,product_id: int,quantity: int):
        order_id = self.get_max_order_id()+1

        if self.get_client(client_id) == None:
            raise ClientNotFoundError("Client id does not exist")
        if self.get_product(product_id) == None:
            raise ShirtNotFoundError("Product id does not exist")
        if type(self.get_product(product_id)) != Shirts:
            if quantity >1:
                raise ValueError("Out of stock")
        if type(self.get_product(product_id)) == Shirts:
            if self.get_shirt(product_id).unit_in_stock < quantity :
                raise ValueError("Out of stock")

            new_order = Order(order_id, client_id, product_id, quantity)
            self.orders.append(new_order)

# super1 = SuperStore(products="products_supply.csv", clients="clients.csv",shirts="shirts.csv",orders="orders.csv")



