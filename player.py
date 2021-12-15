# Manuel Duarte
from random import randint


class Player:
    def __init__(self, name="Player 1", sound=None):
        self.__name = name
        self.__sound = sound
        self.__hitpoints = randint(60, 80)
        self.__vision_potions = []
        self.__health_potions = []
        self.__pillars = []

    @property
    def name(self):
        """
        Gets the player name
        :return: player name
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the name and makes sure that an str is passed
        :param name: name of player obtained from Instructions()
        :type name: str
        :raises: if input is not a string
        """
        if not name.isalpha():
            raise Exception ('Name must be a string')
        self.__name = name

    @property
    def hitpoints(self):
        """
        Get player's current hitpoints
        :return: amount of player health
        :rtype: int
        """
        return self.__hitpoints

    @property
    def health_potions(self):
        """
        Getter for count of health points
        :return: amount of health potions
        :rtype: int
        """
        return self.__health_potions

    @health_potions.setter
    def health_potions(self, potion):
        """
        Setter for count of health of potions
        :param potion: healing potion encountered in room 
        :type potion: HealingPotion
        :raises: Incorrect DungeonObject
        """
        if potion.letter != 'H':
            raise Exception('This is not the correct DungeonObject')
        self.__health_potions.append(potion)

    @property
    def vision_potions(self):
        """
        Get the current count vision potions
        :return: amount of vision potions
        :rtype: int
        """
        return self.__vision_potions

    @vision_potions.setter
    def vision_potions(self, potion):
        """
        Setter for count of vision of potions
        :param potion: vision potion encountered in room 
        :type potion: VisionPotion
        :raises: Incorrect DungeonObject
        """
        if potion.letter != 'V':
            raise Exception('This is not the correct DungeonObject')
        self.__vision_potions.append(potion)

    @property
    def pillars(self):
        """
        Gets the container of pillar keys
        :return: inventory of pillar keys
        :rtype: Pillar []
        """
        return self.__pillars

    @pillars.setter
    def pillars(self, key):
        """
        Set the name and makes sure that an str is passed
        :param key: name of player obtained from Instructions()
        :type key: str
        :raises: if input is not correct DungeonObject
        """
        if key.letter not in ['A', 'E', 'I', 'P']:
            raise Exception('This is not the correct DungeonObject')
        self.__pillars.append(key)

    def interact_objects(self, objects):
        """
        Interact with objects in Room, add potions & pillars to inventory.
        :param objects: objects in each room 
        :type objects: DungeonObject
        """
        for obj in objects:
            if obj.letter == 'i':
                obj.function()
            elif obj.letter == 'O':
                obj.function(self.__pillars, self.name)
            elif obj.letter == 'X':
                self.__fall_pit(obj)
            elif obj.letter in ['H', 'V']:
                if obj.letter == 'H':
                    obj.inspect()
                    self.health_potions = obj
                else:
                    self.vision_potions = obj
                print(f'  {self.name} added {obj} to backpack!')
            elif obj.letter in ['A', 'E', 'I', 'P'] and obj not in self.__pillars:
                self.__sound.pillar()
                obj.function()
                self.pillars = obj

    def potion_menu(self, map=None, loc=None):
        """
        Displays the current counts of potions available to the player
        :param map: map of dungeon, needed for vision potion
        :type map: BuildDungeon
        :param loc: location of player, needed for vision potion
        :type loc: tuple(x-coord, y-coord)
        """
        selection = None
        options = ['r']
        if len(self.health_potions) != 0:
            options.append('h')
        if len(self.vision_potions) != 0:
            options.append('v')
        while selection not in options:
            print(f'\n  You have {len(self.health_potions)} health potion(s),'
                  f'and {len(self.vision_potions)} vision potion(s):')
            if len(self.health_potions) != 0:
                print(f'\t [h] Use a health potion')
            if len(self.vision_potions) != 0:
                print(f'\t [v] Use a vision potion')
            print(f'\n\t [r] Return')
            print_options = ', '.join(options)
            selection = input(f'\n  Enter your option(s) [{print_options}]: ').strip().lower()
            if selection == 'h' and 'h' in options:
                self.__use_health_potion()
                break
            elif selection == 'v' and 'v' in options:
                self.__use_vision_potion(map, loc)
                break
            elif selection == 'r':
                break

    def __use_health_potion(self):
        """
        Replenish health using potions
        :raises: if player is out of potions
        """
        if len(self.health_potions) == 0:
            raise Exception("You do not any health potion to use")

        for potion in self.__health_potions:
            if potion.letter == "H":
                self.__health_potions.remove(potion)
                self.__sound.health_potion()
                print(f'\n  You used a {potion}, {potion.health_points} health replenished!')
                self.__hitpoints += potion.health_points
                break
            else:
                raise Exception('Wrong object in health potion container')

        if self.__hitpoints > 100:
            self.__hitpoints = 100
        print(f"  {self.__name}'s health is now {self.__hitpoints} health points")

    def __use_vision_potion(self, map, loc):
        """
        Reveal surround 8 rooms, less if at border of maze.
        :param map: map of dungeon, needed for potion's function
        :type map: BuildDungeon
        :param loc: location of player, needed for potion's function
        :type loc: tuple(x-coord, y-coord)
        :raises: if player is out of potions
        """
        if len(self.vision_potions) == 0:
            raise Exception("You do not have any vision potion to use")

        for potion in self.__vision_potions:
            if potion.letter == "V":
                potion.function(map, loc)
                self.__sound.vision_potion()
                self.__vision_potions.remove(potion)
                break
            else:
                raise Exception('Wrong object in vision potion container')

    def __fall_pit(self, pit):
        """
        Call pit function to affect player's health
        :param pit: pit object
        :type pit: Pit
        """
        damage = pit.function()
        if damage > 0:
            self.__sound.pit()
            self.__hitpoints -= damage

    def __str__(self):
        """
        Overides default Oject print and includes print out of player's information and inventory
        """
        return (
            f"\n  Name: {self.__name}\n"
            f"  Hit Points: {self.__hitpoints}\n"
            f"  Total Healing Potions: {len(self.health_potions)}\n"
            f"  Total Vision Potions: {len(self.vision_potions)}\n"
            f"  Pillars Keys Found: {len(self.__pillars)}\n")