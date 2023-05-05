class Client:
    def __init__(self,client_id,name,email,address,phone_nember,gender):
        if type(client_id) == int:
            self.client_id =client_id
        else:
            self.client_id = 1234
        self.name = name
        if "@" in email:
            self.email = email
        else:
            self.email = "****@gmail.com"
        self.address = address
        if len(str(phone_nember)) == 10:
            self.phone_nember = phone_nember
        else:
            self.phone_nember = "5555555555"
        if "M" in gender.capitalize():
            self.gender = "M"
        elif "F" in gender.capitalize():
            self.gender = "F"
        else:
            self.gender = "M"

    def print_me(self):
        return print(f"----{self.client_id}----\nname: {self.name}\nemail: {self.email}\nadderss: {self.address}\nphone_number: {self.phone_nember}\ngender: {self.gender}")

    def __str__(self):
        return f"{self.client_id},{self.name},{self.email},{self.address},{self.phone_nember},{self.gender}"
    def __repr__(self):
        return str(self)




