from dungeon_object import DungeonObject


class HealthPotion(DungeonObject):

    def __init__(self):
        super().set_name('Healing Potion')
        super().set_letter('H')

    def function(self):
        pass
        #function for player health


if __name__ == '__main__':          ############## DELETE #################
    p = HealthPotion()
    print(p.name)
    print(p.letter)
