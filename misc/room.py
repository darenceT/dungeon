class Room:

    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = True
        self.__pillar = "No pillar"
        self.__pit = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__healthChance = 50

    def get_health_chance(self):
        return self.__healthChance

    def __str__(self):
        item_count = 0
        if self.__healthPotion:
            item_count += 1
        if self.__visionPotion:
            item_count += 1

        if item_count > 1:
            return "M"

        return "Health potion: " + str(self.__healthPotion) + "\n" \
               + "Vision potion: " + str(self.__visionPotion) + "\n" \
               + "Pillar: " + str(self.__pillar) + "\n" \
               + "Pit: " + str(self.__pit) + "\n" \
               + "Impassable: " + str(self.__impassable) + "\n" \
               + "Entrance: " + str(self.__entrance) + "\n" \
               + "Exit: " + str(self.__exit) + "\n\n"



    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_impassible(self, is_impassable):
        self.__impassable = is_impassable

    def set_exit(self):
        self.__exit = True