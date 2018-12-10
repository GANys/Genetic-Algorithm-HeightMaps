import time
import math
import random
from classes.dot import Dot

def bread(canvas, previous_generation, size, width, height):
    pos_x = width/2
    pos_y = height-50
    max = 0
    parent = ''

    new_generation = [Dot([pos_x, pos_y], canvas.create_oval(pos_x, pos_y, pos_x+1, pos_y+1, fill=('blue'))) for i in range(size)]

    if previous_generation != '':
        for x in previous_generation:
            if x.fitness > max:
                max = x.fitness
                parent = x

        for y in new_generation:
            if y != parent:
                if y.reachedTarget != True:
                    y.directions = [circular_mean(a, b) for a, b in zip(parent.directions, y.directions)]
                else:
                    y.directions = [circular_mean(a, b) for a, b in zip(parent.directions, previous_generation[new_generation.index(y)].directions)]

    return new_generation


def circular_mean(a, b):
    value = math.atan2((math.sin(a)+math.sin(b)), (math.cos(a)+math.cos(b)))

    return value
