from random import randint


class Pit:
    def __init__(self):
        self.__damage = randint(1, 20)

    @property
    def damage(self):
        return self.__damage
