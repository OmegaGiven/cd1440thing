from GreyScale import GreyScale
from TwoColor import TwoColor
from Rainbow import Rainbow


class GradientFactory:

    def makeGradient(self, iterations, type):

        if type == "TwoColor" or type is None:
            print("GradientFactory: Creating default color gradient")
            return TwoColor(iterations)

        elif type == "GreyScale":
            return GreyScale(iterations)

        elif type == 'Rainbow':
            return Rainbow(iterations)

        raise NotImplementedError("Invalid gradient requested")
