
class Room:

    def __init__(self, map, x_loc, y_loc):
        self.__map = map
        self.__x_loc = x_loc
        self.__y_loc = y_loc
        self.__impassible = False
        self.__entrance = None            ####################### ??? delete ############
        self.__exit = None                ######################## ??? delete ##########
        self.__pit = None
        self.__pillar = None
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
            print('now impassible')               ####################### delete ###########################

    def set_entrance(self, door):
        if self.__entrance:
            raise ValueError('Redundancy, Entrance has already been set')
        else:
            self.__entrance = door
            print('entrance set')               ####################### delete ###########################

    def set_exit(self, door):
        if self.__exit:
            raise ValueError('Redundancy, Exit has already been set')
        else:
            self.__exit = door
            print('Exit set')               ####################### delete ###########################

    def set_pit(self, object):
        if self.__pit:
            raise ValueError('Redundancy, pit has already been set')
        else:
            self.__pit = object
            print('pit added')               ####################### delete ###########################

    def set_pillar(self, pillar):
        if self.__pillar:
            raise ValueError('Redundancy, pillar has already been set')
        else:
            self.__pillar = pillar
            print('pillar has been added')               ####################### delete ###########################

    def enter_room(self):
        """
        Player enters room, method checks impassible status.
        """
        if not self.__impassible:
            print(f'entered room (x: {self.__x_loc}, y: {self.__y_loc}):')
        else:
            raise ValueError('Room has been set impassible, you are trespassing!')
        print(self)

    def obtain_items(self):
        """
        Allow player to obtain objects in room.
        For loop will update display of room for potions picked up.
        :return: objects
        :rtype: list of characters
        """
        ref_list = {'i': 'Entrance', 'O': 'Exit', 'X': 'Pit', 'V': 'Vision Potion', 'H': 'Healing Potion',
                    'A': 'Pillar of Abstraction!', 'E': 'Pillar of Encapsulation!', 'I': 'Pillar of Inheritance!',
                    'P': 'Pillar of Polymorphism'}
        pickup = self.__objects
        if self.__objects:
            print('     This room contains:', ', '.join([ref_list[i.letter] for i in self.__objects]), '\n')
        else:
            print('     This room is empty.\n')

        for obj in self.__objects:
            if obj.letter in ['H', 'V']:
                self.__objects.remove(obj)
        return pickup

    def receive_from_factory(self, obj):
        """
        No function called for potions, only goes to object list.
        """
        route = {'A': self.set_pillar, 'E': self.set_pillar, 'I': self.set_pillar, 'P': self.set_pillar,
                 'i': self.set_entrance, 'O': self.set_exit, 'X': self.set_pit, 'H': None, 'V': None}
        print('success receiving:', obj)            ####################### delete ###########################

        if obj.letter in ['A', 'E', 'I', 'P']:
            route[obj.letter](obj.letter)
        elif obj.letter in ['i', 'O', 'X']:
            route[obj.letter](obj)
        self.__objects.append(obj)

    def __str__(self):
        display = ' '
        if len(self.__objects) == 1:
            display = self.__objects[0].letter
        elif len(self.__objects) > 1:
            display = 'M'

        x = self.__x_loc
        y = self.__y_loc
        self.__map.ver[y][x] = self.__map.ver[y][x][0] + display + ' '

        return '\n               ' + self.__map.hor[y][x] + \
               '+\n               ' + self.__map.ver[y][x] + self.__map.ver[y][x + 1][0] + \
               '\n               ' + self.__map.hor[y + 1][x] + '+'

'''
    # def set_health_potion(self, remove=False):
    #     if not self.__health_potion and not remove:     # add potion
    #         self.__health_potion = True
    #         print('Health potion added')               ####################### delete ###########################
    #     elif self.__health_potion and not remove:
    #         raise ValueError('Redundancy, health potion has already been set')
    #     elif self.__health_potion and remove:       # picked up potion
    #         self.__health_potion = False
    #         print('Health potion picked up')               ####################### delete ###########################
    #     elif not self.__health_potion and remove:
    #         raise ValueError('Redundancy, no health potion to remove')

    # def set_health_potion(self):
    #     if self.__health_potion:
    #         raise ValueError('Redundancy, health potion has already been set')
    #     else:
    #         self.__health_potion = True
    #         print('Health potion added')               ####################### delete ###########################
    #
    # def set_vision_potion(self, remove=False):
    #     if not self.__vision_potion and not remove:     # add potion
    #         self.__vision_potion = True
    #         print('Vision potion added')               ####################### delete ###########################
    #     elif self.__vision_potion and not remove:
    #         raise ValueError('Redundancy, vision potion has already been set')
    #     elif self.__vision_potion and remove:       # picked up potion
    #         self.__vision_potion = False
    #         print('Vision potion picked up')               ####################### delete ###########################
    #     elif not self.__vision_potion and remove:
    #         raise ValueError('Redundancy, no vision potion to remove')

    def get_health_chance(self):
        return self.__healthChance

    def __str__(self):
        item_count = 0;
        if self.__healthPotion:
            item_count += 1
        if self.__visionPotion:
            item_count += 1

        if item_count > 1:
            return "M"

        return "Health potion: " + str(self.__healthPotion) + "\n" \
               + "Vision potion: " + str(self.__visionPotion) + "\n" \
               + "Pillar: " + str(self.__pillar) + "\n" \
               + "Pit: " + str(self.__pit) + "\n" \
               + "Impassable: " + str(self.__impassable) + "\n" \
               + "Entrance: " + str(self.__entrance) + "\n" \
               + "Exit: " + str(self.__exit) + "\n\n"

    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_impassible(self, is_impassable):
        self.__impassable = is_impassable

    def set_exit(self):
        self.__exit = True
        
        
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

Example: Room 1,1 might look like 
* - *
| P |
* - *

Room 0,0 might look like 
* * *
* E |
* - *



'''