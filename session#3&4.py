from classexample import Point


# just to test that Point was imported as expected
# a = Point(5, 5)
# print(a)


class ColorPoint(Point):

    COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]

    # this is a class that inherits from Point!
    def __init__(self, x, y, color):
        #self.x = x
        #self.y = y

       # super().__init__(self, x, y)

        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are: {self.COLORS} "

                            )

    @classmethod

    def add_extra_color(cls, color):
        """
        Add a new valid color to the list
        :param color: the name of the color to add

        """
        cls.COLORS.append(color)

    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"


red_point = ColorPoint(10, 10, "red")
ColorPoint.add_extra_color("orange")
orange_point = ColorPoint(20, 20, "orange")

