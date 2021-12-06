from potion import Potion


class HealingPotion(Potion):

    def __init__(self):
        super().set_name('Healing Potion')
        super().set_letter('H')

    def function(self):
        super().timer()
        #function for player health


if __name__ == '__main__':          ############## DELETE #################
    p = HealingPotion()
    print(p.name)
    print(p.letter)
    p.timer()