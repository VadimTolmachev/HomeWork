class Human:
    head = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет.')

    def birthday(self):
        self.age += 1
        print(f'У меня сегодня день рождения, и мне теперь {self.age} лет.')

    def __del__(self):
        print(f'{self.name} ушел.')

    def __len__(self):
        return self.age

den = Human('Денис', 22)
maks = Human('Максим', 22)

den.age = 23
print(len(den))
# del den
# print(den.name, den.age)
# print(macks.name, macks.age)
#den.say_info()
# macks.say_info()
maks.birthday()
maks.say_info()
print(Human.head)