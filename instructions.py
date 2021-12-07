

class Instructions:

    def __init__(self):
        self.__player_name = ""
        self.__difficulty = 0
        self.menu()

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Only string accepted for name')
        self.__player_name = name

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, num):
        if 1 >= num >= 3:
            raise ValueError('Secondary line of error caught, number is not between 1 and 3')
        self.__difficulty = num

    @staticmethod
    def instructions():
        print("Add Instructions Here")

    def menu(self):
        option = -1
        while option != 0:
            print("[1] Start New Game\n"
                  "[2] Game Instructions\n"
                  "[0] Exit Game")
            option = int(input("Enter the option you would like to choose: "))
            if option == 1:
                self.make_player_name()
                self.pick_difficulty()
                return
            elif option == 2:
                self.instructions()
                print()
                continue
            else:
                print("Invalid Option! Please choose again.\n")
                continue

        print("Thank you for playing!")

    def make_player_name(self):
        name = input("Enter a character name: ").capitalize()
        while name.isalpha() is False:
            name = input("Please input an appropriate name: ")
        self.player_name = name

    def pick_difficulty(self):
        difficulty = input("Enter a game difficulty level between 1 and 3: ")
        while difficulty.isnumeric() is False or int(difficulty) < 1 or int(difficulty) > 3:
            difficulty = input("Please only enter a game difficulty level between 1 and 3: ")
        self.difficulty = int(difficulty)


# below is for testing, delete before submission
if __name__ == '__main__':
    m = Instructions()
    print(m.difficulty)
    print(m.player_name)
