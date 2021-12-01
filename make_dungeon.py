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

        # Create & Check entrance to exit pathway, else recreate
        while True:
            # Entrance location
            #     randomize start location (OPTION)
            # walk(randrange(w), randrange(h))
            #     specify location e.g. 0,0 for top left: x, y
            break_wall(1, 0)
            if self.traverse_dungeon():    # if true, break loop
                break

    def traverse_dungeon(self):
        maze = [[0] * self.__width + [1] for _ in range(self.__height)] + [[1] * (self.__width + 1)]
        maze[self.__height-1][self.__width-1] = 'E'    # Exit at bottom right corner
        # maze[0][0] = 'E'
        stack = [(0, 0)]     # stack with entrance room pushed

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
        for (a, b) in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s


if __name__ == '__main__':
    p = MakeDungeon(8, 4)
    p.make()

