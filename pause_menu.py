import pygame
from pygame import mixer
#from dungeon_adventure import DungeonAdventure

pygame.init()


class PauseMenu:

    def __init__(self):
        self.pause_menu()

    @staticmethod
    def game_instructions():
        print("\n               Welcome to the dungeon crawler!\n"
              "You are tasked with guiding the player character through\n"
              "a dangerous maze. The player can move North, South, East\n"
              "or West by using the keys 'n', 's', 'e', and 'w' respectively.\n"
              "Depending on where you are in the randomly generated maze,\n"
              "you will be informed which directions it is possible to move\n"
              "in. The goal is for the main character to make it through the\n"
              "maze alive while finding the four pillars of Object Oriented\n"
              "Programming: Encapsulation, Inheritance, Abstraction and\n"
              "Polymorphism. However, you must be careful, ase many of the\n"
              "chambers in the maze have traps and pits that will cause you\n"
              "to lose HP(Health Points). Losing all HP will cause you to\n"
              "lose the game. There are other items that can be found and\n"
              "used in the dungeon, such as health potions and vision portions.\n"
              "Health potions restore lost HP and vision potions show small\n"
              "portions of the map that have not yet been explored. You only\n"
              "win the game when you reach the end of the maze AFTER collecting\n"
              "all four pillars. Good Luck Explorer!")

    def pause_menu(self):
        mixer.music.load('Mind And Eye Journey - Emily A. Sprague.mp3')
        mixer.music.play(-1)
        option = -1
        while option != 0:
            print("[1] Resume Game\n"
                  "[2] Game Instructions\n"
                  "[0] Exit Game")
            option = int(input("Enter the option you would like to choose: "))
            if option == 1:
                mixer.music.load('Subterranean Howl - ELPHNT.mp3')
                mixer.music.play(-1)
                return
            elif option == 2:
                self.game_instructions()
                print()
                continue
            elif option == 3:
                #self.__map = DungeonAdventure(self.__map)
                #print(self.__map)
                continue
            else:
                print("Invalid Option! Please choose again.\n")
                continue

        print("Thank you for playing!")
        exit()
