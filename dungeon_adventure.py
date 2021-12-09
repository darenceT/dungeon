from build_dungeon import BuildDungeon
from player import Player
from vision_potion import VisionPotion              ############# delete #################
from instructions import Instructions


class DungeonAdventure:

    def __init__(self, input):
        self.__map = BuildDungeon(input.difficulty)
        print(self.__map)                   ################### delete
        self.__room_index = self.__map.room_index
        self.__player = Player(input.player_name)
        self.__entrance_loc = self.__map.entrance_loc
        self.__exit_loc = self.__map.exit_loc
        self.__current_loc(self.__entrance_loc)

    def __current_loc(self, location):
        Instructions.clear()
        print('  \n==============================================================\n\n    ',
              self.__player.name, end=' ')
        self.__map.room_index[location].enter_room()

        room_objects = self.__room_index[location].touch_objects()
        self.__player.interact_objects(room_objects)

        # if user reached end
        # if location == self.__exit_loc:
        # VisionPotion.function(self.__map, location)               #TURN ON VISION POTION HERE
        self.__move_options(location)

    def __move_options(self, location):
        x, y = location
        open_path = []
        if self.__map.hor[y][x] == "+  ":
            open_path.append('North')
        if self.__map.hor[y+1][x] == "+  ":
            open_path.append('South')
        if self.__map.ver[y][x][0] == " ":
            open_path.append('West')
        if self.__map.ver[y][x+1][0] == " ":
            open_path.append('East')

        while True:
            print('\n  Your options for moving to next room:', ', '.join(open_path))
            choice = input('  Input letter for your next action "n, s, e, w" for next room,\n'
                           '  "p" for potion, "i" for status: ').lower().strip()
            menu = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West',
                    'i': 'Player Status', 'p': 'Potion Menu'}
            next_room = {'n': (x, y - 1), 's': (x, y + 1), 'e': (x + 1, y), 'w': (x - 1, y)}
            if choice not in menu.keys():
                print('Invalid input!')
            else:
                if choice == 'i':
                    print(self.__player)
                elif choice == 'p':
                    self.__player.potion_menu()
                elif menu[choice] not in open_path:
                    print('  That path is not possible!')
                else:
                    self.__current_loc((next_room[choice][0], next_room[choice][1]))
                    break

    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    # def vision(self, loc):                     ############# move to player class? #################
        # VisionPotion.function(self.__map, loc)

"""

DungeonAdventure
    • Contains the main logic for playing the game
    • Introduces the game describing what the game is about and how to play
    • Creates a Dungeon Object and a Adventurer Object
    • Obtains the name of the adventurer from the user
    • Does the following repetitively:
        o Prints the current room (this is based on the Adventurer's current location)
        o Determines the Adventurer's options (Move, Use a Potion)
        o Continues this process until the Adventurer wins or dies
        o NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify
        what the menu option is in your documentation for the DungeonAdventure class
    • At the conclusion of the game, display the entire Dungeon
"""


if __name__ == '__main__':
    class Obj:
        pass
    b = Obj()

    b.difficulty = int(input('Select difficulty:\n1. Easy\n2. Normal\n3. Hard\nType 1, 2 or 3: '))
    # except TypeError:
    b.player_name = 'jack'
    a = DungeonAdventure(b)


