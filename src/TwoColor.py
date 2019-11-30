from colour import Color
from Gradient import Gradient


class TwoColor(Gradient):
    def __init__(self, iterations):
        self.steps = int(iterations)
        red = Color('red')
        yel = Color('yellow')
        self.grad = list(red.range_to(yel, self.steps))
        self.grad += list(yel.range_to(red, self.steps))

    def getColor(self, n):
        return self.grad[n].hex_l

    def getGrad(self):
        return self.grad
