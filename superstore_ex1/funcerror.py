from apperrors import *
from super_store_app import super4


def errorcatch1(product_id, product_price):
    # if product_id == "":
    #     raise EmptyEntry("One or more entry are empty")
    # if product_price == "":
    #     raise EmptyEntry("One or more entry are empty")
    if not product_id.isnumeric():
        raise IDerror("Product ID must be an integer")
    if super4.get_product(product_id) is not None:
        raise ProductnNotFind("The product already exist!")
    if not product_price.isnumeric():
        raise PriceNotInt("Product price must be an integer")
    # if product_brand == "":
    #     raise EmptyEntry("One or more entry are empty")
    # if product_model == "":
    #     raise EmptyEntry("One or more entry are empty")


def errorcatch_laptop(product_hard_disk, product_screen):
    if not product_hard_disk.isnumeric():
        raise HardDiskNum("Hard disk must be an integer")
    if not product_screen.isnumeric():
        raise ScreenNum("Screen must be an integer")


def errocatch_smart(number_of_cores, cam_res):
    if not number_of_cores.isnumeric():
        raise CoreError("Number of cores must be an integer")
    if not cam_res.isnumeric():
        raise ResError("Resolution must be an integer")
