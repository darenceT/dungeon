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
        # self.pillars_loc = []           ################ delete??? ###############################
        self.create_objects()

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
                print('this is passible for putting object')
                if (x, y) == self.__map.entrance_loc or (x, y) == self.__map.exit_loc:
                    print('before continue')           ####################### delete ###########################
                    continue
                else:
                    print('before return')           ####################### delete ###########################
                    return x, y

    def create_objects(self):

        # Put entrance "i" and exit "o"
        self.deliver_to_room(self.__map.entrance_loc, EntranceDoor())
        self.deliver_to_room(self.__map.exit_loc, ExitDoor())
        self.add_pillars()

        # Put pits
        temp_pit = []
        index = 0
        while index < 2:
            coordinate = self.valid_random_loc()
            if coordinate not in temp_pit:
                temp_pit.append(coordinate)
                self.deliver_to_room(coordinate, Pit())
                print(coordinate, 'pit')
                index += 1
            else:       ####################### delete ###########################
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        temp_pit = []

        # healing potion
        temp_healing = []
        index = 0
        while index < 2:
            coordinate = self.valid_random_loc()
            if coordinate not in temp_healing:
                temp_healing.append(coordinate)
                self.deliver_to_room(coordinate, HealthPotion())
                print(coordinate, 'healing potion')
                index += 1
            else:       ####################### delete ###########################
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        temp_healing = []

        # vision potion
        temp_vision = []
        index = 0
        while index < 2:
            coordinate = self.valid_random_loc()
            if coordinate not in temp_vision:
                temp_vision.append(coordinate)
                self.deliver_to_room(coordinate, VisionPotion())
                print(coordinate, 'vision potion')
                index += 1
            else:       ####################### delete ###########################
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        temp_vision = []

    def add_pillars(self):
        """
        Separate method for adding pillars to avoid more than 1 pillar in a room.
        """
        pillars = ['A', 'I', 'E', 'P']
        temp_list = []
        for item in pillars:
            count = 0                   # counting for possible infinite loop
            while True:
                x, y = self.valid_random_loc()
                print('before add_item PILLAR')           ####################### delete ###########################
                if count >= 20:         # break infinite loop by reset maze. Too many unintended impassible rooms
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXRESET')
                    self.__map.build_maze()
                    self.create_objects()
                    return
                else:
                    count += 1
                if (x, y) not in temp_list and self.__map.traverse_dungeon((x, y)):
                    print('will add_item PILLAR')           ####################### delete ###########################
                    self.deliver_to_room((x, y), Pillar(item))
                    temp_list.append((x, y))
                    break

    def deliver_to_room(self, location, object):
        x = location[0]
        y = location[1]
        self.__room_index[(x, y)].receive_from_factory(object)
        print("success sending items", object, object.letter)       ####################### delete #####################

        # Update map, always show all initial objects
        if self.__map.ver[y][x][1] != ' ':
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + 'M '
        else:
            self.__map.ver[y][x] = self.__map.ver[y][x][0] + object.letter + ' '
