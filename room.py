
class Room:
    def __init__(self, maze, x, y):
        self.__maze = maze.p
        self.__x = x
        self.__y = y
        self.__room_items = []
        self.__health_pots = []
        self.__pillar = []

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_room_items(self):
        ref_list = {'i':'Entrance', 'O': 'Exit', 'X': 'Pit', 'V': 'Vision Potion', 'H': 'Healing Potion',
                     'A': 'Pillar of Abstraction!', 'E': 'Pillar of Encapsulation!', 'I': 'Pillar of Inheritance!',
                     'P': 'Pillar of Polymorphism'}
        if (self.__x, self.__y) in self.__maze.factory.items.keys():
            self.__room_items = self.__maze.factory.items[(self.__x, self.__y)]
            print('This room contains:', ', '.join([ref_list[i] for i in self.__room_items]))
        else:
            print('This room is empty')

    def print(self):
        print(f'Current room (x: {self.__x}, y: {self.__y}): ')
        print(self)

    def __str__(self):
        xx = self.__x
        yy = self.__y
        return self.__maze.hor[yy][xx] + '+\n' + self.__maze.ver[yy][xx] +\
               self.__maze.ver[yy][xx + 1][0] + '\n' + self.__maze.hor[yy + 1][xx] + '+'

    x = property(get_x)
    y = property(get_y)
