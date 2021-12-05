from abc import ABC, abstractmethod
import timer


class Potion(ABC):

    def timer(self):
        print("\n*** Using vision potion in ...", end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='')
        time.sleep(1)
        print('\nOnly 8 rooms revealed, not bottom right which is covered by :::\n')