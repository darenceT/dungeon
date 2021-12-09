from dungeon_object import DungeonObject
import time


class Potion(DungeonObject):

    @staticmethod
    def timer(self):
        print("\n*** Using potion in ...", end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='')
        time.sleep(1)

    @staticmethod
    def function():
        pass
        "use potion"
