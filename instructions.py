#from adventure import Adventure


def instructions():
    print("Add Instructions Here")


class CharacterCreation:

    def __init__(self):
        print("Welcome! Please provide a character name and difficulty level when prompted.")

#    def character_name(self):


    def game_difficulty(self):
        difficulty = input("Enter a game difficulty level between 1 and 3: ")
        while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
            difficulty = input("Please only enter a game difficulty level between 1 and 3: ")

        return int(difficulty)
