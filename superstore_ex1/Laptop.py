from Product import Product

class Laptop(Product):
    def __init__(self,product_id,brand,model,year,price,CPU,hard_disk,screen):
        super().__init__(product_id,brand,model,year,price)
        self.CPU = CPU
        if type(hard_disk) == str:
            self.hard_disk = 100
        else:
            self.hard_disk = hard_disk
        if type(screen) == str:
            self.screen = 10
        else:
            self.screen =screen

    def print_me(self):
        old_print = super().print_me()
        return old_print, print(f"Product type:leptop \nCPU type:{self.CPU}\nHard disk:{self.hard_disk}\nScreen size:{self.screen}")

    def __str__(self):
        old_str=super().__str__()
        return old_str+f",leptop,{self.CPU},{self.hard_disk},{self.screen}"

    def __repr__(self):
        old_repr=super().__repr__()
        return old_repr+str(self)



