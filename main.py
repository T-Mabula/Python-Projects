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
    """Class that models a 3X3 board"""
    __BOARD_SIZE = 3

    def __init__(self):
        """Default constructor"""
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
        """
        Marks a specified position on the board with a cross

        :param pos: GridCoordinate of cell to be marked with a cross
        :return: None
        """
        if (self.__board[pos.x][pos.y].value() == Cell.Mark.EMPTY):
            self.__board[pos.x][pos.y].markWithCross()
            self.__numOfFilledCells += 1


    def markWithNought(self, pos: GridCoordinate) -> None:
        """
        Marks a specified position on the board with a nought

        :param pos: GridCoordinate of cell to be marked with a nought
        :return: None
        """
        if (self.__board[pos.x][pos.y].value() == Cell.Mark.EMPTY):
            self.__board[pos.x][pos.y].markWithNought()
            self.__numOfFilledCells += 1

    def isFull(self) -> bool:
        """
        Indicates whether the playing board is full or not

        :return: Boolean value indicating whether playing board is full or not
        """
        return self.__numOfFilledCells == pow(Board.__BOARD_SIZE, 2)

    def value(self, pos: GridCoordinate) -> int:
        """
        Returns a numeric value corresponding to the contents of the specified cell

        :param pos: GridCoordinate of cell
        :return: Integer value representing contents of cell
        """
        return int(self.__board[pos.x][pos.y].value())


class Player:
    """Class that manages the logic component of each player"""
    def __init__(self):
        """Default constructor"""
        self.__name: str = ''
        self.__won: bool = False
        self.__symbol: Cell.Mark.Symbol = Cell.Mark.CROSS

    @property
    def name(self) -> str:
        """
        Returns the name of the player

        :return: Name of player
        :rtype: str
        """

        return self.__name

    @name.setter
    def name(self, playerName: str) -> None:
        """
        Sets the name of the player

        :param playerName: Name of the player
        :return: None
        """
        self.__name = playerName

    @property
    def won(self) -> bool:
        """
        Returns whether the player has won or not

        :return: Boolean indicating whether the player has won or not
        :rtype: bool
        """
        return self.__won

    @won.setter
    def won(self, winStatus: bool) -> None:
        """
        Sets the player to win or lose

        :param winStatus: Boolean inidicating whether the player has won or not
        :return: None
        """
        self.__won = winStatus

    @property
    def symbol(self) -> Cell.Mark:
        """
        Returns the mark symbol of the player on the board (i.e. whether the player marks the board with a cross or nought)

        :return: Cell.Mark indicating the mark that the player makes on the board
        :rtype: Cell.Mark
        """
        return self.__symbol

