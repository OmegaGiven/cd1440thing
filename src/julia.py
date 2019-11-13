# Julia Set Visualizer
import Gradient

def getColorFromGradient(z):
    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""
    # c is the Julia Constant; varying this value can yield interesting images
    c = complex(-1.0, 0.0)

    gradientRange = 78
    for i in range(gradientRange):
        z = z * z + c
        if abs(z) > 2:
            return Gradient.getColor(i)
    return Gradient.getColor(Gradient.length() - 1)