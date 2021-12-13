from instructions import Instructions
from dungeon_adventure import DungeonAdventure


class Main:
    def __init__(self):
        """
        Restart code credit https://www.dreamincode.net/forums/topic/96312-restarting-a-program/
        """
        DungeonAdventure(Instructions())
        while True:
            choice = input('\n    Play again? (yes/no):').lower().strip()
            if choice in ['y', 'yes']:
                DungeonAdventure(Instructions())
            elif choice in ['n', 'no'] :
                print("\n    Thanks for playing!\n")
                exit()
            else:
                print('\n    Enter yes or no only')
                continue


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print('\n\n                   Thank you for playing!\n\n')
        exit(0)