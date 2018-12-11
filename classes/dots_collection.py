import time
import math
import random
from classes.dot import Dot

def bread(canvas, previous_generation, size, width, height):
    pos_x = width/2
    pos_y = height-25
    parent = ''

    new_generation = [Dot([pos_x, pos_y], canvas.create_oval(pos_x, pos_y, pos_x+1, pos_y+1, fill=('blue'))) for i in range(size)]

    if previous_generation != '':
        hi = mid = 0
        for x in previous_generation:
            if x.fitness > hi:
                mid = hi
                hi = x.fitness
            elif x.fitness < hi and x.fitness > mid:
                lo = mid
                mid = x.fitness

        for x in previous_generation:
            if x.fitness == hi:
                parent_1 = x
            if x.fitness == mid:
                parent_2 = x

        for y in new_generation:
            if y != parent_1 and y != parent_2:
                if y.reachedTarget != True:
                    y.directions = [circular_mean(a, b, c) for a, b, c in zip(parent_1.directions, parent_2.directions, y.directions)]
                else:
                    y.directions = [circular_mean(a, b, c) for a, b, c in zip(parent.directions, parent_2.directions, previous_generation[new_generation.index(y)].directions)]

    return new_generation


def circular_mean(a, b, c):
    value = math.atan2((math.sin(a)+math.sin(b)+math.sin(c)), (math.cos(a)+math.cos(b)+math.cos(c)))

    return value
