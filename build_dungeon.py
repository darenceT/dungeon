from object_factory import ObjectFactory
from room import Room
from random import shuffle, randrange


class BuildDungeon:
    """
    Create map of dungeon while simutaneously creating each room.
    Entrance location is randomized, exit location is always at bottom right corner
    Location of pillars are randomized and checked with traversal method to ensure 
    that they are obtainable, then passed to ObjectFactory to create Pillars.
    """
    def __init__(self, mode):
        """
        Difficulty method establishes size of dungeon, assigning __width & __height,
        and assigns entrance and exit locations.
        __hor and __ver are rows & colums strings that can print out the map.
        __room_index is dictionary of Rooms with keys as tuple(x-coord, y-coord).
        __pillars_loc is list of locations where Pillars will be placed
        __build_maze creates map and rooms
        __objects_for_traversal checks critical items and exit are obtainable
        ObjectFactory() turns on factory to create objects for each room,
        passing in this instance for location information.
        :param mode: difficulty level passed from DungeonAdventure (origin from Instructions())
        :type mode: int
        """
        self.__width = 0
        self.__height = 0
        self.__entrance_loc = ()
        self.__exit_loc = ()
        self.__hor = []
        self.__ver = []
        self.__difficulty(mode)
        self.__room_index = {}
        self.__pillars_loc = []
        self.__build_maze()
        self.__objects_for_traversal()
        ObjectFactory(self)

    @property
    def width(self):
        """
        Getter for width of dungeon
        :return: width of dungeon
        :rtype: int
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for height of dungeon
        :return: height of dungeon
        :rtype: int
        """
        return self.__height

    @property
    def ver(self):
        """
        Getter for vertical walls and object of map
        :return: vertical walls and object of map
        :rtype: str
        """
        return self.__ver

    @property
    def hor(self):
        """
        Getter for horizontal walls of map
        :return: horizontal walls of map
        :rtype: str
        """
        return self.__hor

    @property
    def entrance_loc(self):
        """
        Getter for entrance location
        :return: entrance location
        :rtype: tuple(x-coord: int, y-coord: int)
        """
        return self.__entrance_loc

    @property
    def exit_loc(self):
        """
        Getter for exit location of dungeon
        :return: exit location
        :rtype: tuple(x-coord: int, y-coord: int)
        """
        return self.__exit_loc

    @property
    def room_index(self):
        """
        Getter for container of rooms
        :return: container of rooms
        :rtype: dict {tuple(x-coord, y-coord): Room}
        """
        return self.__room_index

    @property
    def pillars_loc(self):
        """
        Getter for locations of where pillars that will be used by object factory
        :return: list of locations for pillars
        :rtype: tuple(x-coord, y-coord)
        """
        return self.__pillars_loc

    def __difficulty(self, mode):
        """
        Create size of dungeon per mode selected at Instructions()
        Entrance location is randomized but limited to top left quarter of dungeon
        so that entrance will not spawn too close to exit.
        Exit location always set at bottom right corner of dungeon.
        :param mode: difficulty level selected at begining of game, Instructions()
        :type mode: int
        :raises: if value is not between 1 and 3
        """
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

        self.__entrance_loc = randrange(0, self.__width // 2,), randrange(0, self.__height // 2)
        self.__exit_loc = self.__width - 1, self.__height - 1

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
            Path of maze created using visited grid. 
            In each room, neighbors ("d" list) are approached randomly by using time.shuffle.
            Room objects created during wall-breaking process, 
            indexed into dictionary "__room_index".
            :param location: location of current room to break wall to create path
            :type location: tuple(x-coord, y-coord)
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

    def __objects_for_traversal(self):
        """
        Ensures pillar locations and exit are obtainable after creating
        impassible rooms. Recreate maze if not obtainable
        """                
        while True:
            self.__create_impassible()
            self.__create_pillar_loc()
            if self.__traverse_dungeon(self.__exit_loc):
                for loc in self.__pillars_loc:
                    if not self.__traverse_dungeon(loc):
                        self.__pillars_loc = []
                        self.__build_maze()
                        self.__objects_for_traversal()
                        break
                break
            else:
                self.__pillars_loc = []
                self.__build_maze()
                self.__objects_for_traversal()
                break

    def __create_pillar_loc(self):
        """
        Random locations for pillars. List will be passed to factory to create Pillars
        """
        while len(self.__pillars_loc) < 4:
            x = randrange(0, self.__width)
            y = randrange(0, self.__height)
            if (x, y) != self.__entrance_loc and (x, y) != self.__exit_loc \
                    and (x, y) not in self.__pillars_loc:
                self.__pillars_loc.append((x, y))

    def __create_impassible(self):
        """
        Create impassible rooms at random locations to make maze more complex.
        Temp list used to avoid duplicates.
        Number of rooms per difficulty, Easy: 1, Normal: 2, Hard: 3
        Credit to Steph Liu for help with debugging.
        """
        temp_list = []
        for _ in range(self.__width // 8):
            while True:
                x = randrange(0, self.__width)
                y = randrange(0, self.__height)
                if (x, y) == self.__entrance_loc or (x, y) == self.__entrance_loc:
                    continue
                elif (x, y) not in temp_list:     
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
        to target, 'E' is possible.
        :param target_loc: target location to traverse from entrance
        :type target_loc: tuple(x-coord, y-coord) of pillars and exit location
        :return: True if path is possible
        :rtype: boolean
        """
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
        """
        Print out map of dungeon using __hor and __ver properties.
        This will reveal all objects even after they have been picked up by player.
        Credit code to https://rosettacode.org/wiki/Maze_generation#Python
        :return: map of dungeon
        :rtype: str
        """
        spaces = '                 '
        map_print = f"\n\n{spaces}"
        for a, b in zip(self.__hor, self.__ver):
            map_print += ''.join(a + [f'\n{spaces}'] + b + [f'\n{spaces}'])
        return map_print


# if __name__ == '__main__':
#     p = BuildDungeon(1)
#     print(p)
