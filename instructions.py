from clear_screen import ClearScreen
from sound_fx import SoundFx
from sound_option import SoundOption
from art import Art

class Instructions:
    """
    This runs the main menu, through which the user can access the game, read instructions for the game, adjust sound
    options or exit the game.
    """
    def __init__(self):
        self.__sound = SoundFx()
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

    @property
    def sound(self):
        return self.__sound

    @staticmethod
    def instructions():
        """
        This introduces how the game works.
        """
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
        input('\n               Press Enter to return to menu')
        return
    
    def menu(self):
        """
        This allows the user to navigate the main menu through the selection of specified options.
        Credit https://www.youtube.com/watch?v=63nw00JqHo0
        """
        self.__sound.intro()
        Art.intro()
        selection = None
        spaces = "                   "
        choices = ["1", "2", "3", "0"]
        while selection not in choices:
            ClearScreen()
            print("\n\n\n\n"
                  f"{spaces} DUNGEON CRAWLER\n\n\n"
                  f"{spaces} [1] Start New Game\n"
                  f"{spaces} [2] Game Instructions\n"
                  f"{spaces} [3] Sound option\n"
                  f"{spaces} [0] Exit Game\n\n")
            if selection is not None and selection not in choices:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                self.make_player_name()
                self.pick_difficulty()
                return
            elif selection == "2":
                self.instructions()
                selection = None
            elif selection == "3":
                SoundOption.change(self.__sound)
                selection = None
            elif selection == "0":
                print(f"\n{spaces}Thank you for playing!\n\n")
                exit()
    
    def make_player_name(self):
        """
        User can only enter letter and space containing names
        Credit https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python 
        """
        while True:
            name = input("\n  Enter your player name: ").capitalize().strip()
            if all(x.isalpha() or x.isspace() for x in name):
                break
            else:
                print("  Please enter an appropriate name.")
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