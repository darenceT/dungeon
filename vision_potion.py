from dungeon_object import DungeonObject
import time


class VisionPotion(DungeonObject):

    def __init__(self):
        super().set_name('Vision Potion')
        super().set_letter('V')

    @staticmethod
    def function(dungeon_map, loc):
        print("  *** Potion effects in ...3, 2, 1!", end='')
        # count = [' 3,', ' 2,', ' 1!']
        # for i in count:
        time.sleep(2)
        # print(i, end='')

        def get_letter(xx, yy):
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

        vision = '\n\n              '
        vert_top = '\n              '
        # top row
        if x-1 >= 0 and y-1 >= 0:                       # top left
            vision += hor[y-1][x-1]
            vert_top += ver[y-1][x-1][0] + get_letter(x-1, y-1) + ver[y-1][x][0]
        elif y-1 >= 0:
            vert_top += ver[y-1][x][0]
        if y-1 >= 0:                                    # top middle
            vision += hor[y-1][x]
            vert_top += get_letter(x, y-1)
        if x+1 < dungeon_map.width and y-1 >= 0:         # top right
            vision += hor[y-1][x+1] + '+'
            vert_top += ver[y-1][x+1][0] + get_letter(x+1, y-1) + ver[y-1][x+2][0]
        elif y-1 >= 0:
            vision += '+'
            vert_top += '|'

        vision += vert_top + '\n              '

        # middle row
        vert_mid = '\n              '
        if x-1 >= 0:                                          # left middle
            vision += hor[y][x-1]
            vert_mid += ver[y][x-1][0] + get_letter(x-1, y)
        vision += hor[y][x]                                   # center
        vert_mid += ver[y][x]
        if x+1 < dungeon_map.width:                           # right middle
            vision += hor[y][x+1] + '+'
            vert_mid += ver[y][x+1][0] + get_letter(x+1, y) + ver[y][x+2][0]
        else:
            vision += '+'
            vert_mid += '|'
        vision += vert_mid + '\n              '

        # bottom row
        vert_bot = '+\n              '
        if x-1 >= 0:                                           # left bottom
            vision += hor[y+1][x-1]
            if y+1 < dungeon_map.height:
                vert_bot += ver[y+1][x-1][0] + get_letter(x-1, y+1) + ver[y+1][x][0]
        elif y+1 < dungeon_map.height:
            vert_bot += ver[y+1][x][0]
        vision += hor[y+1][x]                                   # middle bottom
        if y+1 < dungeon_map.height:
            vert_bot += get_letter(x, y+1) + ver[y+1][x+1][0]
        if x+1 < dungeon_map.width:                             # right bottom
            vision += hor[y+1][x+1]
            if y+1 < dungeon_map.height:
                vert_bot += get_letter(x+1, y+1) + ver[y+1][x+2][0]
        vision += vert_bot + '\n              '

        # very bottom horizontal
        if x-1 >= 0 and y+1 < dungeon_map.height:                # left
            vision += hor[y+2][x-1]
        if y+1 < dungeon_map.height:                             # middle
            vision += hor[y+2][x]
        if x+1 < dungeon_map.width and y+1 < dungeon_map.height: # right
            vision += hor[y+2][x+1] + '+\n              '
        elif y+1 < dungeon_map.height:
            vision += '+\n'

        print(vision)


if __name__ == '__main__':
    p = BuildDungeon(1)
    print(p)
    v = VisionPotion()
    v.function(p, 6, 5)
