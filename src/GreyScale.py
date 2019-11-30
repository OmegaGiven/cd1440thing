from colour import Color
from Gradient import Gradient


class GreyScale(Gradient):

    def __init__(self, iterations):
        steps = int(iterations)
        blk = Color('black')
        wht = Color('white')
        self.grad = list(blk.range_to(wht, steps))
        self.grad += list(wht.range_to(blk, steps))[1:]

    def getColor(self, n):
        return self.grad[n].hex_l

    def getGrad(self):
        return self.grad
