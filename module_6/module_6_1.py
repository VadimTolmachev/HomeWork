class Animal:
    """
    Животный мир. Атрибуты живой и накормленный, список названий
    """
    alive = True
    fed = False

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    """
    Растительный мир. Атрибуты съедобный, список названий.
    edible - логический, определяет съедобность.
    """
    edible = False


class Mammal(Animal):
    """
    Класс млекопитающие.
    """

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    """
    Класс хищники.
    """

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    """
    Класс цветы.
    """

    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    """
    Класс фрукты.
    """
    edible = True

    def __init__(self, name):
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
