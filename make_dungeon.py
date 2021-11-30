# https://rosettacode.org/wiki/Maze_generation#Python

from random import shuffle, randrange


class MakeDungeon:

    def __init__(self, w=16, h=8):
        self.__width = w
        self.__height = h
        self.__ver = []
        self.__hor = []

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
                    self.__ver[y][max(x, xx)] = "   "
                # move to next room
                break_wall(xx, yy)

        # create & check entrance to exit pathway, else recreate
        # while True:
            # Entrance location
                # randomize start location (OPTION)
            # walk(randrange(w), randrange(h))
                # specify location e.g. 0,0 for top left: x, y
        break_wall(1, 0)

            # if self.traverse_dungeon():
            #     break

    def traverse_dungeon(self):
        exit = (self.__width - 1, self.__height - 1)    # bottom right corner

        while True:
            pass

    def print_dungeon(self):
        s = ""
        for (a, b) in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

    def __str__(self):
        return self.print_dungeon()


if __name__ == '__main__':
    p = MakeDungeon(8, 4)
    p.make()
    print(p)
