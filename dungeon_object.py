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
        """
        Setter for object name
        :param name: object name
        :type name: str
        :raises: if param is not str
        """
        if not isinstance(name, str):
            raise TypeError('Only string accepted for name')
        else:
            self.__name = name

    def get_name(self):
        """
        Getter for object name
        :return: object name
        :rtype: str
        """
        return self.__name

    def set_letter(self, letter):
        """
        Setter for object's letter
        :param letter: object's letter
        :type letter: str
        :raises: TypeError(non-str type), ValueError(non-alphabet value),
                ValueError(more than 1 letter)
        """
        if not isinstance(letter, str):
            raise TypeError('Only string accepted')
        elif not letter.isalpha():
            raise ValueError('No strange business, alphabet letters only!')
        elif len(letter) > 1:
            raise ValueError('No more than 1 letter')
        self.__letter = letter

    def get_letter(self):
        """
        Getter for object's letter
        :return: object's letter
        :rtype: str
        """
        return self.__letter

    # super() in child classes does not support setter property
    name = property(get_name)
    letter = property(get_letter)

    @abstractmethod
    def function(self, item=None, name=None):
        """
        Require that every object in child class have a function method
        :param item: optionally allow child class to pass in an object
        :type item: DungeonObject
        :param name: optionally allow child class to pass in player name
        :type name: str
        """
        pass

    def __str__(self):
        """
        Change default object print to name of object
        """
        return self.__name

    def __repr__(self):
        """
        Change default object print to name of object
        """
        return self.__name
