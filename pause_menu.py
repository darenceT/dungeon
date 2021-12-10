from instructions import Instructions
from clear_screen import ClearScreen
from sound_fx import SoundFx


class PauseMenu:

    def __init__(self, map):
        self.__map = map
        self.pause_menu(self.__map)

    def pause_menu(self, map):
        # mixer.music.load('sound\Mind And Eye Journey - Emily A. Sprague.mp3')
        # mixer.music.play(-1)
        SoundFx.pause_menu()
        option = -1
        while option != 0:
            ClearScreen()
            print("\n\n                     DUNGEON CRAWLER\n\n\n"
                  "                     [1] Resume Game\n"
                  "                     [2] Game Instructions\n"
                  "                     [3] **** Cheat ****\n"
                  "                     [0] Exit Game\n")
                  # restart game
                  # sound options
            option = int(input("           Enter your option: "))
            if option == 1:
                SoundFx.pause_menu(resume=True)
                return
            elif option == 2:
                Instructions.instructions()
                continue
            elif option == 3:
                ClearScreen()
                print(map)
                if input('\n               Press Enter to return to menu'):
                    return
                continue
            else:
                print("Invalid Option! Please choose again.\n")
                continue

        print("Thank you for playing!")
        exit()






    # @staticmethod
    # def game_instructions():
    #     ClearScreen()
    #     print("\n               Welcome to the Dungeon Crawler!\n\n"
    #           "  You are tasked with guiding the player character through a\n"
    #           "  dangerous maze. The player can move North, South, East or West\n"
    #           "  by using the keys 'n', 's', 'e', and 'w' respectively. Make it\n "
    #           " through the maze alive while finding the four pillars of Object\n"
    #           "  Oriented Programming: Encapsulation, Inheritance, Abstraction\n"
    #           "  and Polymorphism. However, be careful of pits that will cause\n"
    #           "  you to lose health. Losing all health will cause you to lose the\n"
    #           "  game. There are other items that can be found, such as health\n"
    #           "  potions and vision portions. Health potions restore lost HP and\n"
    #           "  vision potions reveal 8 rounds around you. You only Win the game\n"
    #           "  when you reach the end of the maze AFTER collecting all four\n"
    #           "  pillars. Good Luck Explorer!")
    #     if input('\n               Press Enter to return to menu'):
    #         return