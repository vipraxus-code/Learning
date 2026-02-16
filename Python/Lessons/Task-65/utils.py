from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        print(f"Die is showing {randint(1, self.sides)}.")