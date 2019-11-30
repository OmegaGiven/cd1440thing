import Julia
import Mandelbrot
import Mandelbrot3
from read import read


class FractalFactory:
    def makeFractal(self, file=None):
        if file:
            config = read(file)
        else:
            print('Printing default fractal')
            config = makeDefault()

        type = config.get('type')
        if type == 'julia:':
            return Julia(config)
        elif type == 'mandelbrot':
            return Mandelbrot(config)
        elif type == 'mandelbrot3':
            return Mandelbrot3(config)
        elif type is None:
            raise KeyError('no type specified in configuration file')
        else:
            raise NotImplementedError('The supplied type is not supported')

    def makeDefault(self):
        return {
            'type': 'mandelbrot',
            'pixels': 640,
            'axislength': 4.0,
            'pixelsize': 0.00625,
            'iterations': 100,
            'min': {'x': -2.0, 'y': -2.0},
            'max': {'x': 2.0, 'y': 2.0},
            'imagename': 'fullmandelbrot.png'
        }
