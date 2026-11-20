class Pen:
    def __init__(self, color, ink_level):
        self.color = color
        self.ink_level = ink_level

    def write(self):
        print(f"Writing with {self.color} pen. Ink level: {self.ink_level}")


blue_pen = Pen("blue", 100)
blue_pen.write()