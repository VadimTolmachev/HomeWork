# Задача "Нужно больше этажей"
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_flors = number_of_floors
        #print(self.say_info())

    def say_info(self):
        return f'Этажность здания - {self.number_of_flors}, от компании - {self.name}.'

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_flors:
            return f'Такого этажа не существует'
        else:
            for i in range(1, new_floor + 1):
                print(f'Подъем на {i} этаж.')

    def __lt__(self, other):
        return self.number_of_flors < other

    def __eq__(self, other):
        return self.number_of_flors == other

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация',20)

