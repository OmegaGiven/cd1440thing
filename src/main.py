'''
The driver program; imports other modules, accepts
    command-line arguments and calls upon other modules to display a fractal
    on-screen and write a PNG image
'''
import sys
from FractalFactory import FractalFactory
from GradientFactory import GradientFactory


def main():
    file = None
    gradientName = 'TwoColor'
    if len(sys.argv) > 1:
        file = sys.argv[1]

    if len(sys.argv) > 2:
      gradientName = sys.argv[2]

    factory = FractalFactory()
    fractal = factory.makeFractal(file)

    factory2 = GradientFactory()
    gradient = factory2.makeGradient(fractal.getIterations(), gradientName)

    ImagePainter(fractal, gradient).display()


main()
