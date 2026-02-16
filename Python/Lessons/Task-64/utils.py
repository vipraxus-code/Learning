class User:
    def __init__(self, user_id, first_name, last_name, age):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = Balance(self.user_id, 0)
        self.privileges = Privileges(user_id, [])

    def describe(self):
        print(f"Describing {self.user_id}:\n - Name: {self.first_name} {self.last_name}\n - Age: {self.age}")

    def greet(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


class Admin(User):
    def __init__(self, user_id, first_name, last_name, age):
        super().__init__(user_id, first_name, last_name, age)
        self.privileges = Privileges(user_id, ["delete messages", "ban users"])


class Privileges:
    def __init__(self, user_id, privileges=None):
        self.user_id = user_id
        self.privileges = privileges
    
    def show(self):
        print(f"{self.user_id}'s privileges are {self.privileges}.")


class Balance:
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.balance = amount 

    def show(self):
        print(f"{self.user_id}'s balance is {self.balance}.")

    def add(self, amount):
        self.balance += amount
        print(f"{self.user_id}'s balance changed: {amount}.")
    
    def set(self, value):
        self.balance = value
        print(f"{self.user_id}'s balance set to {value}.")