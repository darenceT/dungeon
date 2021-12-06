from dungeon_object import DungeonObject
import time


class Pillar(DungeonObject):
    ref = {'A': 'Pillar of Abstraction', 'E': 'Pillar of Encapsulation',
           'I': 'Pillar of Inheritance', 'P': 'Pillar of Polymorphism'}

    def __init__(self, letter):
        super().set_name(Pillar.ref[letter])
        super().set_letter(letter)

    def function(self):
        print('INSERT AMAZING PILLAR OF ABSTRACTION ART \n'
              'You see a shiny button and you cannot help yourself but to push it...')
        time.sleep(2)
        print(f'You have collected {Pillar.ref[letter]} key!')


if __name__ == '__main__':          ############## DELETE #################
    p = Pillar('E')
    print(p.name)
    print(p.letter)