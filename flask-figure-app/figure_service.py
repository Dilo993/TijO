class Figure:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def set_color(self, new_color):
        self.color = new_color

    def get_color(self):
        return self.color

class Square(Figure):
    def __init__(self, color):
        super().__init__("square", color)

class Circle(Figure):
    def __init__(self, color):
        super().__init__("circle", color)

class Triangle(Figure):
    def __init__(self, color):
        super().__init__("triangle", color)


class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square("#808080"),
            "circle": Circle("#808080"),
            "triangle": Triangle("#808080")
        }

    def get_all_colors(self):
        return {name: figure.get_color() for name, figure in self.figures.items()}

    def set_color(self, figure_type, new_color):
        if figure_type in self.figures:
            self.figures[figure_type].set_color(new_color)
            return True
        return False

    def set_color_all(self, new_color): 
        for figure in self.figures.values():
            figure.set_color(new_color)