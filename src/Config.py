'''
Contains a Python dictionary composed of fractal
    configuration data
'''
image = {
    'fullmandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLen': 2.5,
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLen': 0.004978179931102462,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
    },

    'seahorse': {
        'centerX': -0.745,
        'centerY': 0.105,
        'axisLen': 0.01,
    },

    'elephants': {
        'centerX': 0.30820836067024604,
        'centerY': 0.030620936230004017,
        'axisLen': 0.03,
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLen': 0.000051248888,
    },

    'fulljulia': {
        'centerX': 0.0,
        'centerY': 0.0,
        'axisLength': 4.0,
    },

    'hourglass': {
        'centerX': 0.618,
        'centerY': 0.00,
        'axisLength': 0.017148277367054,
    },

    'lakes': {
        'centerX': -0.339230468501458,
        'centerY': 0.417970758224314,
        'axisLength': 0.164938488846612,
    },
}

class Config:

    def getImage(self):
        return image

    def getImageIndex(i):
        return image[i]