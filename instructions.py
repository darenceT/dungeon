from os import system, name


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
        if 1 >= num >= 3:
            raise ValueError('Secondary line of error caught, number is not between 1 and 3')
        self.__difficulty = num

    @staticmethod
    def clear():
        """
        Function clears screen after each input for improve game play.
        Credit to https://www.geeksforgeeks.org/clear-screen-python/
        """
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    @staticmethod
    def instructions():
        Instructions.clear()
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
        option = -1
        while option != 0:
            self.clear()
            print("\n\n\n\n                     DUNGEON CRAWLER\n\n\n"
                  "                     [1] Start New Game\n"
                  "                     [2] Game Instructions\n"
                  "                     [0] Exit Game\n\n")
            option = int(input("                    Enter your option: "))
            if option == 1:
                self.make_player_name()
                self.pick_difficulty()
                return
            elif option == 2:
                self.instructions()
                print()
                continue
            else:
                print("  Invalid Option! Please choose again.\n")
                continue

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
