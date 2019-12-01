'''
Creates a Tk window and a  `PhotoImage`  object; the
    `PhotoImage`  stores the pixels and is capable of creating a PNG image file
'''
from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:
    def __init__(self, fractal, gradient):
        self.fractal = fractal
        self.gradient = gradient
        self.type = fractal.getConfig()['type']
        self.size = self.fractal.getConfig()['pixels']
        self.pixelSize = self.fractal.getConfig()['pixelsize']
        self.min = self.fractal.getConfig()['min']

    def show(self):
        window = Tk()
        photo = PhotoImage(width=self.size, height=self.size)
        self.paint(photo, window)
        mainloop()

    def makeImage(self, photo, image):
        # Output the Fractal into a .png image
        photo.write(image + ".png")
        print("Wrote picture " + image + ".png")

    def paint(self, photo, window):
        """Paint a Fractal image into the TKinter PhotoImage canvas."""
        self.makeCanvas(photo, window)
        for row in range(self.size, 0, -1):
            for column in range(self.size):
                x = self.min['x'] + column * self.pixelSize
                y = self.min['y'] + row * self.pixelSize
                i = complex(x, y)
                color = self.gradient.getColor(self.fractal.count(i))
                photo.put(color, (column, self.size - row))
            window.update()

    def makeCanvas(self, photo, window):
        """Paint a Fractal image into the TKinter PhotoImage canvas."""
        canvas = Canvas(window, width=self.size, height=self.size, bg='#ffffff')
        canvas.pack()
        canvas.create_image(self.size / 2, self.size / 2, image=photo, state="normal")

