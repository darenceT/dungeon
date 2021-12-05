from build_dungeon import BuildDungeon
from vision_potion import VisionPotion


class Adventure:

    def __init__(self, difficulty):
        self.p = BuildDungeon(difficulty)
        print(self.p)                   ################### delete
        self.current_loc(0, 0)

    def current_loc(self, x, y):
        self.p.room_index[(x, y)].enter_room()
        print(self.p.room_index[(x, y)])

        items_found = self.p.room_index[(x, y)].obtain_items()

        # player.pickup(items_found)

        # if user reached end
        if x == self.p.width -1 and y == self.p.height -1:
            print('You have reached the exit!')
            # if player.pillars:          True for collected all 4
            #     print('you win! You have gained adequate knowledge for quarter 2 and still much to learn...')
            # else:
            #     print('Keep looking for those pillars of success...')
            #     self.move_options(x, y)

        # self.vision(x, y)           ################################ DELETE
        self.move_options(x, y)

    def move_options(self, x, y):
        options = []

        if self.p.hor[y][x] == "+  ":
            options.append('North')
        if self.p.hor[y+1][x] == "+  ":
            options.append('South')
        if self.p.ver[y][x][0] == " ":
            options.append('West')
        if self.p.ver[y][x+1][0] == " ":
            options.append('East')

        while True:
            print('Your options for moving to next room:', ', '.join(options))
            player_choice = input('Input letter for your next action "n, s, e, w" for next room,\n'
                                  '"p" for potion, "i" for status: ').lower()
            input_detail = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}   # add 's': status(), 'p': potion()

            if player_choice not in input_detail.keys():
                print('Invalid input!')
                continue
            else:
                if input_detail[player_choice] not in options:
                    print('That path is not possible!')
                    continue
                else:
                    move_next = {'n': (x, y - 1), 's': (x, y + 1), 'e': (x + 1, y), 'w': (x - 1, y)}
                    self.current_loc(move_next[player_choice][0], move_next[player_choice][1])
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
    # try:
    mode = int(input('Select difficulty:\n1. Easy\n2. Normal\n3. Hard\nType 1, 2 or 3: '))
    # except TypeError:

    a = Adventure(mode)

