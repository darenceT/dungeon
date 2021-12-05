from dungeon_object import DungeonObject
import timer


class Potion(DungeonObject):

    def __init__(self):
        self.__name = ''

    def timer(self):
        print("\n*** Using potion in ...", end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='')
        time.sleep(1)

    # print('\nOnly 8 rooms revealed, not bottom right which is covered by :::\n')

    def function(self):
        pass
        "use potion"

    def char(self):
        return self.__name[0]

    def __str__(self):
        return self.__name