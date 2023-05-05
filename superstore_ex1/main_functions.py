from SuperStore import *

def menu_options():
    return ("---Menu---\n1.Print all products\n2.Print all clients\n3.Add new product to the store\n4.Add new client to the store"
          "\n5.Remove product\n6.Remove client\n7.Print all products under price\n"
          "8.Print the most expensive product\n9.Print all phones\n10.Print all laptops\n11.Print average phone price\n"
            "12.Print the biggest laptop screen\n13.Print the most common camara\n"
            "14.Print popular products\n15.Print all shirts\n16.Add new order\n17.Print all orders\nB. Press B  for the chart\n18.EXITE")


def product_details():
    product_type = int(input("Please press [1] to add SmartPhone or press [2] to add Laptop: "))
    product_id = int(input("Enter product ID with 8 digit numbers: "))
    product_brand = input("Enter product brand: ")
    product_model = input("Enter product model: ")
    product_year = int(input("Enter product year with 4 digit numbers: "))
    product_price = float(input("Enter product price: "))
    if product_type==2:
        laptop_cpu = input("Enter laptop CPU: ")
        laptop_hard_disk = float(input("Enter laptop hard dick: "))
        laptop_screnn = float(input("Enter laptop screen size: "))
        return Laptop(product_id,product_brand.capitalize(),product_model.capitalize(),product_year,product_price,laptop_cpu,laptop_hard_disk,laptop_screnn)
    if product_type==1:
        smart_cell_net = input("Enter cell net: ")
        smart_num_core = int(input("Enter number of cores: "))
        smart_cam_res = float(input("Enter camara resulotion: "))
        return Smartphone(product_id,product_brand.capitalize(),product_model.capitalize(),product_year,product_price,smart_cell_net,smart_num_core,smart_cam_res)

def client_details():
    client_id = int(input("Enter client ID:"))
    client_name = input("Enter client name:")
    client_email = input("Enter client email with the format -----@---:")
    client_adderss = input("Enter client adderss:")
    client_phone = input("Enter client phone number:")
    client_gender = input("Enter client gender:")
    return Client(client_id, client_name.capitalize(), client_email.capitalize(), client_adderss.capitalize(),client_phone, client_gender)

