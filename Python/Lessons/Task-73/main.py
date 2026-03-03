from utils import UserData


user0 = UserData(0, "Alex", 10)

print(user0.dump_data())
print(user0.load_data())
print(user0.greet())

user1 = UserData(1, "Ben", 15)

print(user1.dump_data())
print(user1.load_data())

user2 = UserData(2, "Steve", 100)

print(user2.dump_data())
print(user2.load_data())