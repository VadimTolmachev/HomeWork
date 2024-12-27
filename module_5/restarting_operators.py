# Задача "Нужно больше этажей"
def print_func():
    pass

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
        # print(self.say_info())

    def say_info(self):
        return f'Название: {self.name}, количество этажей: {self.floors}.'

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.floors:
            return f'Такого этажа не существует'
        else:
            for i in range(1, new_floor + 1):
                print(f'Подъем на {i} этаж.')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}.'

    def __eq__(self, other):
        print('__eq__ - ==')
        return self.floors == other.floors

    def __lt__(self, other):
        print('__lt__ - <')
        # if isinstance(self.number_of_floors, int) and isinstance(other, House):
        return self.floors < other.floors
        # return 'Ошибка сравнения.'

    def __le__(self, other):
        print('__le__ - <=')
        # if isinstance(self.number_of_floors, int) and isinstance(other, House):
        return self.floors <= other.floors
        # return 'Ошибка сравнения.'

    def __gt__(self, other):
        print('__gt__ - >')
        return self.floors > other.floors


    def __ge__(self, other):
        print('__ge__ - >=')
        return self.floors >= other.floors


    def __ne__(self, other):
        print('__ne__ - !=')
        return self.floors != other.floors


    def __add__(self, value):
        print(__name__)
        #print('__add__')
        return self.floors + value
        #return f'Ошибка.Невозможно к {self.number_of_floors} прибавить {value}.'

    def __radd__(self, value):
        print(__name__)
        #print('__radd__')
        #if isinstance(self.number_of_floors, int) and isinstance(value, int):
        return value + self.floors
        #return f'Ошибка.Невозможно к {value} прибавить {self.number_of_floors}.'

    def __iadd__(self, value):
        print_func()
        #if isinstance(self.number_of_floors, int) and isinstance(value, int):
        return self.floors + value
        #return f'Ошибка.Невозможно к {self.number_of_floors} прибавить {value}.'

    def __del__(self):
        print(f'{self.name} ушел.')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__
h1.floors = h1 + 10 # __add__

print(h1)
print(h1 == h2)
h1.floors += 10 # __iadd__

print(h1)
h2.floors = 10 + h2 # __radd__

print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__