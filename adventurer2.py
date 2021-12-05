import random
from room import Room


class Adventurer():
    """Base class for players.
    1) Players have a name.
    2) Players have a specified number of hit points.
    3) Players do a specified amount of damage."""

    def __init__(self, name: str):
        self.name = name
        self.hit_point = random(75, 100)
        self.healing_potion = []
        self.vision_potion = 0
        self, pillars = []
        self.current_location = (0, 0)

    @property
    def current_location(self):
        return self.current_location

    def set_location(self, row, column):
        self.current_location = (row, column)

    def take_postion(self, potion):
        self.healing_potion.append(potion)

    def take_vision(self):
        self.vision_potion += 1

    def take_pillar(self, pillar):
        self.pillars.append(pillar)

# I will continue working on this later on