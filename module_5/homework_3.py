def checking_the_method(v1_int, v2_house):
    if isinstance(v1_int, int) and isinstance(v2_house, House):
        return True
    else:
        print(f'Переменные не прошли проверку на принадлежность классу {v1_int}, {v2_house}')
        return False


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
        # self.say_info()

    def say_info(self):
        print(f'Здание построено компанией "{self.name}", в {self.floors} этажей(а).')

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __del__(self):
        print(f'{self.name} ушел.')

    def __eq__(self, other):
        if checking_the_method(other.floors, other):
            return self.floors == other.floors

    def __lt__(self, other):
        if checking_the_method(other.floors, other):
            print(other.floors)
            return self.floors < other.floors

    def __le__(self, other):
        if checking_the_method(other.floors, other):
            return self.floors <= other.floors

    def __gt__(self, other):
        if checking_the_method(other.floors, other):
            return self.floors > other.floors

    def __ge__(self, other):
        if checking_the_method(other.floors, other):
            return self.floors >= other.floors

    def __ne__(self, other):
        if checking_the_method(other.floors, other):
            return self.floors != other.floors

    def __add__(self, value):
        if checking_the_method(value, self):
            return self.floors + value

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1.floors = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1.floors += 10  # __iadd__
print(h1)
h2.floors = 10 + h2  # __radd__
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
