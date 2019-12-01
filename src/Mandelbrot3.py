# Mandelbrot Set Visualizer
from Fractal import Fractal


class Mandelbrot3(Fractal):
    def __init__(self, config):
        self.config = config
        self.MAX_ITERATIONS = config['iterations']

    def count(self, count):
        """Return the color of the current pixel within the Mandelbrot set"""
        j = complex(0, 0)
        for i in range(self.MAX_ITERATIONS):
            j = j * j * j + count
            if abs(j) > 2:
                return i
        return self.MAX_ITERATIONS - 1

    def getIterations(self):
        return self.MAX_ITERATIONS

    def getConfig(self):
        return self.config
