# from build_dungeon import BuildDungeon
from potion import Potion


class VisionPotion(Potion):

    def __init__(self):
        super().set_name('Vision Potion')
        super().set_letter('V')

    def function(self, map, xx, yy):
        super().timer()
        # modify values if at borders of dungeons
        x = xx if xx > 0 else 1
        x = x if x < map.width - 1 else map.width - 2
        y = yy if yy > 0 else 1
        y = y if y < map.height - 1 else map.height - 2

        print('\nOnly 8 rooms revealed, not bottom right which is covered by :::\n')

        print(''.join(map.hor[y - 1][x - 1:x + 2]) + '+\n' +
              ''.join(map.ver[y - 1][x - 1:x + 2]) + map.ver[y - 1][x + 2][0] + '\n' +
              ''.join(map.hor[y][x - 1:x + 2]) + '+\n' +
              ''.join(map.ver[y][x - 1:x + 2]) + map.ver[y][x + 2][0] + '\n' +
              ''.join(map.hor[y + 1][x - 1:x + 2]) + '+\n' +
              ''.join(map.ver[y + 1][x - 1:x + 1]) + map.ver[y + 1][x + 1][0] + ':::\n' +
              ''.join(map.hor[y + 2][x - 1:x + 1]) + '+\n')  # + '+:::')


        # print(''.join(map.hor[y - 1][x - 1:x + 2]) + '+\n' +
        #       ''.join(map.ver[y - 1][x - 1:x + 2]) + map.ver[y - 1][x + 2][0] + '\n' +
        #       ''.join(map.hor[y][x - 1:x + 2]) + '+\n' +
        #       ''.join(map.ver[y][x - 1:x + 2]) + map.ver[y][x + 2][0] + '\n' +
        #       ''.join(map.hor[y + 1][x - 1:x + 2]) + '+\n' +
        #       ''.join(map.ver[y + 1][x - 1:x + 1]) + map.ver[y + 1][x + 1][0] + ':::\n' +
        #       ''.join(map.hor[y + 2][x - 1:x + 1]) + '+\n')  # + '+:::')


if __name__ == '__main__':
    p = BuildDungeon(1)
    print(p)
    v = VisionPotion()
    v.function(p, 6, 5)

