from dungeon_object import DungeonObject
from random import choice


class HealthPotion(DungeonObject):
    """
    Inherit from abstract base class DungeonObject.
    3 types of health potion to replenish player's health. Class variable of dictionary
    type to allow random generation of potions.
    """
    type = {5: 'Minor Health Potion', 10: 'Health Potion', 15: 'Greater Health Potion'}

    def __init__(self):
        """
        Create random strength potion using random.choice and class variable
        """
        self.__set_health_points(choice(list(self.type.keys())))
        super().set_name(self.type[self.__health_points])
        super().set_letter('H')

    @property
    def health_points(self):
        """
        Getter for potion health points
        :return: potion's healing power
        :rtype: int
        """
        return self.__health_points

    def __set_health_points(self, num):
        """
        Setter for potion health points
        :param num: random choice of 5, 10 or 15 health points
        :type num: int
        :raises: if param is not int or not one of the numbers 5, 10, or 15
        """
        if isinstance(num, int):
            if num in [5, 10, 15]:
                self.__health_points = num
            else:
                raise ValueError('Only values 5, 10, or 15 allowed for health potion')
        else:
            raise TypeError('Integer only allowed')

    def inspect(self):
        """
        Lets player see name and healing power when first obtaining potion
        """
        print(f'  This {self.name} can heal {self.__health_points} points!\n')

    def function(self):
        """
        Gives player the amount of healing power
        :return: amount in healing potion
        :rtype: int
        """
        return self.__health_points



if __name__ == '__main__':
    p = HealthPotion()
    print(p.name)
    print(p.letter)
    print(p.function())
