from instructions import Instructions
from clear_screen import ClearScreen
from sound_option import SoundOption


class PauseGame:
    """
    This runs the pause menu, which can only be accessed in game. Through this, the user can access the game, read
    instructions for the game, view the entire map(only for the purpose of testing and grading), adjust sound options,
    restart the game, or exit the game.
    """
    @staticmethod
    def menu(map, sound):
        """
        This allows the user to navigate the main menu through the selection of specified options.
        Credit https://www.youtube.com/watch?v=63nw00JqHo0
        """
        sound.pause_menu()
        selection = None
        spaces = "                   "
        options = ["1", "2", "3", "4", "5", "0"]
        while selection not in options:
            ClearScreen()
            print("\n\n\n" 
                  f"{spaces} DUNGEON CRAWLER\n\n\n"
                  f"{spaces}  * GAME PAUSED *\n\n\n"
                  f"{spaces} [1] Resume Game\n"
                  f"{spaces} [2] Game Instructions\n"
                  f"{spaces} [3] Sound options\n"   
                  f"{spaces} [4] Restart Game\n"    
                # f"{spaces} [5] *Cheat* Reveals hidden room. This message is hidden in game\n"
                  f"{spaces} [0] Exit Game\n")
 
            if selection is not None and selection not in options:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                sound.pause_menu(resume=True)
                return False
            elif selection == "2":
                Instructions.instructions()
                selection = None
            elif selection == "3":
                sound.pause_menu(resume=True)
                SoundOption.change(sound, in_game=True)
                selection = None
            elif selection == "4":
                return True
            elif selection == "5":
                ClearScreen()
                print(f'\n\n{spaces}You found the hidden map!\n\n{map}')
                input('\n       Press Enter to return to menu')
                selection = None
            elif selection == "0":
                print(f"\n{spaces}Thank you for playing!\n\n")
                exit()