from dungeon_object import DungeonObject


class EntranceDoor(DungeonObject):
    """
    Inherit from abstract base class DungeonObject.
    Entrance door for the starting location. Has function of finding a phone to use a light.
    Future feature can include battery life as timer for player to find exit or lose.
    """
    def __init__(self):
        """
        Create entrance door. Deactivate attribute is used similar to visited, so player
        will not pick up additional iphones by revisiting entrance room.
        """
        super().set_name('Entrance')
        super().set_letter('i')
        self.__deactivate = False

    @property
    def deactivate(self):
        """
        Getter for deactivate status of entrance door.
        :return: deactivated status of entrance door
        :rtype: boolean
        """
        return self.__visited

    @deactivate.setter
    def deactivate(self, switch=False):
        """
        Setter for deactivate status of entrance door.
        :param switch: allow turning off function
        :type switch: bool
        :raises: if param is not boolean or not True
        """
        if isinstance(switch, bool):
            if not switch:
                raise ValueError('Only True boolean allowed')
            self.__deactivate = switch
        else:
            raise TypeError('Only boolean type allowed')

    def function(self):
        """
        Allows player to pick up iphone then deactivate door.
        """
        if not self.__deactivate:
            print('  You found an iphone.\n'
                  '  It contains a "Torch" app you can use as a flashlight!\n')
            self.deactivate = True


if __name__ == '__main__':          ############## DELETE #################
    p = EntranceDoor()
    print(p.name)
    print(p.letter)