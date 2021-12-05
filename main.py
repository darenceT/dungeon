from instructions import Instructions
from adventure import Adventure


class Main:
    def __init__(self):
        self.__user = Instructions()
        self.__player_name = self.__user.player_name
        self.__difficulty = self.__user.difficulty
        self.__adventure = Adventure(self.__difficulty)


if __name__ == '__main__':
    m = Main()

