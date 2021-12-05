from dungeon_object import DungeonObject


class EntranceDoor(DungeonObject):

    def __init__(self):
        self.__name = "Entrance"

    def function(self):
        print('You found an iphone. The only app it contains is "Torch" which looks like just a flashlight')

    def char(self):
        return 'i'
    
    def __str__(self):
        return self.__name