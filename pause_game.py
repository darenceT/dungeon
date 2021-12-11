# from main import Main
from instructions import Instructions
from clear_screen import ClearScreen
from sound_fx import SoundFx


class PauseGame:

    # def __init__(self, map):
    #     self.__map = map
    #     self.pause_menu(self.__map)

    @staticmethod
    def menu(map):
        SoundFx.pause_menu()
        selection = None
        spaces = "                   "
        while selection not in ["1", "2", "3", "4", "5", "0"]:
            ClearScreen()
            print("\n\n\n" 
                  f"{spaces} DUNGEON CRAWLER\n\n\n"
                  f"{spaces}  * GAME PAUSED *\n\n\n"
                  f"{spaces} [1] Resume Game\n"
                  f"{spaces} [2] Game Instructions\n"
                  f"{spaces} [3] Sound options\n"       # in progress
                  f"{spaces} [4] *Cheat* Remove display later but will still work\n"
                  f"{spaces} [5] Restart Game\n"
                  f"{spaces} [0] Exit Game\n")
 
            if selection is not None and selection not in ['1', '2', '3', '4', '5', '0']:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                SoundFx.pause_menu(resume=True)
                return False
            elif selection == "2":
                Instructions.instructions()
                selection = None
                continue
            elif selection == "4":
                ClearScreen()
                print(f'\n\n{spaces}You found the hidden map!\n\n{map}')
                input('\n       Press Enter to return to menu')
                selection = None
                continue
            elif selection == "5":
                return True
            elif selection == "0":
                print(f"\n{spaces}Thank you for playing!\n\n")
                exit()