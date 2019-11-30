'''
The driver program; imports other modules, accepts
    command-line arguments and calls upon other modules to display a fractal
    on-screen and write a PNG image
'''
import sys
import Config
import ImagePainter

image = ""


def main():

    if len(sys.argv) < 2:
        print("Usage: main.py FRACTALNAME")
        print("Where FRACTALNAME is one of:")
        for i in Config.getImage():
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in Config.getImage():
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in Config.getImage():
            print(f"\t{i}")
        sys.exit(1)

    else:
        image = sys.argv[1]

    ImagePainter.imagePainter(image)


main()
