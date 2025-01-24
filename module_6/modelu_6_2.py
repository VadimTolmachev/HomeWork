class Vehicle:
    """
    Класс транспортное средство.
    """
    owner = ''
    __model = 'Toyota'
    __engine_power = 190
    __color = 'White'

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

class Sedan(Vehicle):
    __color_variants = ['Yellow, Green, Gray, Blue', 'Red', 'Black', 'White']

