from instructions import Instructions
from adventure import Adventure


class Main:
    def __init__(self):
        # self.__user_input = Instructions()
        # self.__adventure = Adventure(self.__user_input)

        Adventure(Instructions())


if __name__ == '__main__':
    m = Main()

