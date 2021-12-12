from build_dungeon import BuildDungeon
from player import Player
from pause_game import PauseGame
from clear_screen import ClearScreen
from sound_fx import SoundFx
import time

class DungeonAdventure:
    """
    This runs the game, creates dungeon and player, allow player to interact with
    objects in dungeon rooms. Allow player to move to different rooms, lose
    game by losing all of player health or win by collecting 4 pillars & reaching
    exit.
    """
    def __init__(self, player_input):
        """
        Obtained player name and difficulty choice from Instructions() as param.
        Create dungeon and player, then start __play method.
        :param player_input: obtained from Instructions() for user's input of player
        name and difficulty level
        :type player_input: Instructions class object
        :property __map: map of dungeon from BuildDungeon
        :property __room_index: list of rooms (x-coord, y-coord) created in BuildDungeon
        :property __entrance_loc: Entrance location from created in BuildDungeon
        :property __exit_loc: Exit location from BuildDungeon, always at bottom right corner 
        """
        SoundFx.in_game()
        self.__map = BuildDungeon(player_input.difficulty)
        self.__room_index = self.__map.room_index
        self.__player = Player(player_input.player_name)
        self.__entrance_loc = self.__map.entrance_loc
        self.__exit_loc = self.__map.exit_loc
        self.__play(self.__entrance_loc)

    def __play(self, location):
        """
        This method runs the game, enter room, interact with objects.
        Lose game if player health is <= 0.
        Win game if at exit with 4 pillars, then display map.
        Move to next room 
        :param location: room location of player
        :param type: set(x-coordinate: int, y-coordinate: int)
        :return: None. Exit loop to return to Main(), to exit or restart
        """
        while location is not None:
            ClearScreen()
            print('  \n================================='
                  '===============================\n\n    ',
                  self.__player.name, end=' ')
            self.__map.room_index[location].enter_room()

            room_objects = self.__room_index[location].touch_objects()
            self.__player.interact_objects(room_objects)

            # Lose game
            if self.__player.hitpoints <= 0:
                SoundFx.lose()
                ClearScreen()
                print('\n\n\n\n          ** GAME OVER **\n\n'
                      '\n\n\n        Your health reached 0!\n\n')
                time.sleep(2)
                location = None

            # Win game
            if room_objects:
                if room_objects[0].letter == 'O' and room_objects[0].freedom:
                    SoundFx.win()
                    time.sleep(2)
                    print(self.__map)
                    location = None

            # Move to next room
            if location is not None:
                location = self.__move_options(location)

    def __move_options(self, location):
        """
        Menu of options for player at each room
        List of paths created for options.
        Player status includes inventory information
        Potion menu allows consumption of potions
        Pause menu allows additional options including hidden map, reset game, & exit
        """
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
                           '  "p" for potion, "i" for status, "m" for menu: ').lower().strip()
            ref = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West', 
                   'i': 'Player Status', 'p': 'Potion Menu', 'm': 'Pause Menu'}
            next_room = {'n': (x, y - 1), 's': (x, y + 1), 'e': (x + 1, y), 'w': (x - 1, y)}
            if choice not in ref.keys():
                print('  Invalid input!')
            else:
                if choice == 'i':
                    print(self.__player)
                elif choice == 'p':
                    if self.__player.vision_potions:
                        self.__player.potion_menu(self.__map, location)
                    else:
                        self.__player.potion_menu()
                elif choice == 'm':
                    if not PauseGame.menu(self.__map):
                        # PausGame.menu() resume game returns False, then re-print room
                        self.__play(location)
                    else:
                        # Restart game when PauseGame.menu() returns True
                        return
                elif ref[choice] not in open_path:
                    print('  That path is not possible!')
                else:
                    return next_room[choice][0], next_room[choice][1]
                    
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