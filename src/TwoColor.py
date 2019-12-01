from colour import Color
from Gradient import Gradient


class TwoColor(Gradient):
    def __init__(self, iterations):
        self.steps = int(iterations)
        blue = Color('blue')
        green = Color('green')
        self.grad = list(blue.range_to(blue, self.steps))
        self.grad += list(green.range_to(green, self.steps))

    def getColor(self, n):
        return self.grad[n].hex_l

    def getGrad(self):
        return self.grad
