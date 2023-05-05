import numpy as np
from ClientNotFoundError import ClientNotFoundError
from SuperStore import SuperStore
import matplotlib.pyplot as plt

super2 = SuperStore(products="products_supply.csv", clients="clients.csv",shirts="shirts.csv",orders="orders.csv")

# Q1 :
orders =np.genfromtxt("orders.csv",dtype="int32",delimiter=",",skip_header=1)

# Q2 :
total_cost_lst = []
for i in orders:
    quantity = i[3]
    price = super2.get_shirt(i[2]).price
    total_cost = int(quantity*price)
    total_cost_lst.append(total_cost)

total_cost_array = np.array(total_cost_lst)
print(total_cost_array)
total_cost_array = total_cost_array.reshape(200,1)
print(total_cost_array)

orders = np.append(orders,total_cost_array,axis=1)
#print(orders)

# Q3:
def Q3():
    max_cost = max(total_cost_lst)

    for c in orders:
        if c[4] == max_cost:
            print(f"{c[0]},{super2.get_client(c[1]).name},{super2.get_product(c[2]).product_name},{max_cost}")

# Q4:
def Q4():
    client_id_from_user = int(input("Enter client id: "))

    try:
        if super2.get_client(client_id_from_user) == None:
            raise ClientNotFoundError("Client does not exist")

        number_of_orders = np.count_nonzero(orders[:, 1]==client_id_from_user)

        client_spent = 0
        for s in orders:
            if s[1] == client_id_from_user:
                client_spent+=s[4]

        print(f"Clinet name:{super2.get_client(client_id_from_user).name}, number of orders:{number_of_orders},total spent:{client_spent}")
    except ClientNotFoundError as e:
        print(e)

# Q5:
def Q5():
    av_spent = np.mean(total_cost_array)

    av_mask = orders[:,4]>av_spent
    arr_finle = orders[av_mask]
    print(arr_finle)

# Q6
def Q6():
    dict ={}
    unique , count = np.unique(orders[:,1],return_counts=True)
    for (u,c) in zip(unique,count):
        dict[u]=c

    return dict
print(Q6())
# Q7
def Q7():
    a1_client = np.array([])
    a2_orders = np.array([])
    for i in Q6():
        a1_client=np.append(a1_client,str(i))
        a2_orders=np.append(a2_orders,Q6()[i])
    plt.bar(a1_client,a2_orders,color = ["green"])
    plt.title("Client orders",fontdict={"fontname":"Garamond","fontsize":30})
    plt.xlabel("Client ID",fontdict={"fontsize":15})
    plt.ylabel("Number of orders",fontdict={"fontsize":15})
    return plt.show()


if __name__ == "__main__":
    Q3()
    print()
    Q4()
    Q5()

    Q7()


