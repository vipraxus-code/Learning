def printed(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

class Employee:
    def __init__(self, first_name, last_name, salary=30000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @printed
    def give_raise(self, amount=5000):
        self.salary += amount
        return f"{self.first_name.title()} {self.last_name.title()} now has salary of {self.salary}!"