from abc import ABC, abstractmethod


class DungeonObject(ABC):
    """
    Abstract class for all objects in dungeon: pillars, potions, pit, entrance & exit door
    Abstract method of function for each object
    Parent properties of __name, __letter, and methods getters/setters, __str/__repr
    will be inherited by child class objects. 
    """
    def __init__(self):
        """
        Name and letter for each object
        """
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
        elif len(letter) > 1:
            raise ValueError('No more than 1 letter')
        self.__letter = letter

    def get_letter(self):
        return self.__letter

    # super() in child classes does not support setter property
    name = property(get_name)
    letter = property(get_letter)

    @abstractmethod
    def function(self):
        """
        Require that every object in child class have a function method
        """
        pass

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name
