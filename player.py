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
        for obj in objects:
            self.__bag.append(obj)
            print('Player picked up', obj)

    def addhealingpotion(self, potion):
        self.__healingpotions.append(potion)
        print("Added healing potion to inventory.")

    def takehealingpotion(self):
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

    def takevisionpotion(self):
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
            f"Name: {self.__name}\n"
            f"Hit Points: {self.__hitpoints}\n"
            f"Total Healing Potions: {len(self.__healingpotions)}\n"
            f"Total Vision Potions: {self.__visionpotions}\n"
            f"List of Pillars Pieces Found: {', '.join(p for p in self.__pillarsfound)}"
        )
