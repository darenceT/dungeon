

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
    def instructions():
        print("\n               Welcome to the dungeon crawler!\n"
              "You are tasked with guiding the player character through\n"
              "a dangerous maze. The player can move North, South, East\n"
              "or West by using the keys 'n', 's', 'e', and 'w' respectively.\n"
              "Depending on where you are in the randomly generated maze,\n"
              "you will be informed which directions it is possible to move\n"
              "in. The goal is for the main character to make it through the\n"
              "maze alive while finding the four pillars of Object Oriented\n"
              "Programming: Encapsulation, Inheritance, Abstraction and\n"
              "Polymorphism. However, you must be careful, ase many of the\n"
              "chambers in the maze have traps and pits that will cause you\n"
              "to lose HP(Health Points). Losing all HP will cause you to\n"
              "lose the game. There are other items that can be found and\n"
              "used in the dungeon, such as health potions and vision portions.\n"
              "Health potions restore lost HP and vision potions show small\n"
              "portions of the map that have not yet been explored. You only\n"
              "win the game when you reach the end of the maze AFTER collecting\n"
              "all four pillars. Good Luck Explorer!")

    def menu(self):
        option = -1
        while option != 0:
            print("[1] Start New Game\n"
                  "[2] Game Instructions\n"
                  "[0] Exit Game")
            option = int(input("Enter the option you would like to choose: "))
            if option == 1:
                self.make_player_name()
                self.pick_difficulty()
                return
            elif option == 2:
                self.instructions()
                print()
                continue
            else:
                print("Invalid Option! Please choose again.\n")
                continue

        print("Thank you for playing!")
        exit()

    def make_player_name(self):
        name = input("Enter a character name: ").capitalize()
        while name.isalpha() is False:
            name = input("Please input an appropriate name: ")
        self.player_name = name

    def pick_difficulty(self):
        difficulty = input("Enter a game difficulty level between 1 and 3: ")
        while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
            difficulty = input("Please only enter a game difficulty level between 1 and 3: ")
        self.difficulty = int(difficulty)


# below is for testing, delete before submission
if __name__ == '__main__':
    m = Instructions()
    print(m.difficulty)
    print(m.player_name)
