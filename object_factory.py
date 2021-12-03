
class ObjectFactory:

    def __init__(self, maze):
        self.__maze = maze

    def put_inside_room(self):      ######## Move to RoomFactory ##########

        # put entrance "i" and exit "o"
        self.add_item_in_room(0, 0, 'i')
        self.add_item_in_room(self.width-1, self.height-1, 'O')
        self.add_pillars()

        # put traps
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.width - 1), randrange(1, self.height - 1), 'X')

        # put healing potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.width - 1), randrange(1, self.height - 1), 'H')

        # put vision potions
        for _ in range(2):   # change based on difficulty
            self.add_item_in_room(randrange(1, self.width - 1), randrange(1, self.height - 1), 'V')

    def add_pillars(self):      ######## Move to RoomFactory ##########
        """
        Separate method for adding pillars to avoid more than 1 pillar in a room.
        """
        pillars = ['A', 'I', 'E', 'P']

        index = 0
        while index < len(pillars):
            x, y = randrange(0, self.width), randrange(0, self.height)
            if (x, y) not in self.__items.keys():
                self.add_item_in_room(x, y, pillars[index])
                index += 1

    def add_item_in_room(self, x, y, letter):      ######## Move to RoomFactory ##########
        if self.ver[y][x][1] != ' ':
            self.ver[y][x] = self.ver[y][x][0] + 'M '
            self.__items[(x, y)].append(letter)
        else:
            self.ver[y][x] = self.ver[y][x][0] + letter + ' '
            self.__items[(x, y)] = [letter]
