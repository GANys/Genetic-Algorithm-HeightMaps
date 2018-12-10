import tkinter as tk
import random

class Target(object):
    pos = [0, 0]
    radius = 0
    image = ""

    # The class "constructor" - It's actually an initializer for Targets
    def __init__(self, image, pos, radius):
        self.pos = pos
        self.radius = radius
        self.image = image
