#!/bin/env python3

# Mandelbrot Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
import Gradient


MAX_ITERATIONS = Gradient.length()
z = 0


def colorOfThePixel(c):
    """Return the color of the current pixel within the Mandelbrot set"""
    global z
    z = complex(0, 0)  # z0

    global i

    for i in range(MAX_ITERATIONS):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            z = 2.0
            return Gradient.getColor(i)  # The sequence is unbounded
    # XXX: one of these return statements made the program crash...
    return Gradient.getColor(MAX_ITERATIONS - 1)   # Indicate a bounded sequence
    return Gradient.getColor(MAX_ITERATIONS)


def paint(fractals, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 512x512 pixels in size."""

    global gradient
    global img

    fractal = fractals[imagename]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=1024, height=1024, bg=Gradient.getColor(0))
    canvas.pack()
    canvas.create_image((512, 512), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 1024

    for row in range(1024, 0, -1):
        for col in range(1024):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y))
            img.put(color, (col, 1024 - row))
        window.update()  # display a row of pixels


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")


# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.



if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in images:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

else:
    image = sys.argv[1]


# Set up the GUI so that we can paint the fractal image on the screen
window = Tk()
img = PhotoImage(width=1024, height=1024)
paint(images, image)

# Save the image as a PNG
img.write(f"{image}.png")
print(f"Wrote image {image}.png")

# Call tkinter.mainloop so the GUI remains open
mainloop()
