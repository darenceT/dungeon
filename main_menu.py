#from character_creation import CharacterCreation


def menu():
    print("[1] Start New Game\n[2] Game Instructions\n[0] Exit Game")


def instructions():
    print("Add Instructions Here")


class MainMenu:
    menu()
    option = int(input("Enter the option you would like to choose: "))
    while option != 0:
        if option == 1:
            pass
        elif option == 2:
            instructions()
            print()
            menu()
            option = int(input("Enter the option you would like to choose: "))
        else:
            print("Invalid Option! Please choose again.")

            print()
            menu()
            option = int(input("Enter the option you would like to choose: "))

    print("Thank you for playing!")


if __name__ == '__main__':
    m = MainMenu()
