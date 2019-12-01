from colour import Color
from Gradient import Gradient


class Rainbow(Gradient):
    def __init__(self, iterations):
        self.steps = int(iterations)
        red = Color('red')
        purple = Color('purple')
        self.grad = list(red.range_to(purple, self.steps))
        self.grad += list(purple.range_to(red, self.steps))[1:]

    def getColor(self, n):
        return self.grad[n].hex_l

    def getGrad(self):
        return self.grad
