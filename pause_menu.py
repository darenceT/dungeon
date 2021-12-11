from instructions import Instructions
from clear_screen import ClearScreen
from sound_fx import SoundFx


class PauseMenu:

    def __init__(self, map):
        self.__map = map
        self.pause_menu(self.__map)

    def pause_menu(self, map):
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
            option = int(input("           Enter your option: ").strip())
            if option == 1:
                SoundFx.pause_menu(resume=True)
                return
            elif option == 2:
                Instructions.instructions()
                continue
            elif option == 3:
                ClearScreen()
                print(map)
                if input('\n          Press Enter to return to menu'):
                    return
                continue
            elif option !=0:
                print("Invalid Option! Please choose again.\n")
                continue

        print("\nThank you for playing!\n")
        exit()