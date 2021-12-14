from clear_screen import ClearScreen


class SoundOption:
    """
    Sound menu for changes to music and sounds, turn off, on or change volume.
    Accessed at intro or in-game
    """
    @staticmethod
    def change(sound, in_game=False):
        """
        Menu of sound changes
        :param sound: passing instance of SoundFx to know if sound is on (is_running attribute)
        :type sound: SoundFx
        :param in_game: notify if accessed in intro or in-game
        :type in_game: bool
        """
        selection = None
        choices = ['1', '2', '3', '4', '0']
        change_switch = 'off'
        while selection not in choices:
            ClearScreen()
            if not sound.is_running:
                change_switch = 'on'
            spaces = "                     "
            print(f'\n\n\n\n{spaces}DUNGEON CRAWLER\n\n\n'
                  f'{spaces}* Sound Options *\n\n\n'
                  f'{spaces}[1] Turn sound {change_switch}\n')
            if sound.is_running:
                print(f'{spaces}[2] Low volume\n'
                    f'{spaces}[3] Normal volume\n'
                    f'{spaces}[4] High volume\n')
            print(f'{spaces}[0] Return\n\n')
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
                sound.low_volume()
                selection = None
            elif selection == "3":
                sound.normal_volume()
                selection = None
            elif selection == "4":
                sound.high_volume()
                selection = None
            elif selection == "0":
                return