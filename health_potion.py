from dungeon_object import DungeonObject
from random import choice
from sound_fx import SoundFx


class HealthPotion(DungeonObject):
    type = {5: 'Minor Health Potion', 10: 'Health Potion', 15: 'Greater Health Potion'}

    def __init__(self):
        self.__set_health_points(choice(list(self.type.keys())))
        super().set_name(self.type[self.__health_points])
        super().set_letter('H')

    @property
    def health_points(self):
        SoundFx.health_potion()
        return self.__health_points

    def __set_health_points(self, num):
        if isinstance(num, int):
            if num in [5, 10, 15]:
                self.__health_points = num
            else:
                raise ValueError('Only values 5, 10, or 15 allowed for health potion')
        else:
            raise TypeError('Integer only allowed')

    def function(self):
        return self.__health_points

    def inspect(self):
        print(f'  This {self.name} can heal {self.__health_points} points!\n')

if __name__ == '__main__':
    p = HealthPotion()
    print(p.name)
    print(p.letter)
    print(p.function())
