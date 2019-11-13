#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
import Gradient

# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program?
f = {


        }

# Process command-line arguments, allowing the user to select their fractal




height = 1024
width = 1024
photo = PhotoImage(width=1024, height=1024)



def getColorFromGradient(z):
    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""

    # c is the Julia Constant; varying this value can yield interesting images
    c = complex(-1.0, 0.0)

    for j in range(78):
        z = z * z + c  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return Gradient.getColor(j)  # The sequence is unbounded
    return Gradient.getColor(77)         # Else this is a bounded sequence


def makePicture(f):
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    max = f['centerX'] + (f['axisLength'] / 2.0)


    size = abs(max - min[0]) / height

    for r in range(height, 0, -1):
        for c in range(height):
            x = min[0] + c * size
            y = min[1] + r * size
            c2 = getColorFromGradient(complex(x, y))
            photo.put(c2, (c, height - r))
        win.update()  # display a row of pixels


def makeImage():
    # Output the Fractal into a .png image
    photo.write(i + ".png")
    print("Wrote picture " + i + ".png")
    photo.write(i + ".png")

def makeCanvas():
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 1024x1024 pixels."""
    canvas = Canvas(win, width=1024, height=1024, bg=Gradient.getColor(0))
    canvas.create_image(height/2, width/2, image=photo, state="normal")
    canvas.pack()

makeCanvas()
makePicture(f[i])
makeImage()
mainloop()
