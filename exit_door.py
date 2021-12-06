from dungeon_object import DungeonObject


class ExitDoor(DungeonObject):
    def __init__(self):
        super().set_name('Exit')
        super().set_letter('O')

    def function(self):
        print('You see some light...it\'s a door! There are 4 strange-key holes...')
        # checks if user has 4 pillars


if __name__ == '__main__':          ############## DELETE #################
    p = ExitDoor()
    print(p.name)
    print(p.letter)