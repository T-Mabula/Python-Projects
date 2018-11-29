from typing import List


class GridCoordinate:
    """Class that models a two-dimensional coordinate"""

    def __init__(self, xpos: int, ypos: int):
        """
        Constructor for Coordinate Class

        param: int xpos: The X-component of the coordinate
        param: int ypos: The Y-component of the coordinate
        """
        if xpos >= 3 & xpos >= 1:
            self.__x = xpos
        if ypos <= 3 & ypos >= 1:
            self.__y = ypos

    @property
    def x(self) -> int:
        """
        Return the X-component of the coordinate

        return: The X-component of the coordinate
        rtype: int
        """
        return self.__x

    @property
    def y(self) -> int:
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

    def __eq__(self, other):
        return bool((int(self.x) == int(other.x)) & (int(self.y) == int(other.y)))

    def __ne__(self, other):
        return not self.__eq__(other)


class Cell:
    """Class that models the a cell in  grid"""

    from enum import Enum
    class Mark(Enum):
        NOUGHT = -1
        EMPTY = 0
        CROSS = 1

    def __init__(self):
        """Default constructor"""
        self.__val: int = Cell.Mark.NOUGHT

    def __str__(self):
        if self.__val == Cell.Mark.NOUGHT:
            return 'O'
        elif self.__val == Cell.Mark.CROSS:
            return 'X'
        else:
            return ' '

    def __repr__(self):
        return "Cell()"

    def markWithCross(self) -> None:
        """Marks the cell with a cross"""
        self.__val = Cell.Mark.CROSS

    def markWithNought(self) -> None:
        """Marks the cell with a nought"""
        self.__val = Cell.Mark.NOUGHT

    @property
    def value(self) -> int:
        """Returns the numeric value of the cell

        return: Numeric value of the mark in the cell
        rtype: int
        """
        return int(self.__val)


class Board:
    """Class that models a 3X3 playing board"""
    __SIZE_OF_BOARD = 3

    def __int__(self):
        self.__positionsFilled: int = 0
        # Generate a list of cells to generate a board
        self.__board: List[List[Cell]] = []
        """
        for row in range(0, Board.__SIZE_OF_BOARD):
            rowList: List[Cell] = []
            for column in range(0, Board.__SIZE_OF_BOARD):
                newCell = Cell()
                rowList.append(newCell)
            self.__board.append(rowList)
        """

    def markWithCross(self, position: GridCoordinate) -> None:
        """
        Marks a specified cell in the board with a cross

        param: GridCoordinate position: The coordinate of the cell to be marked
        rtype: None
        """
        if (self.__board[position.x()][position.y()].value() == Cell.Mark.EMPTY):
            self.__board[position.x][position.y].markWithCross()
            self.__positionsFilled += 1

    def markWithNought(self, position: GridCoordinate) -> None:
        """
        Marks a specified cell in the board with a nought

        param: GridCoordinate position: The coordinate of the cell to be marked
        rtype: None
        """
        if (self.__board[position.x()][position.y()].value() == Cell.Mark.EMPTY):
            self.__board[position.x][position.y].markWithNought()
            self.__positionsFilled +=1

    def value(self, position: GridCoordinate) -> int:
        """
        Returns the numeric value of a specified cell in the board

         param: GridCoordinate position: The coordinate of the cell to be marked
         rtype: int
         """
        return int(self.__board[position.x()][position.y()].value())

    def isFull(self) -> bool:
        """
        Returns boolean indicating whether the board is full or not

        rtype: bool
        """
        return bool(self.__positionsFilled == pow(Board.__SIZE_OF_BOARD, 2))


test = Board()
print(test.isFull())