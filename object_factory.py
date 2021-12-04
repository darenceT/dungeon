from random import randrange


class ObjectFactory:

    def __init__(self, maze):
        self.__maze = maze
        self.__items = {}
        self.pillars_loc = []           # delete???
        self.put_inside_rooms()

    def get_items(self):
        return self.__items

    items = property(get_items)

    def valid_random_loc(self):
        """
        Generate random locations while avoiding impassible, entrance and exit rooms
        :return: random location
        :rtype: tuple
        """
        while True:
            x = randrange(0, self.__maze.width)
            y = randrange(0, self.__maze.height)
            if (x, y) not in self.__maze.impassible_rooms:
                if (x == 0 and y == 0) or (x == self.__maze.width - 1 and y == self.__maze.height - 1):
                    continue
                else:
                    return x, y

    def put_inside_rooms(self):

        # Put entrance "i" and exit "o"
        self.add_item_in_room((0, 0), 'i')
        self.add_item_in_room((self.__maze.width-1, self.__maze.height-1), 'O')
        self.add_pillars()

        # Put traps
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(self.valid_random_loc(), 'X')

        # Put healing potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(self.valid_random_loc(), 'H')

        # Put vision potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(self.valid_random_loc(), 'V')

    def add_pillars(self):
        """
        Separate method for adding pillars to avoid more than 1 pillar in a room.
        """
        pillars = ['A', 'I', 'E', 'P']
        temp_list = []
        for item in pillars:
            while True:
                x, y = self.valid_random_loc()
                if (x, y) not in temp_list and self.__maze.traverse_dungeon(x, y):
                    self.add_item_in_room((x, y), item)
                    temp_list.append((x, y))
                    break

        # index = 0
        # while index < len(pillars):
        #     x, y = randrange(0, self.__maze.width), randrange(0, self.__maze.height)
        #     if (x, y) not in self.__items.keys() and (x, y) not in self.__maze.impassible_rooms \
        #             and self.__maze.traverse_dungeon(x, y):
        #         self.add_item_in_room((x, y), pillars[index])
        #         self.pillars_loc.append((x, y))
        #         index += 1
        #         print('pillar')

    def add_item_in_room(self, location, letter):
        x = location[0]
        y = location[1]
        if self.__maze.ver[y][x][1] != ' ':
            self.__maze.ver[y][x] = self.__maze.ver[y][x][0] + 'M '
            self.__items[(x, y)].append(letter)
        else:
            self.__maze.ver[y][x] = self.__maze.ver[y][x][0] + letter + ' '
            self.__items[(x, y)] = [letter]
