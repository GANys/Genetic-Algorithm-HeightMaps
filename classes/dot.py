import tkinter as tk
import random
import math

class Dot(object):
    ball = ""
    pos = [0, 0]
    vel = [0, 0]
    acc = [0, 0]
    directions = ''
    move = 0
    energy = 0
    isDead = False
    fitness = -1
    reachedTarget = False

    # The class "constructor" - It's actually an initializer for Drops
    def __init__(self, pos, ball):
        self.ball = ball
        self.pos = pos
        self.vel = [0, 0]
        self.acc = [0, 0]
        self.directions = [random.uniform(0, 2*math.pi) for i in range(500)]
        self.move = 0
        self.energy = 150
        self.fitness = 0
        self.isDead = False
        self.reachedTarget = False

    def frame_collision(self, target, width, height):
        if self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > width-2 or self.pos[1] > height-2:
            self.isDead = True
        if (math.sqrt((self.pos[0] - target.pos[0])**2 + (self.pos[1] - target.pos[1])**2) < target.radius):
            self.isDead = True
            self.reachedTarget = True

    def frame_move(self, canvas):
        if(random.randint(0, 999) <= 1):
            self.directions[self.move] += random.uniform(-2, 2)*(2*math.pi)/360

        self.acc[0] = math.cos(self.directions[self.move])
        self.acc[1] = math.sin(self.directions[self.move])

        if(abs(self.vel[0] + self.acc[0]) < 2):
            self.vel[0] += self.acc[0]
        if(abs(self.vel[1] + self.acc[1]) < 2):
            self.vel[1] += self.acc[1]

        canvas.move(self.ball, self.vel[0], self.vel[1])
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.move += 1

    def consume_energy(self, HM_object):
        height = HM_object.getPixelValue(self.pos)[0] / 256
        self.energy -= height
        if self.energy < 0:
            self.isDead = True

    def calculate_fitness(self, target):
        if self.reachedTarget:
            self.fitness = 1 / 16 + 10000 /(self.move * self.move)
        else:
            distanceToGoal = abs(target.pos[0] - self.pos[0]) + abs(target.pos[1] - self.pos[1])
            self.fitness = 1/(distanceToGoal * distanceToGoal)
