class Figure:
    def draw(self):
        raise NotImplementedError("Subclasses must implement the draw method")

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for side in range(self.a):
            print(self.a * "o ")
        print()

class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(self.h):
            print(side * "o ")
        print()

a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

square.draw()
triangle.draw()
