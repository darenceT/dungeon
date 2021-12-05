# from adventure import Adventure


def player_input():
    name = input("Enter a character name: ")
    while name.isalpha() is False:
        name = input("Please input an appropriate name: ")

    difficulty = input("Enter a game difficulty level between 1 and 3: ")
    while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
        difficulty = input("Please only enter a game difficulty level between 1 and 3: ")


class CharacterCreation:

    def __init__(self, name, difficulty, ):
        print("Welcome! Please provide a character name and difficulty level when prompted.")
        self.name = name
        self.difficulty = difficulty

    player_input()
