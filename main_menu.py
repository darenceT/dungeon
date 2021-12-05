from instructions import instructions
from instructions import CharacterCreation


def menu():
    print("[1] Start New Game")
    print("[2] Game Instructions")
    print("[0] Exit Game")


menu()
option = int(input("Enter the option you would like to choose: "))
while option != 0:
    if option == 1:
#        obj = instructions.CharacterCreation

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
