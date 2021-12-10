from dungeon_object import DungeonObject
from random import choice


class HealthPotion(DungeonObject):
    type = {5: 'Minor Health Potion', 10: 'Health Potion', 15: 'Greater Health Potion'}

    def __init__(self):
        self.__set_health_points(choice(list(self.type.keys())))
        super().set_name(self.type[self.__health_points])
        super().set_letter('H')

    def __set_health_points(self, num):
        if isinstance(num, int):
            if num in [5, 10, 15]:
                self.__health_points = num
            else:
                raise ValueError('Only values 5, 10, or 15 allowed for health potion')
        else:
            raise TypeError('Integer only allowed')

    def function(self):
        print(f'  Your health is replenished by {self.name} for {self.__health_points} points!\n')
        return self.__health_points


if __name__ == '__main__':
    p = HealthPotion()
    print(p.name)
    print(p.letter)
    print(p.function())
