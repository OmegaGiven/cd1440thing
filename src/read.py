'''
    This function is made to make a dictionaries of config files used to make fractals.
'''
import os.path

def read(file):
    config = {}
    f = open(file)
    i = 0

    for line in f:
        i += 1
        line = line.strip().lower()
        if line.startswith("#") or line == "":
            continue
        key, value = line.split(":", maxsplit=1)
        key = key.strip()
        value = value.replace(" ", "")
        if key in ['axislength', 'centerx', 'centery', 'creal', 'cimag']:
            config[key] = float(value)
        elif key in ['pixels', 'iterations']:
            config[key] = int(value)
        else:
            config[key] = value

    if "centerx" not in config:
        raise Exception(f"{file} does not contain 'centerx'")
    if "centery" not in config:
        raise Exception(f"{file} does not contain 'centery'")

    config['min'] = {'x': config['centerx'] - config['axislength'] / 2.0, 'y': config['centery'] - config['axislength'] / 2.0}
    config['max'] = {'x': config['centerx'] + config['axislength'] / 2.0, 'y': config['centery'] + config['axislength'] / 2.0}
    del config['centery']
    del config['centerx']

    if 'creal' in config and 'cimag' in config:
        config['param'] = complex(config['creal'], config['cimag'])
        del config['creal']
        del config['cimag']

    config['pixelsize'] = abs(config['max']['x'] - config['min']['x']) / config['pixels']

    basename = os.path.basename(file)
    name, ext = os.path.splitext(basename)
    config['imagename'] = name

    return config
