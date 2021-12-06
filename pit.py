from dungeon_object import DungeonObject
from random import randint


class Pit(DungeonObject):
    def __init__(self):
        super().set_name('Pit')
        super().set_letter('X')
        self.__damage = randint(1, 20)

    @property
    def damage(self):
        return self.__damage
