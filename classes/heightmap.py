import os
import numpy as np
import imageio
from PIL import Image

class HeightMap(object):
    path = 'your_file_path'
    image = ''
    pixels = ''

    def __init__(self, path):
        self.path = path
        self.image = Image.open('image.bmp')
        self.pixels = self.image.convert('RGB')

    def getPixelValue(self, pos):
        return self.pixels.getpixel((pos[0], pos[1]))
