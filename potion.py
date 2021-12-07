from dungeon_object import DungeonObject
import time


class Potion(DungeonObject):

    @staticmethod
    def timer():
        print("\n*** Using potion in ...", end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='')
        time.sleep(1)

    # print('\nOnly 8 rooms revealed, not bottom right which is covered by :::\n')
    # @abstractmethod
    def function(self):
        pass
        "use potion"
