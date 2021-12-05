from build_dungeon import BuildDungeon
import time


class VisionPotion:

    def __init__(self):
        pass
        # count or container of potions

    @staticmethod
    def use_vision(self, xx, yy):
        # modify values if at borders of dungeons
        x = xx if xx > 0 else 1
        x = x if x < self.p.width - 1 else self.p.width - 2
        y = yy if yy > 0 else 1
        y = y if y < self.p.height - 1 else self.p.height - 2

        print("\n*** Using vision potion in ...", end='')
        count = [' 3,', ' 2,', ' 1!']
        for i in count:
            time.sleep(1)
            print(i, end='')
        time.sleep(1)
        print('\nOnly 8 rooms revealed, not bottom right which is covered by :::\n')

        print(''.join(self.p.hor[y - 1][x - 1:x + 2]) + '+\n' +
              ''.join(self.p.ver[y - 1][x - 1:x + 2]) + self.p.ver[y - 1][x + 2][0] + '\n' +
              ''.join(self.p.hor[y][x - 1:x + 2]) + '+\n' +
              ''.join(self.p.ver[y][x - 1:x + 2]) + self.p.ver[y][x + 2][0] + '\n' +
              ''.join(self.p.hor[y + 1][x - 1:x + 2]) + '+\n' +
              ''.join(self.p.ver[y + 1][x - 1:x + 1]) + self.p.ver[y + 1][x + 1][0] + ':::\n' +
              ''.join(self.p.hor[y + 2][x - 1:x + 1]) + '+\n')  # + '+:::')


# if __name__ == '__main__':
#     p = MakeDungeon(8, 4)
#     p.make()
#     print(p)
#


    '''
    xx = 0
    yy = 3
    # modify values if at borders of dungeons
    x = xx if xx > 0 else 1
    x = x if x < p.width - 1 else p.width - 2
    y = yy if yy > 0 else 1
    y = y if y < p.height - 1 else p.height - 2

    print(''.join(p.hor[y-1][x-1:x+2]) + '+\n' +
            ''.join(p.ver[y-1][x-1:x+2]) + p.ver[y-1][x+2][0] + '\n' +
            ''.join(p.hor[y][x-1:x+2]) + '+\n' +
            ''.join(p.ver[y][x-1:x+2]) + p.ver[y][x+2][0] + '\n' +
            ''.join(p.hor[y+1][x-1:x+2]) + '+\n' +
            ''.join(p.ver[y+1][x-1:x+1]) + p.ver[y+1][x+1][0] + ':::\n' +
            ''.join(p.hor[y+2][x-1:x+1]) + '+') #+ '+:::')
    '''
