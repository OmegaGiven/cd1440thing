# Julia Set Visualizer
from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, config):
        self.config = config
        self.MAX_ITERATIONS = config['iterations']

    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""
    def count(self, count):
        param = self.config['param']
        for i in range(self.MAX_ITERATIONS):
            count = count * count + param
            if abs(count) > 2:
                return i
        return self.MAX_ITERATIONS - 1

    def getIterations(self):
        return self.MAX_ITERATIONS

    def getConfig(self):
        return self.config
