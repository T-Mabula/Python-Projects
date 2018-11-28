class GridCoordinate:
    """Class that models a two-dimensional coordinate"""

    __x: int = 0
    __y: int = 0

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



