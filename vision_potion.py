from dungeon_object import DungeonObject
from clear_screen import ClearScreen
from art import Art
import time


class VisionPotion(DungeonObject):

    def __init__(self):
        super().set_name('Vision Potion')
        super().set_letter('V')

    @staticmethod
    def function(dungeon_map, loc):
        """
        Prints out surround 8 rooms of player's current room.
        Less than 8 rooms revealed if player is next to dungeon border.
        Timer count down credit https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
        :param dungeon_map: map instance passed from DungeonAdventure
        :type dungeon_map: BuildDungeon
        :param loc: location of player's current room
        :type loc: tuple(x-coordinate, y-coordinate)
        :return: map of current and surround 8 rooms
        :rtype: str
        """
        Art.in_game3()
        print('  *** Using potion in ...', end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='', flush=True)

        # SoundFx.vision()

        def __get_letter(xx, yy):
            objects = dungeon_map.room_index[(xx, yy)].objects

            if len(objects) > 1:
                return 'M '
            elif len(objects) == 1:
                return objects[0].letter + ' '
            else:
                return '  '

        x, y = loc
        hor = dungeon_map.hor
        ver = dungeon_map.ver

        spaces = '              '
        vision = f'\n\n{spaces}'
        vert_top = f'\n{spaces}'
        # top row
        if x-1 >= 0 and y-1 >= 0:                       # top left
            vision += hor[y-1][x-1]
            vert_top += ver[y-1][x-1][0] + __get_letter(x-1, y-1) + ver[y-1][x][0]
        elif y-1 >= 0:
            vert_top += ver[y-1][x][0]
        if y-1 >= 0:                                    # top middle
            vision += hor[y-1][x]
            vert_top += __get_letter(x, y-1)
        if x+1 < dungeon_map.width and y-1 >= 0:         # top right
            vision += hor[y-1][x+1] + '+'
            vert_top += ver[y-1][x+1][0] + __get_letter(x+1, y-1) + ver[y-1][x+2][0]
        elif y-1 >= 0:
            vision += '+'
            vert_top += '|'

        vision += vert_top + f'\n{spaces}'

        # middle row
        vert_mid = f'\n{spaces}'
        if x-1 >= 0:                                          # left middle
            vision += hor[y][x-1]
            vert_mid += ver[y][x-1][0] + __get_letter(x-1, y)
        vision += hor[y][x]                                   # center
        vert_mid += ver[y][x]
        if x+1 < dungeon_map.width:                           # right middle
            vision += hor[y][x+1] + '+'
            vert_mid += ver[y][x+1][0] + __get_letter(x+1, y) + ver[y][x+2][0]
        else:
            vision += '+'
            vert_mid += '|'
        vision += vert_mid + f'\n{spaces}'

        # bottom row
        vert_bot = f'+\n{spaces}'
        if x-1 >= 0:                                           # left bottom
            vision += hor[y+1][x-1]
            if y+1 < dungeon_map.height:
                vert_bot += ver[y+1][x-1][0] + __get_letter(x-1, y+1) + ver[y+1][x][0]
        elif y+1 < dungeon_map.height:
            vert_bot += ver[y+1][x][0]
        vision += hor[y+1][x]                                   # middle bottom
        if y+1 < dungeon_map.height:
            vert_bot += __get_letter(x, y+1) + ver[y+1][x+1][0]
        if x+1 < dungeon_map.width:                             # right bottom
            vision += hor[y+1][x+1]
            if y+1 < dungeon_map.height:
                vert_bot += __get_letter(x+1, y+1) + ver[y+1][x+2][0]
        vision += vert_bot + f'\n{spaces}'

        # very bottom horizontal
        if x-1 >= 0 and y+1 < dungeon_map.height:                # left
            vision += hor[y+2][x-1]
        if y+1 < dungeon_map.height:                             # middle
            vision += hor[y+2][x]
        if x+1 < dungeon_map.width and y+1 < dungeon_map.height: # right
            vision += hor[y+2][x+1] + f'+\n{spaces}'
        elif y+1 < dungeon_map.height:
            vision += '+\n'
        
        print(vision, '\n  Rooms surrounding you are revealed!\n'
              '  (Up to 9 including current room)')