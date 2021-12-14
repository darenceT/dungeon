from dungeon_object import DungeonObject
from random import randint
import time


class Pit(DungeonObject):
    def __init__(self):
        super().set_name('Pit')
        super().set_letter('X')
        self.__damage = randint(15, 25)
        self.__deactivate = False

    @property
    def damage(self):
        return self.__damage

    @property
    def deactivate(self):
        return self.__deactivate

    @deactivate.setter
    def deactivate(self, switch=False):
        if isinstance(switch, bool):
            if not switch:
                raise ValueError('Only True boolean allowed')
            self.__deactivate = switch
        else:
            raise TypeError('Only boolean type allowed')

    def function(self):
        if not self.__deactivate:
            print('\n  Walk slow or run too fast, you still fell into a pit!\n')
            time.sleep(1)
            print('  You lose', self.__damage, 'health.\n')
            self.deactivate = True
            return self.__damage
        else:
            print('  You safely walk around the pit\n')
            time.sleep(1)
            return 0


if __name__ == '__main__':          ############## DELETE #################
    p = Pit()
    print(p.letter)
    p.visited = True
    print(p.visited)
