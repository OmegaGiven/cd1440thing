'''
Creates a Tk window and a  `PhotoImage`  object; the
    `PhotoImage`  stores the pixels and is capable of creating a PNG image file
'''
from tkinter import Tk, Canvas, PhotoImage, mainloop
import Config
from julia import getColorFromGradient
from mandelbrot import colorOfThePixel
import Gradient

height = 1024
width = 1024

def imagePainter(image):
    window = Tk()
    if Config.image[image]["type"] == "julia":
        photo = PhotoImage(width=1024, height=1024)
        makeCanvas(photo, window)
        makePicture(Config.getImage(), photo, image, window)

    elif Config.image[image]["type"] == "mandelbrot":
        photo = PhotoImage(width=640, height=640)
        paint(Config.getImage(), photo, image, window)

    makeImage()

    mainloop() #keeps window open

def makePicture(images, photo, image, window):
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    min = ((images[image]['centerX'] - (images[image]['axisLength'] / 2.0)),
           (images[image]['centerY'] - (images[image]['axisLength'] / 2.0)))

    max = images[image]['centerX'] + (images[image]['axisLength'] / 2.0)

    size = abs(max - min[0]) / height

    for r in range(height, 0, -1):
        for c in range(height):
            x = min[0] + c * size
            y = min[1] + r * size
            c2 = getColorFromGradient(complex(x, y))
            photo.put(c2, (c, height - r))
        window.update()  # display a row of pixels

def makeImage(photo, image):
    # Output the Fractal into a .png image
    photo.write(image + ".png")
    print("Wrote picture " + image + ".png")


def makeCanvas(photo, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 1024x1024 pixels."""
    canvas = Canvas(window, width=1024, height=1024, bg=Gradient.getColor(0))
    canvas.create_image(height / 2, width / 2, image=photo, state="normal")
    canvas.pack()


def paint(images, photo, image, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 512x512 pixels in size."""

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = images[image]['centerX'] - (images[image]['axisLen'] / 2.0)
    maxx = images[image]['centerX'] + (images[image]['axisLen'] / 2.0)
    miny = images[image]['centerY'] - (images[image]['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=640, height=640, bg=Gradient.getColor(0))
    canvas.pack()
    canvas.create_image((320, 320), image=photo, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 640

    for row in range(640, 0, -1):
        for col in range(640):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y), Gradient.getGrad())
            photo.put(color, (col, 640 - row))
        window.update()  # display a row of pixels

