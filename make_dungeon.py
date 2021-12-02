# https://rosettacode.org/wiki/Maze_generation#Python

from random import shuffle, randrange


class MakeDungeon:

    def __init__(self, w=16, h=8):
        self.__width = w
        self.__height = h
        self.__ver = []
        self.__hor = []
        self.__items = {}

    def get_items(self):
        return self.__items

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def set_ver(self, ver):
        self.__ver = ver

    def get_ver(self):
        return self.__ver

    def set_hor(self, hor):
        self.__hor = hor

    def get_hor(self):
        return self.__hor

    width = property(get_width, set_width)
    height = property(get_height, set_height)
    ver = property(get_ver, set_ver)
    hor = property(get_hor, set_hor)
    items = property(get_items)

    # place holder method for selecting difficulty, not functional
    def difficulty(self, mode):
        mode = mode.lower().strip()
        if mode == 'easy':
            self.__width = 12
            self.__height = 6
        elif mode == 'medium':
            self.__width = 20
            self.__height = 10
        elif mode == 'hard':
            self.__width = 40
            self.__height = 20
        else:
            raise ValueError('Input does not match "easy", "medium", or "hard" mode options')

    def make(self):
        # (wide x height of 0s + last column 1s) + last row 1s
        visited = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]

        # (wide + 1 x height) vertical walls. +[[]] allows printing of bottom wall
        self.__ver = [["|  "] * self.__width + ['|'] for _ in range(self.__height)] + [[]]

        # wide (+--) + 1 (+) x height + 1) horizontal walls
        self.__hor = [["+--"] * self.__width + ['+'] for _ in range(self.__height + 1)]

        def break_wall(x, y):
            # change 0 to 1 after room visited
            visited[y][x] = 1

            # initializes an array with all four neighbors of the current room
            # [(-1,0),(0,1),(1,0),(0,-1)]
            # d = [(west),(south),(east),(north)]
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]

            # randomize order of next room to visit
            shuffle(d)

            for (xx, yy) in d:
                # if neighbor has been visited or at grid border, skip to next neighbor
                if visited[yy][xx]:
                    continue
                # remove horizontal wall, "+--" turns into "+  "
                if xx == x:
                    self.__hor[max(y, yy)][x] = "+  "
                # remove vertical wall, "|"   turns into "   "
                if yy == y:
                    self.__ver[y][max(x, xx)] =
                # move to next room
                break_wall(xx, yy)

        # Create & Check entrance to exit pathway, else recreate
        while True:
            # Entrance location
            #     randomize start location (OPTION)
            # break_wall(randrange(w), randrange(h))
            #     specify location e.g. 0,0 for top left: x, y
            break_wall(0, 0)
            if self.traverse_dungeon():    # if true, break loop
                break

        self.put_inside_room()
        # call pillars to assign location

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

    def visited_potion(self, x, y, potion):         ######## Not tested ###########
        if potion in self.__items[(x, y)]:
            self.__items[(x, y)].remove(potion)
            if len(self.__items[(x, y)]) == 0:      # update map for empty room
                self.ver[y][x] = self.ver[y][x][0] + '  '
            elif len(self.__items[(x, y)]) == 1:    # update map for single item in room
                self.ver[y][x] = self.ver[y][x][0] + self.__items[(x, y)] + ' '
        else:
            raise ValueError('Game error, no potion at this location to change to used potion')

    def traverse_dungeon(self):
        maze = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]
        maze[self.__height-1][self.__width-1] = 'E'    # Exit at bottom right corner
        stack = [(0, 0)]     # stack starts with entrance room

        while len(stack) > 0:
            x, y = stack.pop()

            if maze[y][x] == 'E':
                return True
            # 1 is already visited or outside of maze
            if maze[y][x] == 1:
                continue
            # mark current location as visited
            maze[y][x] = 1
            # push all possible neighbor routes, "0", to stack; Order is N, S, E, W
            if maze[y-1][x] in (0, 'E') and self.__hor[y][x] == "+  ":
                stack.append((x, y-1))
            if maze[y+1][x] in (0, 'E') and self.__hor[y+1][x] == "+  ":
                stack.append((x, y+1))
            if maze[y][x+1] in (0, 'E') and self.__ver[y][x+1] == "   ":
                stack.append((x+1, y))
            if maze[y][x-1] in (0, 'E') and self.__ver[y][x] == "   ":
                stack.append((x-1, y))
        return False

    def __str__(self):
        s = ""
        for a, b in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

# Here are the letters to use and what they represent:
#     ▪ M - Multiple Items
#     ▪ X-Pit
#     ▪ i - Entrance (In)
#     ▪ O-Exit(Out)
#     ▪ V-VisionPotion
#     ▪ H-HealingPotion
#     ▪ -EmptyRoom


# delete this later for submission
if __name__ == '__main__':
    p = MakeDungeon(8, 4)
    p.make()
    print(p)

    for i in p.items:
        print(i, p.items[i])
