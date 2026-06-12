import os

import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [6,3]

map_objects = [[2, 3], [5, 4], [3, 4], [10, 6]]

while True:


    print('+' + '-' * (MAP_WIDTH * 3) + '+')

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range (MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = '*'
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = '@'
                if object_in_cell:
                    map_objects.remove(object_in_cell)

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print('+' + '-' * (MAP_WIDTH * 3) + '+')

    #direction = input('donde te quieres mover? [WASD]: ')

    direction = readchar.readkey()

    if direction == 'w':
        my_position[POS_Y] -= 1
        if my_position[POS_Y] == 0:
            my_position[POS_Y] = 15
    elif direction == 's':
        my_position[POS_Y] += 1
        if my_position[POS_Y] == 15:
            my_position[POS_Y] = 0
    elif direction == 'a':
        my_position[POS_X] -= 1
        if my_position[POS_X] == 0:
            my_position[POS_X] = 20
    elif direction == 'd':
        my_position[POS_X] += 1
        if my_position[POS_X] == 20:
            my_position[POS_X] = 0
    elif direction == 'q':
        break

    os.system('clear')


