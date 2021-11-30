from make_dungeon import MakeDungeon


class Adventure:

    def __init__(self):
        self.p = MakeDungeon(2, 2)
        self.p.make()
        print(self.p)

    def print_room(self, x, y):
        print(f'Current room (x: {x}, y: {y}): ')
        print(self.p.hor[y][x] + '+\n' + self.p.ver[y][x] + self.p.ver[y][x + 1] + '\n'
              + self.p.hor[y + 1][x] + '+')


    # print('exit room')
    # print(p.hor[p.height-1][p.width-1] + '+\n' + p.ver[p.height-1][p.width-1][0] + 'X |' + '\n+--+')


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
    a.print_room(0, 1)
