from object_factory import ObjectFactory
from random import shuffle, randrange


class MakeDungeon:

    def __init__(self, w=16, h=8):
        self.__width = w
        self.__height = h
        self.__ver = []
        self.__hor = []
        self.build_maze()
        # factory puts objects into maze
        self.__factory = ObjectFactory(self)

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

    def get_factory(self):
        return self.__factory

    width = property(get_width, set_width)
    height = property(get_height, set_height)
    ver = property(get_ver, set_ver)
    hor = property(get_hor, set_hor)
    factory = property(get_factory)

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

    def build_maze(self):
        """
        Build maze by first creating a grid of 1s, and 0s, where unvisited 0 becomes 1 when visited.
        Walls are created vertically, "ver" and horizontally, "hor". Helper function break_wall
        creates path of maze.
        Credit for logic/algorithm to https://rosettacode.org/wiki/Maze_generation#Python
        """
        # (wide x height of 0s + last column 1s) + last row 1s
        visited = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]

        # (wide + 1 x height) vertical walls. +[[]] allows printing of bottom wall
        self.__ver = [["|  "] * self.__width + ['|'] for _ in range(self.__height)] + [[]]

        # wide (+--) + 1 (+) x height + 1) horizontal walls
        self.__hor = [["+--"] * self.__width + ['+'] for _ in range(self.__height + 1)]

        def break_wall(x, y):
            """
            Path of maze created using visited grid. In each room, neighbors ("d" list) are approached
            randomly by using time.shuffle.
            """
            # change 0 to 1 after room visited
            visited[y][x] = 1
            # initializes an array with all four neighbors of the current room
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
                    self.__ver[y][max(x, xx)] = "   "
                # move to next room
                break_wall(xx, yy)

        # Create & Check entrance to exit pathway, else recreate
        while True:
            '''# Entrance location
                # randomize start location (alternate OPTION)
            # break_wall(randrange(w), randrange(h))
                # specify location e.g. 0,0 for top left: x, y '''
            break_wall(0, 0)
            if self.traverse_dungeon():    # if not true, recreate maze
                break

    def traverse_dungeon(self):
        """
        Traverse maze just after walls broken and path created, ensure path from (0, 0)
        to exit, 'E' is possible.
        :return: True if path to exit is possible
        :rtype: boolean
        """
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

    def visited_potion(self, x, y, potion):         ######## Not tested ########### Move to adventure??
        if potion in self.__items[(x, y)]:
            self.__items[(x, y)].remove(potion)
            if len(self.__items[(x, y)]) == 0:      # update map for empty room
                self.ver[y][x] = self.ver[y][x][0] + '  '
            elif len(self.__items[(x, y)]) == 1:    # update map for single item in room
                self.ver[y][x] = self.ver[y][x][0] + self.__items[(x, y)] + ' '
        else:
            raise ValueError('Game error, no potion at this location to change to used potion')

    def __str__(self):
        s = ""
        for a, b in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s


# delete this later for submission
if __name__ == '__main__':
    p = MakeDungeon(8, 4)
    print(p)

    # for i in p.factory.items:                       ############### DELETE
    #     print(i, p.factory.items[i])