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

    from enum import IntEnum
    class Mark(IntEnum):
        NOUGHT = -1
        EMPTY = 0
        CROSS = 1

    def __init__(self):
        """Default constructor"""
        self.__val: Cell.Mark = Cell.Mark.EMPTY

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

    def value(self) -> int:
        """Returns the numeric value of the cell

        return: Numeric value of the mark in the cell
        rtype: int
        """
        return int(self.__val)

class Board:
    __BOARD_SIZE = 3
    def __init__(self):
        self.__numOfFilledCells: int = 0
        # Create a list of Cells to make up the board
        self.__board: List[List[Cell]] = []
        for row in range(0, Board.__BOARD_SIZE):
            newRow = []
            for column in range(0, Board.__BOARD_SIZE):
                newCell = Cell()
                newRow.append(newCell)
            self.__board.append(newRow)

    def markWithCross(self, pos: GridCoordinate) -> None:
        if (self.__board[pos.x][pos.y].value() == Cell.Mark.EMPTY):
            self.__board[pos.x][pos.y].markWithCross()
            self.__numOfFilledCells += 1


    def markWithNought(self, pos: GridCoordinate) -> None:
        if (self.__board[pos.x][pos.y].value() == Cell.Mark.EMPTY):
            self.__board[pos.x][pos.y].markWithNought()
            self.__numOfFilledCells += 1

    def isFull(self) -> bool:
        return self.__numOfFilledCells == pow(Board.__BOARD_SIZE, 2)

    def value(self, pos: GridCoordinate) -> int:
        return int(self.__board[pos.x][pos.y].value())

test = Board()
test.markWithCross(GridCoordinate(1, 2))
print(test.isFull())