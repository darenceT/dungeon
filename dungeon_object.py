from abc import ABC, abstractmethod


class DungeonObject(ABC):
    def __init__(self):
        self.__name = ''

    @abstractmethod
    def function(self):
        pass

    @abstractmethod
    def char(self):
        pass

    def __str__(self):
        return self.__name

    def print(self):
        print(name)

