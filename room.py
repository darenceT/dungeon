from sound_fx import SoundFx


class Room:

    def __init__(self, map, x_loc, y_loc):
        self.__map = map
        self.__x_loc = x_loc
        self.__y_loc = y_loc
        self.__impassible = False
        self.__objects = []

    @property
    def impassible(self):
        return self.__impassible

    @impassible.setter
    def impassible(self, change=True):
        if self.__impassible:
            raise ValueError('Redundancy, Room has already been made impassible')
        else:
            self.__impassible = change

    @property
    def objects(self):
        return self.__objects

    def enter_room(self):
        """
        Player enters room, method checks impassible status. Print room.
        """
        SoundFx.enter_room()
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
        :return: object from factory
        :rtype: DungeonObject
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

'''
        
Room
    • Contains default constructor and all methods you deem necessary -- modular design is CRUCIAL
    • Contains the following items/behaviors
        o (Possibly a) Healing Potion - heals 5-15 hit points (this amount will be randomly generated 
        -- you can modify the range)
               
        o (Possibly a) Pit - damage a pit can cause is from 1-20 hit points (this amount will be 
        randomly generated - you can modify the range)
        o (Possibly an) Entrance - only one room will have an entrance and the room that contains the 
        entrance will contain NOTHING else
        o (Possibly an) Exit - only one room will have an exit and the room that contains the exit 
        will contain NOTHING else
        o (Possibly a) Pillar of OO - four pillars in game and they will never be in the same room
        o Doors-N,S,E,W
        o 10% possibility (this is a constant that you can modify) room will contain a healing potion, 
        vision potion, and pit (each of these are independent of one another)
        o Vision Potion - can be used to allow user to see eight rooms surrounding current room as 
        well as current room (location in maze may cause less than 8 to be displayed)
    • Must contain a _ _ str _ _ () method that builds a 2D Graphical representation of the room 
    (NOTE: you may use any graphical components that you wish). The (command line) representation is 
    as follows:
        o * - * will represent a north/south door (the - represents the door). If the room is on a 
        boundary of the maze (upper or lower), then that will be represented with ***
        o East/west doors will be represented in a similar fashion with the door being the | character 
        as opposed to a -.
        o In the center of the room you will display a letter that represents what the room contains. 
        Here are the letters to use and what they represent:
            ▪ M - Multiple Items
            ▪ X-Pit
            ▪ i - Entrance (In)
            ▪ O-Exit(Out)
            ▪ V-VisionPotion
            ▪ H-HealingPotion
            ▪ <space>-EmptyRoom
            ▪ A, E, I, P - Pillars


'''