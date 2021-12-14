from clear_screen import ClearScreen


class SoundOption:
    
    @staticmethod
    def change(sound, in_game=False):
        selection = None
        choices = ['1', '2', '3', '0']
        change_switch = 'off'
        while selection not in choices:
            ClearScreen()
            if not sound.is_running:
                change_switch = 'on'
            spaces = "                     "
            print(f'\n\n\n\n{spaces}DUNGEON CRAWLER\n\n\n'
                  f'{spaces}       * Sound Options *\n\n\n'
                  f'{spaces}[1] Turn sound {change_switch}\n'
                  f'{spaces}[2] in progress \n'
                  f'{spaces}[3] in progress\n'
                  f'{spaces}[0] Return\n\n')
            if selection is not None and selection not in choices:
                print(f"{spaces}Invalid selection! Please choose again.\n")
            selection = input(f"{spaces}Enter your selection: ").strip()
            if selection == "1":
                if sound.is_running:
                    sound.turn_off()
                    selection = None
                else:
                    sound.turn_on(in_game)
                    change_switch = 'off'
                    selection = None
            elif selection == "2":
                selection = None
            elif selection == "0":
                return