import tkinter as tk
import random
import os
import cv2
import PIL.Image, PIL.ImageTk

from classes.target import Target
from classes.heightmap import HeightMap
from classes.dot import Dot
from classes.dots_collection import bread

#Contact http://labos.ulg.ac.be/etho/brotcorne/

dots_number_init = 500

HM_object = HeightMap(os.path.dirname(os.path.realpath(__file__)))

cv_img = cv2.cvtColor(cv2.imread("image.bmp"), cv2.COLOR_BGR2RGB)

height, width, no_channels = cv_img.shape

root = tk.Tk()
root.title("Genetic Algorithm in Heightmaps")
canvas = tk.Canvas(master = root, width = width, height = height)

photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

canvas.create_image(0, 0, image=photo, anchor=tk.NW)

target_radius = 5
target_x = width/2
target_y = 25
target = Target(canvas.create_oval(target_x-target_radius, target_y-target_radius, target_x+target_radius, target_y+target_radius, width=0, fill=('red')), [target_x, 25], target_radius)

canvas.pack()

new_generation = ''
previous_generation = ''
generation = 1
n = 0

while generation <= 150:

    previous_generation = new_generation
    dots_number = dots_number_init

    for x in previous_generation:
        canvas.delete(x.ball)

    if generation == 1:
        new_generation = bread(canvas, '', dots_number, width, height)
    else:
        new_generation = bread(canvas, previous_generation, dots_number, width, height)

    for x in previous_generation:
        canvas.delete(x.ball)

    while (dots_number > 0):
        dots_number = dots_number_init

        for x in new_generation:
            x.frame_collision(target, width, height)
            if(x.isDead != True and x.energy >= 0):
                x.frame_move(canvas)
                x.consume_energy(HM_object)
            else:
                dots_number -= 1

        root.update() # update the display
        root.after(16) # wait 1 ms

    for x in new_generation:
        x.calculate_fitness(target)

    report = '- Generation: ' + str(generation)

    print(report)

    reached = 0

    moves = []

    for x in new_generation:
        if x.reachedTarget:
            reached += 1
            moves.append(x.move)
    print('Points to Goal: ' + str(reached))
    if moves != []:
        print('Mean moves: ' + str(round(sum(moves) / len(moves))))
    else:
        print('Mean moves: 0')

    generation += 1

root.mainloop()
