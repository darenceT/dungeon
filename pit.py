from dungeon_object import DungeonObject
from random import randint
import time


class Pit(DungeonObject):
    def __init__(self):
        super().set_name('Pit')
        super().set_letter('X')
        self.__damage = randint(1, 20)
        self.__visited = False

    def damage(self):
        return self.__damage

    def get_visited(self):
        return self.__visited

    def set_visited(self):
        self.__visited = True

    damage = property(damage)
    visited = property(get_visited)

    def function(self):
        if not self.__visited:
            print('Walk slow or run too fast, you still fell into a pit!\n')
            time.sleep(3)
            print('You lose', self.__damage, 'health.\n')
            return self.__damage
        else:
            print('You safely walk around the pit\n')
            time.sleep(2)
            return 0


if __name__ == '__main__':          ############## DELETE #################
    p = Pit()
    print(p.name)
    p.set_visited()
    print(p.visited)
