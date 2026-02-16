from utils import User, Admin


user0 = User("user0", "John", "Smith", 34)
user1 = User("user1", "Jane", "Doe", 28)
user2 = User("user2", "Bob", "Johnson", 42)

admin0 = Admin("admin0", "God of", "the new world", "error")


user0.describe()
user0.greet()
user0.balance.add(16)
user0.balance.set(1756)
user0.balance.show()
user0.privileges.show()

admin0.describe()
admin0.greet()
admin0.balance.add(16)
admin0.balance.set(1756)
admin0.balance.show()
admin0.privileges.show()