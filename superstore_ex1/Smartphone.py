from Product import  Product

class Smartphone(Product):
    def __init__(self,product_id,brand,model,year,price,cell_net,num_cores,cam_res):
        super().__init__(product_id,brand,model,year,price)
        self.cell_net = cell_net
        if type(num_cores) == str:
            self.num_cores = 2
        else:
            self.num_cores = int(num_cores)
        if type(cam_res)== str:
            self.cam_res = 100
        else:
            self.cam_res = cam_res

    def print_me(self):
        old_print = super().print_me()
        return old_print, print(f"Product type:smartphone\nCell network:{self.cell_net}\nNumber of cores:{self.num_cores}\nCamara resulotion:{self.cam_res}")

    def __str__(self):
        old_str = super().__str__()
        return old_str+f",smartphone,{self.cell_net},{self.num_cores},{self.cam_res}"

    def __repr__(self):
        old_repr=super().__repr__()
        return old_repr+str(self)


