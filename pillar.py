from dungeon_object import DungeonObject
import time
from art import Art

class Pillar(DungeonObject):
    ref = {'A': 'Pillar of Abstraction', 'E': 'Pillar of Encapsulation',
           'I': 'Pillar of Inheritance', 'P': 'Pillar of Polymorphism'}

    def __init__(self, letter):
        super().set_name(Pillar.ref[letter])
        super().set_letter(letter)

    def function(self):
        Art.pillar(self.letter)
        time.sleep(2)
        print(f'  You have collected {self.name} key!')


if __name__ == '__main__':          ############## DELETE #################
    p = Pillar('E')
    # print(isinstance(p, Lack))
    print(p.letter)