from make_dungeon import MakeDungeon


class Adventure:

    def __init__(self):
        self.p = MakeDungeon(20, 10)
        self.p.make()
        print(self.p) # delete
        self.current_loc(0, 0)

    def current_loc(self, x, y):
        self.print_room(x, y)

        # if user reached end
        if x == self.p.width -1 and y == self.p.height -1:
            print('You have reached the end!')
            # if collected 4 pillars, return, else: self.move_options
            self.move_options(x, y)

        self.move_options(x, y)

    def print_room(self, x, y):
        print(f'Current room (x: {x}, y: {y}): ')
        print(self.p.hor[y][x] + '+\n' + self.p.ver[y][x] + self.p.ver[y][x + 1] + '\n'
              + self.p.hor[y + 1][x] + '+')

    def move_options(self, x, y):
        options = []

        if self.p.hor[y][x] == "+  ":
            options.append('North')
        if self.p.hor[y+1][x] == "+  ":
            options.append('South')
        if self.p.ver[y][x] == "   ":
            options.append('West')
        if self.p.ver[y][x+1] == "   ":
            options.append('East')

        while True:
            print('Your options for moving to next room are:', ','.join(options))
            player_choice = input('Input letter for moving to next room (e.g. n, s, e, w): ').lower()

            input_detail = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}

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

    def use_vision(self, x, y):
        s = ""
        for a, b in zip(self.__hor, self.__ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

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
    a = Adventure()

