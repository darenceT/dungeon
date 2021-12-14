from instructions import Instructions
from clear_screen import ClearScreen
from sound_fx import SoundFx
import pygame


class PauseGame:

    @staticmethod
    def menu(map, sound):
        SoundFx.pause_menu()
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
                  f"{spaces} [3] Sound options\n"       # in progress
                  f"{spaces} [4] Restart Game\n"
                  f"{spaces} [5] *Cheat* Remove display later but will still work\n"
                  f"{spaces} [0] Exit Game\n")
 
            if selection is not None and selection not in options:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                SoundFx.pause_menu(resume=True)
                return False
            elif selection == "2":
                Instructions.instructions()
                selection = None
                continue
            elif selection == "3":
                PauseGame.sound_options(sound)
            elif selection == "4":
                return True
            elif selection == "5":
                ClearScreen()
                print(f'\n\n{spaces}You found the hidden map!\n\n{map}')
                input('\n       Press Enter to return to menu')
                selection = None
                continue
            elif selection == "0":
                print(f"\n{spaces}Thank you for playing!\n\n")
                pygame.quit()
                exit()
    
    @staticmethod
    def sound_options(sound):
        selection = None
        choices = ['1', '2', '3', '0']
        all_sound_on = True
        change_switch = 'off'
        while selection not in choices:
            ClearScreen()
            if not all_sound_on:
                change_switch = 'on'
            spaces = "                     "
            print(f'\n\n\n\n{spaces}DUNGEON CRAWLER\n\n\n'
                  f'{spaces}       * Sound Options *\n\n\n'
                  f'{spaces}[1] Turn music {change_switch}\n'
                  f'{spaces}[2] Game Instructions\n'
                  f'{spaces}[3] Sound options\n'
                  f'{spaces}[0] Return\n\n')
            if selection is not None and selection not in choices:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                if all_sound_on:
                    pygame.mixer.quit()
                    all_sound_on = False
                    selection = None
                else:
                    pygame.init()
                    mixer.music.load(Path('sound/Subterranean Howl - ELPHNT_short.mp3'))
                    mixer.music.set_volume(0.6)
                    mixer.music.play(-1)
                    all_sound_on = True
                    change_switch = 'off'
                    selection = None
            elif selection == "2":
                selection = None
            elif selection == "0":
                return