from dungeon_object import DungeonObject
import time
from art import Art


class Pillar(DungeonObject):
    """
    Inherit from abstract base class DungeonObject.
    Create 4 pillars of OOP, specifically keys for player to pick up to exit dungeon.
    """
    ref = {'A': 'Pillar of Abstraction', 'E': 'Pillar of Encapsulation',
           'I': 'Pillar of Inheritance', 'P': 'Pillar of Polymorphism'}

    def __init__(self, letter):
        """
        Create pillar key using class varible ref
        :param letter: letter of pillar
        :type letter: str
        """
        super().set_name(Pillar.ref[letter])
        super().set_letter(letter)

    def function(self):
        """
        Display pillar art and collect key
        """
        Art.pillar(self.letter)
        time.sleep(2)
        print(f'  You have collected {self.name} key!')