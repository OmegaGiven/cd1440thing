# Mandelbrot Set Visualizer
import Gradient

def colorOfThePixel(c, gradient):
    """Return the color of the current pixel within the Mandelbrot set"""
    z = complex(0, 0)

    for i in range(Gradient.length()):
        z = z * z + c
        if abs(z) > 2:
            return Gradient.getColor(i)
    return Gradient.getColor(Gradient.length() - 1)