from random import randrange

width = 35
height = 3
__impassible_rooms = []

for i in range(width // 4):
    while True:
        x = randrange(0, width)
        y = randrange(0, height)
        print(x, y)
        # Avoid entrance and exit rooms
        if x == 0 and y == 0 or x == width - 1 and y == height-1:
            continue
        elif (x, y) not in __impassible_rooms:
            __impassible_rooms.append((x, y))
            print(__impassible_rooms)
            break
