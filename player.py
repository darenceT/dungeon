# Name: Manuel Duarte 

from random import randint


class Player:
    def __init__(self, name="Player 1"):
        self.__name = name
        self.__hitpoints = randint(75, 100)
        self.__healingpotions = []
        self.__visionpotioncount = 0
        self.__pillarsfound = []
        self.__bag = []

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
    def visionpotioncount(self):
        return self.__visionpotioncount

    @property
    def pillarsfound(self):
        return self.__pillarsfound

    def pick_up(self, objects):
        print('before loop', objects)
        for obj in objects:
            print('start for loop', obj)
            if obj.letter == 'X':
                self.__hitpoints -= obj.function()
                obj.visited = True
                continue
            elif obj.letter in ['H', 'V']:
                print('in H & V', obj)
                print(self.__name, 'picked up', obj, '\n')
            # elif obj.letter in ['A', ...] and not in self.__pillarsfound:
            #     self.__pillarsfound.append()
            elif obj not in self.__bag:
                obj.function()
            self.__bag.append(obj)

    def potion_menu(self):
        print("potion menu: you have X potions, use healing or vision?")
        # Display: # health potions and # of vision potion
        # 1. use health potion (option to pick which health potion) obj.letter = "H"
        # 2. use vision potion
        # 3. return to game
        #         if 1:
        #             self.__hitpoints += obj.function()
        #         elif 2:
        #         self.__bag.delete(obj)
        #         elif 3:
        #             return

    def add_healing_potion(self, potion):
        self.__healingpotions.append(potion)
        print("Added healing potion to inventory.")

    def takehealing_potion(self):
        if len(self.__healingpotions) == 0:
            print("You are all out of healing potions.")
        else:
            potion = self.__healingpotions.pop(0)
            # Does not allow hitpoints to go over 100
            # Remove if going over 100 is allowed
            # self.__hitpoints += potion.points
            totalhitpoints = self.__hitpoints + potion.points
            if totalhitpoints <= 100:
                self.__hitpoints = totalhitpoints
            else:
                self.__hitpoints = 100
            print(f"Took healing potion. Hit points restored to {self.__hitpoints}")

    def addvisionpotion(self):
        self.__visionpotions += 1
        print("Added vision potion to inventory.")

    def take_vision_potion(self):
        if self.__visionpotioncount == 0:
            print("You are all out of vision potions.")
        else:
            self.__visionpotions -= 1
            # I don't think the maze code will be called from within the player class

    def takedamage(self, pit):
        self.__hitpoints -= pit.damage
        print(f"Took damage. Lost {pit.damage} points.")

    def __str__(self):
        return (
            f"\nName: {self.__name}\n"
            f"Hit Points: {self.__hitpoints}\n"
            f"Total Healing Potions: {len(self.__healingpotions)}\n"
            f"Total Vision Potions: {self.__visionpotioncount}\n"
            f"Pillars Keys Found: {', '.join(p.name for p in self.__pillarsfound)}\n"
        )
