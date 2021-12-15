

class Room:
    """
    Each room of dungeon (BuildDungeon) class, contains objects for player to interact.
    Objects will be removed from room as appropriate (obtained potions and keys).
    """
    def __init__(self, map, x_loc, y_loc):
        """
        Creation of room requires map and current location of room from BuildDungeon
        Room is set as impassible which cannot contain essential items: exit, entrance,
        or pillars.
        :param map: map of dungeon
        :type map: BuildDungeon
        :param x_loc: x-coordinate of room
        :type x_loc: int
        :param y_loc: y-coordinate of room
        :type y_loc: int
        """
        self.__map = map
        self.__x_loc = x_loc
        self.__y_loc = y_loc
        self.__impassible = False
        self.__objects = []

    @property
    def impassible(self):
        """
        Getter for status of room impassibility
        :return: impassibility status
        :rtype: bool
        """
        return self.__impassible

    @impassible.setter
    def impassible(self, change):
        """
        Setter for impassibility of room
        :param change: impassibility of room
        :type change: bool
        :raises: if impassible status has already been set to True
        """
        if self.__impassible:
            raise ValueError('Redundancy, Room has already been made impassible')
        else:
            self.__impassible = change

    @property
    def objects(self):
        """
        Getter for objects of room
        :return: list of objects in room
        :rtype: DungeonObject []
        """
        return self.__objects

    def enter_room(self):
        """
        Player enters room, method checks impassible status. Print room.
        :raises: if player enters room that is impassible
        """
        if not self.__impassible:
            print(f'entered room (x: {self.__x_loc}, y: {self.__y_loc}):')
        else:
            raise ValueError('Room has been set impassible, you are trespassing!')
        print(self)

    def touch_objects(self):
        """
        Allow player to obtain objects in room.
        For loop will update display of room for potions picked up.
        :return: objects
        :rtype: list of characters
        """
        if self.__objects:
            print('     This room contains:', ', '.join([str(x) for x in self.__objects]), '\n')
        else:
            print('     This room is empty.\n')

        touched_objects = []
        temp_for_removal = []
        for obj in self.__objects:
            touched_objects.append(obj)
            if obj.letter in ['H', 'V']:
                temp_for_removal.append(obj)

        while temp_for_removal:
            self.__objects.remove(temp_for_removal.pop())
        return touched_objects

    def receive_from_factory(self, obj):
        """
        Receive object from factory and adds to room's object list.
        :param obj: dungeon object
        :type obj: DungeonObject
        """
        self.__objects.append(obj)

    def __str__(self):
        '''
        Create print of room with letter representing objects, M for multiple.
        '''
        display = ' '
        if len(self.__objects) == 1:
            display = self.__objects[0].letter
        elif len(self.__objects) > 1:
            display = 'M'

        x = self.__x_loc
        y = self.__y_loc
        self.__map.ver[y][x] = self.__map.ver[y][x][0] + display + ' '
        spaces = '                            '
        return f'\n{spaces}' + self.__map.hor[y][x] + \
               f'+\n{spaces}' + self.__map.ver[y][x] + self.__map.ver[y][x + 1][0] + \
               f'\n{spaces}' + self.__map.hor[y + 1][x] + '+\n'