from GreyScale import GreyScale
from TwoColor import TwoColor


class GradientFactory:

    def makeGradient(self, iterations, type):

        if type == "BinaryColor" or type is None:
            print("GradientFactory: Creating default color gradient")
            return TwoColor(iterations)

        elif type == "GreyScale":
            return GreyScale(iterations)

        raise NotImplementedError("Invalid gradient requested")
