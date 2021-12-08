#from character_creation import CharacterCreation



class Instructions:

    def __init__(self):
        self.__player_name = ""
        self.__difficulty = 0
        self.menu()

    @property
    def player_name(self):
        return self.__player_name

    @property
    def difficulty(self):
        return self.__difficulty

    def instructions(self):
        print("\nWelcome to the dungeon crawler!"
              "\nYou are tasked with guiding the player character through a dangerous maze."
              "\nThe player can move North, South, East or West by using the keys 'n', 's', 'e', and 'w' respectively."
              "\nDepending on where you are in the randomly generated maze, you will be informed which directions it is possible to move in."
              "\nThe goal is for the main character to make it through the maze alive while finding the four pillars of Object Oriented Programming: Encapsulation, Inheritance, Abstraction and Polymorphism."
              "\nHowever, you must be careful, ase many of the chambers in the maze have traps and pits that will cause you to lose HP(Health Points)."
              "\nLosing all HP will cause you to lose the game"
              "\nThere are other items that can be found and used in the dungeon, such as health potions and vision portions."
              "\nHealth potions restore lost HP and vision potions show small portions of the map that have not yet been explored."
              "\nYou only win the game when you reach the end of the maze AFTER collecting all four pillars."
              "\nGood Luck Explorer!")

    def menu(self):
        print("[1] Start New Game\n[2] Game Instructions\n[0] Exit Game")

        option = int(input("Enter the option you would like to choose: "))
        while option != 0:
            if option == 1:
                self.player_name()
                self.difficulty()
            elif option == 2:
                self.instructions()
                print()
                self.menu()
                option = int(input("Enter the option you would like to choose: "))
            else:
                print("Invalid Option! Please choose again.\n")
                self.menu()
                option = int(input("Enter the option you would like to choose: "))

        print("Thank you for playing!")

    def player_name(self):
        name = input("Enter a character name: ")
        while name.isalpha() is False:
            name = input("Please input an appropriate name: ")
        self.__player_name = name

    def difficulty(self):
        difficulty = input("Enter a game difficulty level between 1 and 3: ")
        while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
            difficulty = input("Please only enter a game difficulty level between 1 and 3: ")
        self.__difficulty = difficulty

if __name__ == '__main__':
    m = Instructions()
