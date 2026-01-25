class User:
    def __init__(self, user_id, first_name, last_name, age):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = 0

    def describe(self):
        print(f"Describing {self.user_id}:\n - Name: {self.first_name} {self.last_name}\n - Age: {self.age}")
    
    def greet(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def add_money(self, amount):
        self.balance += amount
        print(f"{self.user_id}'s balance changed: {amount}")
    
    def set_money(self, value):
        self.balance = value
        print(f"{self.user_id}'s balance set to {value}")



