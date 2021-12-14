from dungeon_object import DungeonObject
from random import randint
import time


class Pit(DungeonObject):
    """
    Inherit from abstract base class DungeonObject.
    Pit are objects that cause player to lose health.
    Deactivate pit after seeing it from your fall, avoid falls and subsequent visits
    """
    def __init__(self):
        """
        Generate random damage of pit, due to varying depths
        Deactivate status becomes true after your fall
        """
        super().set_name('Pit')
        super().set_letter('X')
        self.__damage = randint(15, 25)
        self.__deactivate = False

    @property
    def damage(self):
        """
        Getter for pit damage
        :return: amount of pit damage
        :rtype: int
        """
        return self.__damage

    @property
    def deactivate(self):
        """
        Getter for deactivate status of pit
        :return: deactivate status of pit
        :rtype: bool
        """
        return self.__deactivate

    @deactivate.setter
    def deactivate(self, switch=False):
        """
        Setter for deactivate status of pit
        :param switch: mechanism to decativate pit
        :type switch: bool
        :raises: if switch is not bool or if not True
        """
        if isinstance(switch, bool):
            if not switch:
                raise ValueError('Only True boolean allowed')
            self.__deactivate = switch
        else:
            raise TypeError('Only boolean type allowed')

    def function(self):
        """
        Check if pit has been deactivated(visited), then return damage affecting player.
        :return: damage of pit
        :rtype: int
        """
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
