from build_dungeon import BuildDungeon
from player import Player
from vision_potion import VisionPotion              ############# delete #################


class Adventure:

    def __init__(self, user_input):
        self.__map = BuildDungeon(user_input.difficulty)
        print(self.__map)                   ################### delete
        self.__player = Player(user_input.player_name)
        self.__entrance_loc = self.__map.entrance_loc
        self.__exit_loc = self.__map.exit_loc
        self.__current_loc(self.__entrance_loc)

    def __current_loc(self, location):
        self.__map.room_index[location].enter_room()
        print(self.__map.room_index[location])
        print('Welcome', self.__player.name)
        items_found = self.__map.room_index[location].obtain_items()
        self.__player.pick_up(items_found)

        # for obj in items_found:
        #     obj.function()

        # if user reached end
        print(location, 'and', self.__exit_loc)
        if location == self.__exit_loc:
            print('You have reached the exit!')
            # if player.pillars:          True for collected all 4
            #     print('you win! You have gained adequate knowledge for quarter 2 and still much to learn...')
            # else:
            #     print('Keep looking for those pillars of success...')
            #     self.move_options(x, y)

        # self.vision(x, y)           ################################ DELETE
        self.__move_options(location)

    def __move_options(self, location):
        x = location[0]
        y = location[1]
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
            print('Your options for moving to next room:', ', '.join(open_path))
            player_choice = input('Input letter for your next action "n, s, e, w" for next room,\n'
                                  '"p" for potion, "i" for status: ').lower()
            input_detail = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}   # add 's': status(), 'p': potion()
            next_room = {'n': (x, y - 1), 's': (x, y + 1), 'e': (x + 1, y), 'w': (x - 1, y)}
            if player_choice not in input_detail.keys():
                print('Invalid input!')
                continue
            else:
                if input_detail[player_choice] not in open_path:
                    print('That path is not possible!')
                    continue
                else:
                    self.__current_loc((next_room[player_choice][0], next_room[player_choice][1]))
                    break

    def vision(self, x, y):                     ############# move to player class? #################
        VisionPotion.use_vision(self, x, y)

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
    a = Adventure(b)

