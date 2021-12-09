from dungeon_object import DungeonObject
from pillar import Pillar
import time

class ExitDoor(DungeonObject):
    def __init__(self):
        super().set_name('Exit')
        super().set_letter('O')

    @staticmethod
    def function(backpack):
        key_count = sum(isinstance(x, Pillar) for x in backpack)
        if key_count == 4:
            print('  You put in all 4 pillar keys and you hear some gears turning...')
            time.sleep(2)
            print('  INSERT ART HERE\n'
                  '  You found your escape!')
            exit()
        else:
            print('  You see some light...it\'s a door! There are 4 strange-key holes...\n'
                  '  You only have', key_count, 'keys...')

if __name__ == '__main__':          ############## DELETE #################
    p = ExitDoor()
    print(p.name)
    print(p.letter)