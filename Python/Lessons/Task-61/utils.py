class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"Name: {self.name}, cuisine_type: {self.cuisine_type}")

    def open(self):
        print(f"{self.name} is now open.")

    def close(self):
        print(f"{self.name} is now сlosed.")