# Julia Set Visualizer
from Fractal import Fractal


class Julia:

    def __init__(self, config):
        self.config = config
        self.iterations = config['iterations']

    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""
    def count(self, count):
        param = self.config['param']
        for i in range(self.iterations):
            count = count * count + param
            if abs(count) > 2:
                return i
        return self.iterations - 1
