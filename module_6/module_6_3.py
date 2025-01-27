from random import randint


class Animal:
    """
    класс описывающий животных
    """
    _DEGREE_OF_DANGER = 0

    live = True
    sound = None
    dx = 0
    dy = 0
    dz = 0
    _cords = [dx, dy, dz]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed > 0:
            self.dx = dx * self.speed
            self.dy = dy * self.speed
            self.dz = dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X:{self.dx}, Y:{self.dy}, Z:{self.dz}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        pass


class Bird(Animal):
    """
    Класс птицы
    """
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, dz):
        super().__init__(dz)

    def dive_in(self, dz):
        self.dz = abs(dz - self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


print(Duckbill.mro())
print(AquaticAnimal.mro())
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
