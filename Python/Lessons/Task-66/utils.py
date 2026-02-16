from random import sample


class Lottery:
    def __init__(self, lottery_pool=None):
        if lottery_pool == None:
            lottery_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
        self.lottery_pool = lottery_pool

    def roll(self, combination):
        win_combination = sample(self.lottery_pool, 4)
        if win_combination == combination:
            print("You won!")
            return True
        print(f"Not today! The win combination was {win_combination}.")
        return False

def gambling(lottery):
    attempts = 0
    while not lottery.roll([1, 2, 3, 4]):
        attempts += 1
    print(f"Attempts: {attempts}")