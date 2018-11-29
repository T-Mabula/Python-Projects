class GridCoordinate:
    """Class that models a two-dimensional coordinate"""

    def __init__(self, xpos, ypos):
        """
        Constructor for Coordinate Class

        param: int xpos: The X-component of the coordinate
        param: int ypos: The Y-component of the coordinate
        """
        if self.__x <= 3 & self.__x >= 1: self.__x = xpos
        if self.__y <= 3 & self.__y >= 1: self.__y = ypos

    @property
    def x(self):
        """
        Return the X-component of the coordinate

        return: The X-component of the coordinate
        rtype: int
        """
        return self.__x

    @property
    def y(self):
        """
        Return the Y-component of the coordinate

        return: The Y-component of the coordinate
        rtype: int
        """
        return self.__y

    def __str__(self):
        return "%d%2d" % (self.x, self.y)

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y)


class Cell:
    """Class that models the a cell in  grid"""

    __EMPTY_CELL_VAL = 0
    __CROSS_VAL = 1
    __NOUGHT_VAL = -1

    def __init__(self):
        """Default constructor"""
        self.__val = self.__EMPTY_CELL_VAL

    def __str__(self):
        if self.__val == self.__NOUGHT_VAL:
            return 'O'
        elif self.__val == self.__CROSS_VAL:
            return 'X'
        else:
            return ' '

    def __repr__(self):
        return "Cell()"

    def markWithCross(self):
        """Marks the cell with a cross"""
        self.__val = self.__CROSS_VAL

    def markWithNought(self):
        """Marks the cell with a nought"""
        self.__val = self.__NOUGHT_VAL

    @property
    def value(self):
        """Returns the numeric value of the cell

        return: Numeric value of the mark in the cell
        rtype: int
        """
        return int(self.__val)
