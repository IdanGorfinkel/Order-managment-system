
import shirt_orders_analysis
from PressBerror import PressBerror
from main_functions import *


# super1 = SuperStore(products="products_supply.csv", clients="clients.csv")


def menu():
    super1 = SuperStore(products="products_supply.csv", clients="clients.csv",shirts="shirts.csv",orders="orders.csv")

    while True:
        print(menu_options())
        try:
            user_choise = input("Please enter your choise:")
            if user_choise == "b" or user_choise == "B":
                raise PressBerror

            user_choise = int(user_choise)

        except PressBerror:
            shirt_orders_analysis.Q7()
            continue


        if user_choise == 1:
            super1.print_products()
            print()

        if user_choise == 2 :
            super1.print_clients()
            print()

        if user_choise == 3 :
            len_pro1 = len(super1)
            new_product = product_details()
            super1 += new_product
            len_pro2 = len(super1)
            if len_pro2 > len_pro1:
                print("Product added\n")
            else:
                print("Product exist\n")

        if user_choise == 4:

            new_client = client_details()

            if super1.add_client(new_client):
                print("Client added\n")
            else:
                print("Client exist\n")

        if user_choise == 5:

            remove_product = int(input("Enter product ID to remove: "))

            if super1.remove_product(remove_product):
                print("Product removed\n")
            else:
                print("ID not found\n")

        if user_choise == 6:

            user_remove = int(input("Enter client ID to remove: "))

            if super1.remove_client(user_remove):
                print("Client removed\n")
            else:
                print("Client ID not exist\n")

        if user_choise == 7:

            max_price = int(input("Enter max price: "))
            print(super1.get_all_by_price_under(max_price))
            print()

        if user_choise == 8:

            print(super1.get_most_expensive_product())
            print()

        if user_choise == 9:
            for phone in super1.get_all_phones():
                print(phone)
            print()

        if user_choise == 10:
            for laptop in super1.get_all_leptops():
                print(laptop)
            print()

        if user_choise == 11:
            print(f"The average value is:{super1.phone_average_price()}")
            print()

        if user_choise ==12:
            print(f"The biggest screen size: {super1.get_max_screen()}")
            print()

        if user_choise == 13:
            print(f"The most common camara is: {super1.get_common_cam()}")
            print()

        if user_choise == 14:
            for pro_com in super1.list_popular():
                print(pro_com)
            print()

        if user_choise == 15:
            super1.print_all_shirts()

        if user_choise == 16:
            client_id = int(input("Enter client ID:"))
            product_id = int(input("Enter product ID:"))
            quantity = int(input("Enter quantity to order:"))
            try :
                super1.add_order(client_id, product_id, quantity)
                print("Order added!\n")

            except ClientNotFoundError as e:
                print(f"{e},operate cancelled ")
            except ShirtNotFoundError as e:
                print(f"{e},operate cancelled ")
            except ValueError as e:
                print(f"{e},operate cancelled ")


        if user_choise == 17:
            super1.print_orders()


        if user_choise == 18:
            print("bye bye!!")


menu()