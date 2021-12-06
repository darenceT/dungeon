from abc import ABC, abstractmethod


class DungeonObject(ABC):
    def __init__(self):
        self.__name = "Error for seeing abstract name"
        self.__letter = 'Error for seeing abstract letter'

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Only string accepted for name')
        self.__name = name

    def get_name(self):
        return self.__name

    def set_letter(self, letter):
        if not isinstance(letter, str):
            raise TypeError('Only string accepted')
        elif not letter.isalpha():
            raise ValueError('No strange business, alphabet letters only!')
        elif len(letter) >1:
            raise ValueError('No more than 1 letter')
        self.__letter = letter

    def get_letter(self):
        return self.__letter

    name = property(get_name, set_name)
    letter = property(get_letter, set_name)

    @abstractmethod
    def function(self):
        pass

    def __str__(self):
        return self.__name
