# Manuel Duarte
from random import randint


class Player:
    def __init__(self, name="Player 1", sound=any):
        self.__name = name
        self.__sound = sound
        self.__hitpoints = randint(60, 80)
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
                self.__fall_pit(obj)
            elif obj.letter in ['H', 'V']:
                if obj.letter == 'H':
                    obj.inspect()
                self.__backpack.append(obj)
                print(f'  {self.name} added {obj} to backpack!')
            elif obj not in self.__backpack:
                if obj.letter in ['A', 'E', 'I', 'P']:
                    self.__sound.pillar()
                obj.function()
                self.__backpack.append(obj)

    def potion_menu(self, map=None, loc=None):
        selection = None
        options = ['r']
        if self.health_potions != 0:
            options.append('h')
        if self.vision_potions != 0:
            options.append('v')
        while selection not in options:
            print(f'\n  You have {self.health_potions} health potion(s),'
                  f'and {self.vision_potions} vision potion(s):')
            if self.health_potions != 0:
                print(f'\t [h] Use a health potion')
            if self.vision_potions != 0:
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
        if self.health_potions == 0:
            raise Exception("You do not any health potion to use")

        for o in self.__backpack:
            if o.letter == "H":
                self.__backpack.remove(o)
                print(f'\n  You used a {o}, {o.health_points} health replenished!')
                self.__hitpoints += o.health_points
                break

        if self.__hitpoints > 100:
            self.__hitpoints = 100
        print(f"  {self.__name}'s health is now {self.__hitpoints} health points")

    def __use_vision_potion(self, map, loc):
        if self.vision_potions == 0:
            raise Exception("You do not have any vision potion to use")

        for o in self.__backpack:
            if o.letter == "V":
                o.function(map, loc)
                self.__backpack.remove(o)
                break

    def __fall_pit(self, pit):
        damage = pit.function()
        if damage > 0:
            self.__sound.pit()
            self.__hitpoints -= damage

    def __str__(self):
        pillars = 0
        for obj in self.__backpack:
            if obj.letter in ['A', 'E', 'I', 'P']:
                pillars += 1
        return (
            f"\n  Name: {self.__name}\n"
            f"  Hit Points: {self.__hitpoints}\n"
            f"  Total Healing Potions: {self.health_potions}\n"
            f"  Total Vision Potions: {self.vision_potions}\n"
            f"  Pillars Keys Found: {pillars}\n")