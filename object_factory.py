from entrance_door import EntranceDoor
from exit_door import ExitDoor
from pillar import Pillar
from health_potion import HealthPotion
from vision_potion import VisionPotion
from pit import Pit

from random import randrange


class ObjectFactory:
    """
    Simple factory design pattern for creating all objects in dungeon, then delivery to
    each room
    """
    def __init__(self, map):
        """
        Obtain map of dungeon and container of rooms to deliver objects.
        Start production starts the building process
        :param map: map of dungeon
        :type map: BuildDungeon
        """
        self.__map = map
        self.__room_index = map.room_index
        self.__start_production()

    def __valid_random_loc(self):
        """
        Generate random locations while avoiding impassible, entrance and exit rooms
        :return: random location
        :rtype: tuple(int, int)
        """
        while True:
            x = randrange(0, self.__map.width)
            y = randrange(0, self.__map.height)
            if not self.__map.room_index[(x, y)].impassible:
                if (x, y) == self.__map.entrance_loc or (x, y) == self.__map.exit_loc:
                    continue
                else:
                    return x, y

    def __start_production(self):
        """
        Power on the factory with list of objects to create
        """
        self.__deliver_to_room(self.__map.entrance_loc, EntranceDoor())
        self.__deliver_to_room(self.__map.exit_loc, ExitDoor())
        self.__build_pillars()
        self.__create_objects(VisionPotion)
        self.__create_objects(HealthPotion)
        self.__create_objects(Pit)

    def __create_objects(self, object):
        """
        Temporary list of locations is used to avoid placing duplicate items in same room.
        map height is used to create number of objects based on difficulty: Easy 4, Normal 8, Hard 12
        
        ***Note: To change # of objects, modify self.__map.height e.g. self.__map.height x 2 to double 
        all the objects (potions & pits)
        
        :param object: objects for each room
        :param type: DungeonObject
        """
        temp_list = []
        index = 0
        while index < self.__map.height:    # change self.__map.height to change # of objects
            loc = self.__valid_random_loc()
            if loc not in temp_list:
                temp_list.append(loc)
                self.__deliver_to_room(loc, object())
                index += 1

    def __build_pillars(self):
        """
        Create pillars by obtaining location from map (BuildDungeon class).
        """
        letters = ['A', 'I', 'E', 'P']
        for loc in self.__map.pillars_loc:
            self.__deliver_to_room(loc, Pillar(letters.pop()))

    def __deliver_to_room(self, location, object):
        """
        Deliver object to specific room. Also write letter on map.
        Letter on map will not change when objects get picked up
        (vs print of room which does changes when objects are picked up)
        """
        x, y = location
        self.__room_index[(x, y)].receive_from_factory(object)

        if self.__map.ver[y][x][1] != ' ':
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + 'M '
        else:
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + object.letter + ' '
