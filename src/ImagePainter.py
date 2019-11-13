'''
Creates a Tk window and a  `PhotoImage`  object; the
    `PhotoImage`  stores the pixels and is capable of creating a PNG image file
'''
from tkinter import Tk, Canvas, PhotoImage, mainloop

class ImagePainter:
    def imagePainter(self, image):
        win = Tk()