import tkinter as tk
from Laptop import Laptop
from Smartphone import Smartphone
from SuperStore import SuperStore
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from apperrors import *


super4 = SuperStore(products="products_supply.csv", clients="clients.csv", shirts="shirts.csv", orders="orders.csv")


# window setting
win = tk.Tk()
win.title("Super Store App")
win.configure(cursor="circle")
win.geometry("900x700")

# labels
l1 = tk.Label(win,text="SuperStore",font=("broadway",30),fg="blue")
l1.grid(row=0,column=0)
l2 = tk.Label(win,text="Products",font=("broadway",20))
l2.grid(row=1,column=0)

def dispay_click():
    element = commbobox1.get()
    if element == "All products":
        product_listbox.delete(0,tk.END)
        for p in super4.products:
            product_listbox.insert(tk.END,p)
    if element == "Laptop":
        product_listbox.delete(0,tk.END)
        for l in super4.get_all_leptops():
            product_listbox.insert(tk.END,l)
    if element == "Smartphone":
        product_listbox.delete(0,tk.END)
        for s in super4.get_all_phones():
            product_listbox.insert(tk.END,s)
    if element == "Shirts":
        product_listbox.delete(0,tk.END)
        for shirt in super4.get_all_shirts():
            product_listbox.insert(tk.END,shirt)

def clean_values():
    entry_id.delete(0,tk.END)
    entry_id.configure(background="white")
    entry_price.delete(0,tk.END)
    entry_price.configure(background="white")
    entry_brand.delete(0,tk.END)
    entry_brand.configure(background="white")
    entry_model.delete(0,tk.END)
    entry_model.configure(background="white")
    commbobox2.delete(0,tk.END)
    entry_cpu.delete(0,tk.END)
    entry_cpu.configure(background="white")
    entry_hard_disk.delete(0,tk.END)
    entry_hard_disk.configure(background="white")
    entry_screen.delete(0,tk.END)
    entry_screen.configure(background="white")
    entry_cellular.delete(0,tk.END)
    entry_cellular.configure(background="white")
    entry_number_cores.delete(0,tk.END)
    entry_number_cores.configure(background="white")
    entry_res.delete(0,tk.END)
    entry_res.configure(background="white")

def white_all_lables():
    entry_id.configure(background="white")
    entry_price.configure(background="white")
    entry_brand.configure(background="white")
    entry_model.configure(background="white")
    entry_cpu.configure(background="white")
    entry_hard_disk.configure(background="white")
    entry_cellular.configure(background="white")
    entry_res.configure(background="white")
    entry_number_cores.configure(background="white")
    entry_screen.configure(background="white")

def start_check(product_id, product_price, product_brand, product_model):
    if product_id == "":
        raise EmptyEntry("One or more entry are empty")
    if product_price == "":
        raise EmptyEntry("One or more entry are empty")
    if not product_id.isnumeric():
        raise IDerror("Product ID must be an integer")
    if super4.get_product(int(product_id)) is not None:
        raise ProductnNotFind("The product already exist!")
    if not product_price.isnumeric():
        raise PriceNotInt("Product price must be an integer")
    if product_brand == "":
        raise EmptyEntry("One or more entry are empty")
    if product_model == "":
        raise EmptyEntry("One or more entry are empty")


def laptop_check(product_hard_disk, product_screen,product_cpu):
    if product_hard_disk == "":
        raise EmptyEntry("One or more entry are empty")
    if product_screen == "":
        raise EmptyEntry("One or more entry are empty")
    if not product_hard_disk.isnumeric():
        raise HardDiskNum("Hard disk must be an integer")
    if not product_screen.isnumeric():
        raise ScreenNum("Screen must be an integer")
    if product_cpu =="":
        raise EmptyEntry("One or more entry are empty")


def smart_check(number_of_cores, cam_res,product_cellular ):
    if number_of_cores == "":
        raise EmptyEntry("One or more entry are empty")
    if cam_res == "":
        raise EmptyEntry("One or more entry are empty")
    if not number_of_cores.isnumeric():
        raise CoreError("Number of cores must be an integer")
    if not cam_res.isnumeric():
        raise ResError("Resolution must be an integer")
    if product_cellular == "":
        raise EmptyEntry("One or more entry are empty")


def red_empty():
    if entry_id.get()=="":
        entry_id.configure(background="red")
    if entry_price.get()=="":
        entry_price.configure(background="red")
    if entry_model.get()=="":
        entry_model.configure(background="red")
    if entry_brand.get()=="":
        entry_brand.configure(background="red")
    if entry_cpu.get()=="":
        entry_cpu.configure(background="red")
    if entry_hard_disk.get()=="":
        entry_hard_disk.configure(background="red")
    if entry_screen.get()=="":
        entry_screen.configure(background="red")
    if entry_cellular.get()=="":
        entry_cellular.configure(background="red")
    if entry_number_cores.get()=="":
        entry_number_cores.configure(background="red")
    if entry_res.get()=="":
        entry_res.configure(background="red")


def create_new_product():
    l_error = tk.Label(text=f" ",fg="white")
    l_error.grid(row=5, column=0)
    white_all_lables()
    try:
        product_id = entry_id.get()
        product_price = entry_price.get()
        product_brand = entry_brand.get()
        product_model = entry_model.get()
        product_year = int(commbobox2.get())

        # chacking error option
        start_check(product_id,product_price,product_brand,product_model)

        product_price = int(product_price)
        product_id = int(product_id)

        if product_choose() == "Laptop":
            product_cpu = entry_cpu.get()
            product_hard_disk = entry_hard_disk.get()
            product_screen = entry_screen.get()
            # checking laptop errors
            laptop_check(product_hard_disk,product_screen,product_cpu)
            new_leptop = [Laptop(product_id,product_brand,product_model,product_year,product_price,product_cpu,product_hard_disk,product_screen)]
            super4.products+=new_leptop
            messagebox.showinfo(message=f"You added new product: {super4.get_product(product_id)}")
        if product_choose() == "Smartphone":
            product_cellular = entry_cellular.get()
            product_number_cores = entry_number_cores.get()
            product_res = entry_res.get()
            # checking phone errors
            smart_check(product_number_cores,product_res,product_cellular)
            new_Smartphone = [Smartphone(product_id,product_brand,product_model,product_year,product_price,product_cellular,product_number_cores,product_res)]
            super4.products+=new_Smartphone
            messagebox.showinfo(message=f"You added new product: {super4.get_product(product_id)}")
        clean_values()

    except IDerror as e:
        l_error.configure(text=f"{e}",fg="red")
    except ProductnNotFind as e:
        l_error.configure(text=f"{e}", fg="red")
    except PriceNotInt as e:
        l_error.configure(text=f"{e}", fg="red")
    except HardDiskNum as e:
        l_error.configure(text=f"{e}", fg="red")
    except ScreenNum as e:
        l_error.configure(text=f"{e}", fg="red")
    except CoreError as e:
        l_error.configure(text=f"{e}", fg="red")
    except ResError as e:
        l_error.configure(text=f"{e}", fg="red")
    except EmptyEntry as e:
        red_empty()
        l_error.configure(text=f"{e}", fg="red")





# create Combobox
commbobox1 = ttk.Combobox(win,values=["All products","Laptop","Smartphone","Shirts"])
commbobox1.grid(row=2,column=0)

# buttons
display_product_button = tk.Button(win,text="Display products",command=dispay_click)
display_product_button.grid(row=2,column=1)
display_create = tk.Button(win,text="   Create   ",command=create_new_product)
display_create.grid(row=35,column=4,sticky=E)


# listbox
product_listbox =Listbox(win,width=50,height=10)
product_listbox.grid(row=2,column=4)

# create new products
l3 = tk.Label(win,text="Create New Product",font=("broadway",20))
l3.grid(row=4,column=0,sticky=W)
l4 = tk.Label(win,text="ID",font=("Times",10))
l4.grid(row=6,column=0)
l5 = tk.Label(win,text="Price",font=("Times",10))
l5.grid(row=6,column=1,sticky=W)
l6 = tk.Label(win,text="Brand",font=("Times",10))
l6.grid(row=6,column=2,sticky=N,padx=30)
l7 = tk.Label(win,text="Model",font=("Times",10))
l7.grid(row=6,column=4,sticky=W,padx=30)
l8 = tk.Label(win,text="Year",font=("Times",10))
l8.grid(row=9,column=0)
l9 = tk.Label(win,text="CPU",font=("Times",10))
l9.grid(row=12,column=1,sticky=W)
l10 = tk.Label(win,text="Hard Disk",font=("Times",10))
l10.grid(row=12,column=2,sticky=N,padx=30)
l11 = tk.Label(win,text="Screen",font=("Times",10))
l11.grid(row=12,column=4,sticky=W,padx=30)
l12 = tk.Label(win,text="Cellular Network",font=("Times",10))
l12.grid(row=14,column=1,sticky=W)
l13 = tk.Label(win,text="Number of cores",font=("Times",10))
l13.grid(row=14,column=2,sticky=N,padx=30)
l14 = tk.Label(win,text="Camara resulution",font=("Times",10))
l14.grid(row=14,column=4,sticky=W,padx=30)
l_enpty = tk.Label(win,text="").grid(column=0,row=14)

# Enter boxes
entry_id = tk.Entry(win, width=10,font=("Times",12))
entry_id.grid(column=0, row=7)
entry_price = tk.Entry(win, width=10,font=("Times",12))
entry_price.grid(column=1, row=7,sticky=W)
entry_brand= tk.Entry(win, width=10,font=("Times",12))
entry_brand.grid(column=2, row=7,sticky=N)
entry_model= tk.Entry(win, width=10,font=("Times",12))
entry_model.grid(column=4, row=7,sticky=W,padx=30)
entry_cpu= tk.Entry(win, width=10,font=("Times",12))
entry_cpu.grid(column=1, row=13,sticky=W)
entry_hard_disk= tk.Entry(win, width=10,font=("Times",12))
entry_hard_disk.grid(column=2, row=13,sticky=N)
entry_screen= tk.Entry(win, width=10,font=("Times",12))
entry_screen.grid(column=3, row=13,columnspan=2,padx=30,sticky=W)
entry_cellular= tk.Entry(win, width=10,font=("Times",12))
entry_cellular.grid(column=1, row=15,sticky=W)
entry_number_cores= tk.Entry(win, width=10,font=("Times",12))
entry_number_cores.grid(column=2, row=15,sticky=N)
entry_res= tk.Entry(win, width=10,font=("Times",12) )
entry_res.grid(column=3, row=15,columnspan=2,padx=30,sticky=W)

#combobox year
commbobox2 = ttk.Combobox(win,values=[str(i) for i in range(1970,2024)])
commbobox2.grid(row=10,column=0)


# radio option
radio_product = StringVar()
radio_values = {"Laptop":"Laptop","Smartphone":"Smartphone"}



def product_choose():
    if radio_product.get() == "Laptop":
        entry_cpu["state"] = "normal"
        entry_hard_disk["state"] = "normal"
        entry_screen["state"] = "normal"
        entry_cellular["state"]="disable"
        entry_number_cores["state"]="disable"
        entry_res["state"]="disable"
        return "Laptop"
    elif radio_product.get() == "Smartphone":
        entry_cpu["state"]="disable"
        entry_hard_disk["state"]="disable"
        entry_screen["state"]="disable"
        entry_cellular["state"] = "normal"
        entry_number_cores["state"] = "normal"
        entry_res["state"] = "normal"
        return "Smartphone"

i=13
for text, value in radio_values.items():
    radio_button = Radiobutton(win, text=text,
                                value=value,
                                variable=radio_product,
                               command=product_choose)
    radio_button.grid(sticky=W, column=0,row=i)
    i+=2



win.mainloop()
