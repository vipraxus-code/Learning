class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def get_info(self):
        print(f"Name: {self.name}, cuisine_type: {self.cuisine_type}")

    def open(self):
        print(f"{self.name} is now open.")

    def close(self):
        print(f"{self.name} is now сlosed.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavor):
        super().__init__(name, cuisine_type)
        self.flavor = flavor

    def get_flavor(self):
        print(f"Flavor of this stand is {self.flavor}.")