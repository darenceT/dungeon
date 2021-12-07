from entrance_door import EntranceDoor
from exit_door import ExitDoor
from pillar import Pillar
from health_potion import HealthPotion
from vision_potion import VisionPotion
from pit import Pit

from random import randrange


class ObjectFactory:

    def __init__(self, map):
        self.__map = map
        self.__room_index = map.room_index
        self.__start_production()

    def valid_random_loc(self):
        """
        Generate random locations while avoiding impassible, entrance and exit rooms
        :return: random location
        :rtype: tuple
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
        self.__deliver_to_room(self.__map.entrance_loc, EntranceDoor())
        self.__deliver_to_room(self.__map.exit_loc, ExitDoor())
        self.__build_pillars()
        self.__create_objects(HealthPotion())
        self.__create_objects(VisionPotion())
        self.__create_objects(Pit())

    def __create_objects(self, object):
        loc_list = []
        index = 0
        while index < self.__map.height:
            loc = self.valid_random_loc()
            if loc not in loc_list:
                loc_list.append(loc)
                self.__deliver_to_room(loc, object)
                index += 1
                print(loc, object, 'created at object factory')             ################## delete ######
            else:                                                            ################## delete ######
                print('object not created', object)                            ################## delete ######

    def __build_pillars(self):
        """
        Create pillars by obtaining location from map (BuildDungeon class).
        """
        letters = ['A', 'I', 'E', 'P']
        for loc in self.__map.pillars_loc:
            self.__deliver_to_room(loc, Pillar(letters.pop()))

    def __deliver_to_room(self, location, object):
        x = location[0]
        y = location[1]
        self.__room_index[(x, y)].receive_from_factory(object)
        print("success sending items", object, object.letter)       ####################### delete #####################

        # Update map, always show all initial objects
        if self.__map.ver[y][x][1] != ' ':
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + 'M '
        else:
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + object.letter + ' '
