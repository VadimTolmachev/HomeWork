class Animal
    """
    класс описывающий животных
    """
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords = [0, 0, 0], speed):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        pass

    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if _DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        pass

