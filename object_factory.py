from random import shuffle, randrange


class ObjectFactory:

    def __init__(self, maze):
        self.__maze = maze
        self.__items = {}
        self.put_inside_rooms()

    def get_items(self):
        return self.__items

    items = property(get_items)

    def put_inside_rooms(self):

        # Put entrance "i" and exit "o"
        self.add_item_in_room(0, 0, 'i')
        self.add_item_in_room(self.__maze.width-1, self.__maze.height-1, 'O')
        self.add_pillars()

        # Put traps
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.__maze.width - 1), randrange(1, self.__maze.height - 1), 'X')

        # Put healing potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.__maze.width - 1), randrange(1, self.__maze.height - 1), 'H')

        # Put vision potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.__maze.width - 1), randrange(1, self.__maze.height - 1), 'V')

    def add_pillars(self):
        """
        Separate method for adding pillars to avoid more than 1 pillar in a room.
        """
        pillars = ['A', 'I', 'E', 'P']

        index = 0
        while index < len(pillars):
            x, y = randrange(0, self.__maze.width), randrange(0, self.__maze.height)
            if (x, y) not in self.__items.keys():
                self.add_item_in_room(x, y, pillars[index])
                index += 1

    def add_item_in_room(self, x, y, letter):
        if self.__maze.ver[y][x][1] != ' ':
            self.__maze.ver[y][x] = self.__maze.ver[y][x][0] + 'M '
            self.__items[(x, y)].append(letter)
        else:
            self.__maze.ver[y][x] = self.__maze.ver[y][x][0] + letter + ' '
            self.__items[(x, y)] = [letter]
