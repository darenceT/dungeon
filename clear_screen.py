from os import system, name


class ClearScreen():
        """
        Function clears screen after each input for improve game play.
        Credit to https://www.geeksforgeeks.org/clear-screen-python/
        """
        def __init__(self):
            """
            Clear screen by checking operating system
            """
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')