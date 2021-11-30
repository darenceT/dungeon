# https://rosettacode.org/wiki/Maze_generation#Python

from random import shuffle, randrange


class MakeDungeon:

    def __init__(self, w=16, h=8):
        self.__width = w
        self.__height = h

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

    def make_grid(self):
        # (wide x height of 0s + last column 1s) + last row 1s
        visited = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]

        # (wide + 1 x height) vertical walls. +[[]] allows printing of bottom wall
        ver = [["|  "] * self.__width + ['|'] for _ in range(self.__height)] + [[]]

        # wide (+--) + 1 (+) x height + 1) horizontal walls
        hor = [["+--"] * self.__width + ['+'] for _ in range(self.__height + 1)]

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
                    hor[max(y, yy)][x] = "+  "
                # remove vertical wall, "|"   turns into "   "
                if yy == y:
                    ver[y][max(x, xx)] = "   "
                # move to next room
                break_wall(xx, yy)

        # START location
            # randomize start location
        # walk(randrange(w), randrange(h))
            # specify location e.g. 0,0 for top left: x, y
        break_wall(1, 0)

        # print maze
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s


if __name__ == '__main__':
    p = MakeDungeon(2, 2)
    print(p.make_grid())
