# print(int.__mro__)
# print(object)
#
# class User:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         print('Я в нью')
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#         return super().__new__(cls)
#
#     def __init__(self):
#         print('Я в инит')
#
# user1 = User()
# user2 = User()
# print(user1 is user2)
# print(id(user1), id(user2), sep='\n')

class User:
    def __init__(self, *args, **kwargs):
        print('Я в инит')
        self.args = args
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, value in kwargs.items():
            setattr(self, key, value)

other = [1, 2, 3]
user = {"name": "Den", "age": 25, "gender": 'male'}

# print(*other)

user1 = User(*other, **user)

print(user1.args)
print(user1.name, user1.age)
print(user1.gender)


