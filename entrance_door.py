from dungeon_object import DungeonObject


class EntranceDoor(DungeonObject):
    def __init__(self):
        super().set_name('Entrance')
        super().set_letter('i')
        self.__deactivate = False

    @property
    def deactivate(self):
        return self.__visited

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
            print('You found an iphone.\nIt contains a "Torch" app you can use as a flashlight!\n')
            self.deactivate = True


if __name__ == '__main__':          ############## DELETE #################
    p = EntranceDoor()
    print(p.name)
    print(p.letter)