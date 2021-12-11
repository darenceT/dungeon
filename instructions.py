from clear_screen import ClearScreen
from sound_fx import SoundFx


class Instructions:

    def __init__(self):
        self.__player_name = ""
        self.__difficulty = 0
        self.menu()

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Only string accepted for name')
        self.__player_name = name

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, num):
        if 1 > num > 3:
            raise ValueError('Secondary line of error caught, number is not between 1 and 3')
        self.__difficulty = num

    def __pick_option(self):
        while True:
            pick = input("                    Enter your pick: ").strip()
            if not pick.isnumeric():
                print("Only integers 0 or greater accepted")
                continue
            if int(pick) > 3:
                print('Only integers between 0 to 3 accepted')
                continue
            return int(pick)

    @staticmethod
    def instructions():
        ClearScreen()
        print("\n               Welcome to the Dungeon Crawler!\n\n"
              "  You are tasked with guiding the player character through a\n"
              "  dangerous maze. The player can move North, South, East or West\n"
              "  by using the keys 'n', 's', 'e', and 'w' respectively. Make it\n "
              " through the maze alive while finding the four pillars of Object\n"
              "  Oriented Programming: Encapsulation, Inheritance, Abstraction\n"
              "  and Polymorphism. However, be careful of pits that will cause\n"
              "  you to lose health. Losing all health will cause you to lose the\n"
              "  game. There are other items that can be found, such as health\n"
              "  potions and vision portions. Health potions restore lost HP and\n"
              "  vision potions reveal 8 rounds around you. You only Win the game\n"
              "  when you reach the end of the maze AFTER collecting all four\n"
              "  pillars. Good Luck Explorer!")
        if input('\n               Press Enter to return to menu'):
            return

    def menu(self):
        SoundFx.intro()
        pick = -1
        while pick != 0:
            ClearScreen()
            print("\n\n\n\n                     DUNGEON CRAWLER\n\n\n"
                  "                     [1] Start New Game\n"
                  "                     [2] Game Instructions\n"
                  "                     [0] Exit Game\n\n")
            pick = self.__pick_option()
            if pick == 1:
                self.make_player_name()
                self.pick_difficulty()
                return
            elif pick == 2:
                self.instructions()
                print()
                continue
            elif pick == 0:
                break
            # add menu for music picks

        print("\n  Thank you for playing!")
        exit()

    def make_player_name(self):
        name = input("\n  Enter a character name: ").capitalize().strip()
        while name.isalpha() is False:
            name = input("  Please input an appropriate name: ")
        self.player_name = name

    def pick_difficulty(self):
        difficulty = input("  Enter a game difficulty level between 1 and 3: ").strip()
        while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
            difficulty = input("  Please only enter a game difficulty level between 1 and 3: ")
        self.difficulty = int(difficulty)


# below is for testing, delete before submission
if __name__ == '__main__':
    m = Instructions()
    print(m.difficulty)
    print(m.player_name)