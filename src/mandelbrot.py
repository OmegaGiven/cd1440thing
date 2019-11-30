# Mandelbrot Set Visualizer
import Gradient
import Fractal


class Mandelbrot(Fractal):
    def __init__(self, config):
        self.config = config
        self.MAX_ITERATIONS = config['iterations']

    def count(self, count):
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0)
        for i in range(self.MAX_ITERATIONS):
            z = z * z + count
            if abs(count) > 2:
                return i
        return self.MAX_ITERATIONS - 1
