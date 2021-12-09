from object_factory import ObjectFactory
from room import Room
from random import shuffle, randrange


class BuildDungeon:
    def __init__(self, mode):
        self.__width = 0
        self.__height = 0
        self.__ver = []
        self.__hor = []
        self.__entrance_loc = ()
        self.__difficulty(mode)
        self.__exit_loc = (self.__width - 1, self.__height - 1)
        self.__room_index = {}
        self.__pillars_loc = []
        self.__build_maze()
        self.__objects_for_traversal()
        self.__factory = ObjectFactory(self)  # factory puts objects into maze

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def ver(self):
        return self.__ver

    @property
    def hor(self):
        return self.__hor

    @property
    def factory(self):
        return self.__factory

    @property
    def entrance_loc(self):
        return self.__entrance_loc

    @property
    def exit_loc(self):
        return self.__exit_loc

    @property
    def room_index(self):
        return self.__room_index

    @property
    def pillars_loc(self):
        return self.__pillars_loc

    def __difficulty(self, mode):
        if mode == 1:
            self.__width = 8
            self.__height = 4
        elif mode == 2:
            self.__width = 16
            self.__height = 8
        elif mode == 3:
            self.__width = 24
            self.__height = 12
        else:
            raise ValueError('Input is not between 1 to 3 for difficulty mode')

        self.__entrance_loc = (randrange(0, self.__width // 2,), randrange(0, self.__height // 2))

    def __build_maze(self):
        """
        Build maze by first creating a grid of 1s, and 0s, where unvisited 0 becomes 1 when visited.
        Walls are created vertically, "ver" and horizontally, "hor". Helper function break_wall
        creates path of maze.
        Credit for logic/algorithm to https://rosettacode.org/wiki/Maze_generation#Python
        """
        # (wide x height of 0s + last column 1s) + last row 1s
        visited = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]
        # (wide + 1 x height) vertical walls. "+[[]]" allows printing of bottom wall
        self.__ver = [["|  "] * self.__width + ['|'] for _ in range(self.__height)] + [[]]
        # wide (+--) + 1 (+) x (height + 1) horizontal walls
        self.__hor = [["+--"] * self.__width + ['+'] for _ in range(self.__height + 1)]

        def __break_wall(location):
            """
            Path of maze created using visited grid. In each room, neighbors ("d" list) are approached
            randomly by using time.shuffle.
            Room objects created during wall-breaking process, indexed into dictionary "__room_index"
            """
            x, y = location
            # create room and map index, reset so room is passable
            self.room_index[location] = Room(self, x, y)
            self.room_index[location].impassible = False
            # change 0 to 1 after room visited
            visited[y][x] = 1
            # [(west),(south),(east),(north)] neighbors of the current room
            neighbors = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(neighbors)
            for (xx, yy) in neighbors:
                # if neighbor has been visited or at grid border, skip to next neighbor
                if visited[yy][xx]:
                    continue
                # remove horizontal wall, "+--" turns into "+  "
                if xx == x:
                    self.__hor[max(y, yy)][x] = "+  "
                # remove vertical wall, "|"   turns into "   "
                if yy == y:
                    self.__ver[y][max(x, xx)] = "   "
                # move to next room
                __break_wall((xx, yy))

        __break_wall(self.__entrance_loc)

    def __objects_for_traversal(self):                # need to clean up this code
        while True:
            self.__create_impassible()
            self.__create_pillar_loc()
            if self.__traverse_dungeon(self.__exit_loc):
                for loc in self.__pillars_loc:
                    if not self.__traverse_dungeon(loc):
                        self.__build_maze()
                        return
                break
            else:
                self.__build_maze()
                break

    def __create_pillar_loc(self):
        while len(self.__pillars_loc) < 4:
            x = randrange(0, self.__width)
            y = randrange(0, self.__height)
            if (x, y) != self.__entrance_loc and (x, y) != self.__exit_loc \
                    and (x, y) not in self.__pillars_loc:
                self.__pillars_loc.append((x, y))
                print()

    def __create_impassible(self):
        """
        Append to list of impassible rooms to avoid putting objects into these rooms
        Credit to Steph for help with debugging.
        """
        temp_list = []
        # rooms per difficulty, Easy: 1, Normal: 2, Hard: 3
        for _ in range(self.__width // 8):
            while True:
                x = randrange(0, self.__width)
                y = randrange(0, self.__height)
                if (x, y) == self.__entrance_loc or (x, y) == self.__entrance_loc:
                    continue
                elif (x, y) not in temp_list:     # avoid duplicates
                    temp_list.append((x, y))
                    self.room_index[(x, y)].impassible = True
                    self.__hor[y][x] = "+--"
                    self.__ver[y][x] = "|  "
                    self.__ver[y][x + 1] = "|" + self.__ver[y][x + 1][1:3]
                    self.__hor[y + 1][x] = "+--"
                    break

    def __traverse_dungeon(self, target_loc):
        """
        Traverse maze just after walls broken and path created, ensure path from (0, 0)
        to exit, 'E' is possible.
        :return: True if path to exit is possible
        :rtype: boolean
        """
        print('traverse')       ####################### delete ########################
        target_x, target_y = target_loc
        maze = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]
        maze[target_y][target_x] = 'E'    # Target
        stack = [self.__entrance_loc]     # stack starts with entrance room
        while len(stack) > 0:
            x, y = stack.pop()
            if maze[y][x] == 'E':
                return True
            # 1 is already visited or outside of maze
            if maze[y][x] == 1:
                continue
            # Check room not impassible and mark current location as visited
            if not self.__room_index[(x, y)].impassible:
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
        s = "        "
        for a, b in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n        '] + b + ['\n        '])
        return s


# delete this later for submission
if __name__ == '__main__':
    p = BuildDungeon(1)
    print(p)