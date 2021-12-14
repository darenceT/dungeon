from dungeon_object import DungeonObject
from pillar import Pillar
import time


class ExitDoor(DungeonObject):
    """
    Inherit from abstract base class DungeonObject.
    Exit door to leave the maze on condition that player has collected 4 pillar keys
    """
    def __init__(self):
        """
        Create exit door. Attribute freedom becomes true if player has 4 pillar key
        to allow player to win game.
        """
        super().set_name('Exit')
        super().set_letter('O')
        self.__freedom = False

    @property
    def freedom(self):
        """
        Getter for freedom attribute of exit door
        :return: status of whether player can open exit door
        :rtype: boolean
        """
        return self.__freedom

    @freedom.setter
    def freedom(self, switch=False):
        """
        Setter for freedom attribute of exit door.
        :param switch: switch to on/True to unlock door
        :type switch: boolean
        :raises: if param is not boolean or not True
        """
        if isinstance(switch, bool):
            if not switch:
                raise ValueError('Only True boolean allowed')
            self.__freedom = switch
        else:
            raise TypeError('Only boolean type allowed')

    def function(self, backpack):
        """
        Allow player to open door, setting freedom to True if player has collect
        4 pillar keys.
        :param backpack: player's inventory
        :type backpack: list
        """
        key_count = sum(isinstance(x, Pillar) for x in backpack)
        if key_count == 4:
            print('  You put in all 4 pillar keys and you hear some gears turning...')
            time.sleep(2)
            print('  INSERT ART HERE\n'
                  '  You found your escape!')
            self.freedom = True
        else:
            print('  You see some light...it\'s a door! There are 4 strange-key holes...\n'
                  '  You only have', key_count, 'keys...')


if __name__ == '__main__':          ############## DELETE #################
    p = ExitDoor()
    print(p.name)
    print(p.letter)