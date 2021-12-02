
class Room:
    def __init__(self, maze, x, y):
        self.__maze = maze.p
        self.__x = x
        self.__y = y
        self.__room_items = []

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_maze(self):        # is this necessary?
        return self.__maze

    def get_room_items(self):
        if (self.__x, self.__y) in self.__maze.items.keys():
            self.__room_items = self.__maze.items[(self.__x, self.__y)]
            print(self.__room_items)
        else:
            print(self.__room_items)

    def print(self):        # delete redundant code, call __str__?
        print(f'Current room (x: {self.__x}, y: {self.__y}): ')
        print(self)

    def __str__(self):
        xx = self.__x
        yy = self.__y
        return self.__maze.hor[yy][xx] + '+\n' + self.__maze.ver[yy][xx] +\
               self.__maze.ver[yy][xx + 1][0] + '\n' + self.__maze.hor[yy + 1][xx] + '+'

    x = property(get_x)
    y = property(get_y)
    maze = property(get_maze)       # is this necessary?