from dungeon_object import DungeonObject


class EntranceDoor(DungeonObject):
    def __init__(self):
        super().set_name('Entrance')
        super().set_letter('i')

    def function(self):
        print('You found an iphone.\nIt contains a "Torch" app you can use as a flashlight!\n')


if __name__ == '__main__':          ############## DELETE #################
    p = EntranceDoor()
    print(p.name)
    print(p.letter)