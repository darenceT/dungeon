import random

from room import Room


class Dungeon:

    def __init__(self, row_count, col_count):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count

        for r in range(0, self.__rowCount):
            self.__maze.append([Room() for c in range(0, self.__colCount)])

        self.build_maze()

    def build_maze(self):

        #SKELETON CODE THAT IS PROOF OF CONCEPT
        #EACH INDIVIDUAL TASK SHOULD GO IN ITS OWN METHOD
        #CODE BELOW DOES NOT HAVE ERROR CHECKING




        # make some rooms impassible
        # rand gen chance a room is impassable
        # GIGANTIC NOTE: AFTER MAKING ROOMS IMPASSABLE YOU NEED TO CHECK TO SEE IF YOU CAN TRAVERSE MAZE
        # >>IF NOT YOU NEED TO RESET IMPASSABLE ROOMS
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                number = random.randint(1, 100)
                if number > 80: #x% chance a room is impassable
                    self.__maze[row][col].set_impassible(True)

        # set entrance and exit, make sure you make room passable
        self.__maze[0][0].set_entrance()
        self.__maze[0][0].set_impassible(False)
        self.__maze[self.__rowCount-1][self.__colCount-1].set_exit()
        self.__maze[self.__rowCount - 1][self.__colCount - 1].set_impassible(False)

        # place pillars after entrance/exit, watch for impassable

        #place health potions
        #could also do vision and pits
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                #make sure room not impassible
                if self.__maze[row][col].can_enter():
                    # generate a random value
                    number = random.randint(1, 100)
                    if self.__maze[row][col].get_health_chance() >= number:

                        self.__maze[row][col].set_health(True)







    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__rowCount):
            print("row ", row)
            for col in range(0, self.__colCount):
                print("col", col)
                print(self.__maze[row][col].__str__())
            print()

    def set_health_potion(self, row, col):
        self.__maze[row][col].set_health(True)

    # WARNING: Work in progress ;-)
    #initial call if you know entrance is 0,0 would be traverse(0, 0)
    def traverse(self, row, col):
        found_exit = False
        if self.is_valid_room(row, col):
            self.__maze[row][col].set_visited(True)
            # check for exit
            if self.__maze[row][col].is_exit():
                return True
            # not at exit so try another room: south, east, north, west
            found_exit = self.traverse(row + 1, col)#south
            if not found_exit:
                found_exit = self.traverse(row, col + 1)#east
            if not found_exit:
                found_exit = self.traverse(row - 1, col)#north
            if not found_exit:
                found_exit = self.traverse(row, col - 1)#west

            # if we did not reach the exit from this room we need mark it as visited to
            # avoid going into the room again
            if not found_exit:
                self.__maze[row][col].set_visited(True)

        else:  # tried to move into a room that is not valid
            return False
        return found_exit

    def is_valid_room(self, row, col):
        return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][col].can_enter()


dungeon = Dungeon(3, 3)
#dungeon.set_health_potion(0, 0)
if dungeon.traverse(0,0):
    print("whoo hoo, we reached the exit")
else:
    print("exit not reachable")
dungeon.print_maze()
