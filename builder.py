#name: Manuel Duarte


from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def room(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class RoomBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._room = Room1()

    @property
    def room(self):
        return self._room

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")
    
    def produce_part_d(self):
        self._product.add("PartC1")

    def produce_part_e(self):
        self._product.add("PartC1")

    def produce_part_f(self):
        self._product.add("PartC1")


class Room1:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def list_items(self):
        print(f"Room items: {', '.join(self.items)}", end="")


if __name__ == "__main__":
    builder = RoomBuilder1()

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom room: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
