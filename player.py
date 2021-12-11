# Name: Manuel Duarte 
from pillar import Pillar
from random import randint


class Player:
    def __init__(self, name="Player 1"):
        self.__name = name
        self.__hitpoints = randint(75, 100)
        # self.__healingpotions = []
        # self.__visionpotioncount = 0
        # self.__pillarsfound = []
        self.__backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hitpoints(self):
        return self.__hitpoints

    @property
    def health_potions(self):
        count = 0
        for o in self.__backpack:
            if o.letter == 'H':
                count += 1
        return count

    @property
    def vision_potions(self):
        count = 0
        for o in self.__backpack:
            if o.letter == 'V':
                count += 1
        return count
    # @property
    # def visionpotioncount(self):
    #     return self.__visionpotioncount
    #
    # @property
    # def pillarsfound(self):
    #     return self.__pillarsfound

    def interact_objects(self, objects):
        """
        Interact with objects in Room, add potions & pillars to backpack.
        """
        for obj in objects:
            if obj.letter == 'i':
                obj.function()
            elif obj.letter == 'O':
                obj.function(self.__backpack)
            elif obj.letter == 'X':
                self.__hitpoints -= obj.function()
            elif obj.letter in ['H', 'V']:
                if obj.letter == 'H':
                    obj.function()
                self.__backpack.append(obj)
                print(f'  {self.name} added {obj} to backpack!')
            elif obj not in self.__backpack:        # for pillars
                obj.function()
                self.__backpack.append(obj)

    def potion_menu(self, map=None, loc=None):
        selection = None
        options = ['r']
        if self.health_potions != 0:
            options.append('h')
        if self.vision_potions != 0:
            options.append('r')
        while selection not in ["h", "v", "r"]:
            print(f'\n  You have {self.health_potions} health potion(s),'
                  f'and {self.vision_potions} vision potion(s):')
            if self.health_potions != 0:
                print(f'\t [h] Use a health potion')
            if self.vision_potions != 0:
                print(f'\t [v] Use a vision potion')
            print(f'\n\t [r] Return')
            selection = input('\n  Your selection: ')
            if selection == 'h':
                self.use_health_potion()
                break
            elif selection == 'v':
                self.use_vision_potion(map, loc)
                break
            elif selection == 'c':
                break

    def use_health_potion(self):
        if self.health_potions == 0:
            raise Exception("You do not any health potion to use")

        for o in self.__backpack:
            if o.letter == "H":
                # potion = o
                self.__backpack.remove(o)
        print(f'  You used a {o}!')

        # Does not allow hitpoints to go over 100
        # Remove if going over 100 is allowed
        # self.__hitpoints += potion.points

        # totalhitpoints = self.__hitpoints + potion.points
        # if totalhitpoints <= 100:
        #     self.__hitpoints = totalhitpoints
        # else:
        #     self.__hitpoints = 100

        self.__hitpoints = 100
        print(f"  Took healing potion. Hit points restored to {self.__hitpoints}")

    def use_vision_potion(self, map, loc):
        if self.vision_potions == 0:
            raise Exception("You do not any vision potion to use")

        for o in self.__backpack:
            if o.letter == "V":
                o.function(map, loc)
                self.__backpack.remove(o)
        print('  You used a vision potion BACKPACK') ################

    def use_damage(self, pit):
        self.__hitpoints -= pit.damage
        print(f"Took damage. Lost {pit.damage} points.")

    def __str__(self):
        pillars = 0
        health_pots = 0
        vision_pots = 0
        for obj in self.__backpack:
            if obj.letter in ['A', 'E', 'I', 'P']:
                pillars += 1
            elif obj.letter == 'H':
                health_pots += 1
            elif obj.letter == 'V':
                vision_pots += 1
        return (
            f"\n  Name: {self.__name}\n"
            f"  Hit Points: {self.__hitpoints}\n"
            f"  Total Healing Potions: {health_pots}\n"
            f"  Total Vision Potions: {vision_pots}\n"
            f"  Pillars Keys Found: {pillars}\n"
        )



    # def add_healing_potion(self, potion):
    #     self.__healingpotions.append(potion)
    #     print("Added healing potion to inventory.")

    # def takehealing_potion(self):
    #     if len(self.__healingpotions) == 0:
    #         print("You are all out of healing potions.")
    #     else:
    #         potion = self.__healingpotions.pop(0)
    #         # Does not allow hitpoints to go over 100
    #         # Remove if going over 100 is allowed
    #         # self.__hitpoints += potion.points
    #         totalhitpoints = self.__hitpoints + potion.points
    #         if totalhitpoints <= 100:
    #             self.__hitpoints = totalhitpoints
    #         else:
    #             self.__hitpoints = 100
    #         print(f"Took healing potion. Hit points restored to {self.__hitpoints}")

    # def addvisionpotion(self):
    #     self.__visionpotions += 1
    #     print("Added vision potion to inventory.")