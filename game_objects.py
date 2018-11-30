from typing import List


class GridCoordinate:
    """Class that models a two-dimensional coordinate"""
    __y: int
    __x: int

    def __init__(self, xpos: int, ypos: int):
        """
        Constructor for Coordinate Class

        :param: int xpos: The X-component of the coordinate
        :param: int ypos: The Y-component of the coordinate
        """
        self.__x = xpos
        self.__y = ypos

    @property
    def x(self) -> int:
        """
        Return the X-component of the coordinate

        return: The X-component of the coordinate
        rtype: int
        """
        return int(self.__x)

    @property
    def y(self) -> int:
        """
        Return the Y-component of the coordinate

        return: The Y-component of the coordinate
        rtype: int
        """
        return int(self.__y)

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

    def mark(self, symbol: Mark) -> None:
        """Marks the cell with a cross

        :param symbol: The symbol to be marked on the cell
        """
        self.__val = symbol


    def value(self) -> int:
        """Returns the numeric value of the cell

        return: Numeric value of the mark in the cell
        rtype: int
        """
        return int(self.__val)

class CoordinateOutOfRange(Exception):
    """Exception for coordinates out of the board's limits"""
    def __init___(self):
        self.__msg = 'Grid coordinate out of board range'
        super(CoordinateOutOfRange).__init__(self.__msg)

class OccupiedCell(Exception):
    def __init__(self):
        self.__msg = 'Attempt to overwrite occupied cell on board'
        super(OccupiedCell, self).__init__(self.__msg)

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

    @property
    def size(self)-> int:
        """
        Returns the length/width of the square board

        :return: Integer indicating the length/width of the square board
        """
        return int(Board.__BOARD_SIZE)


    def markBoard(self, symbol: Cell.Mark, pos: GridCoordinate) -> None:
        """
        Marks a specified position on the board with a nought

        :param symbol: The symbol to be marked on the board
        :param pos: GridCoordinate of cell to be marked with a nought
        :return: None
        """
        if pos.x < 1 or pos.x > Board.__BOARD_SIZE or pos.y < 1 or pos.y > Board.__BOARD_SIZE:
            raise CoordinateOutOfRange
        if (self.__board[pos.x - 1][pos.y - 1].value() == Cell.Mark.EMPTY):
            self.__board[pos.x - 1][pos.y - 1].mark(symbol)
            self.__numOfFilledCells += 1
        else:
            raise OccupiedCell

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
        return int(self.__board[pos.x - 1][pos.y - 1].value())


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

    @symbol.setter
    def symbol(self, symbol: Cell.Mark) -> None:
        """
        Sets the mark symbol of the player on the board (i.e. whether the player marks the board with a cross or nought)

        :param: symbol: The mark that the player will put on the game board
        :rtype: None
        """
        self.__symbol = symbol

class BoardScanner:
    """Class that scans the game board and tallies the markings on the board"""

    def __threeInARow(self, symbol: Cell.Mark, total: int)-> bool:
        '''
        Check if a given row, column or diagonal total corresponds to a given symbol occuring three times consecutively

        :param: symbol: The symbol to be checked
        :total: total: The row, column or diagonal total on the board
        :return: Boolean indicating whether the given symbol has occured thrice
        :rtype: bool
        '''

        return 3 * int(symbol) == total


    def __scanRows(self, symbol: Cell.Mark, board: Board)-> bool:
        """
        Scans the rows of the board and returns whether a given mark has been seen three consecutive times

        :param: symbol: The symbol to be checked for any occurances on the board three times in a row
        :param: board: The game board
        """
        for row in range(1, board.size + 1):
            sum = 0
            for column in range(1, board.size + 1):
                sum += board.value(GridCoordinate(row, column))
            if self.__threeInARow(symbol, sum):
                return True

        return False

    def __scanColumns(self, symbol: Cell.Mark, board: Board)-> bool:
        """
        Scans the columns of the board and returns whether a given mark has been seen three consecutive times

        :param: symbol: The symbol to be checked for any occurances on the board three times in a column
        :param: board: The game board
        """
        for column in range(1, board.size + 1):
            sum = 0
            for row in range(1, board.size + 1):
                sum += board.value(GridCoordinate(row, column))
            if self.__threeInARow(symbol, sum):
                return True

        return False

    def __scanDiagonals(self, symbol: Cell.Mark, board: Board)-> bool:
        """
        Scans the columns of the board and returns whether a given mark has been seen three consecutive times

        :param: symbol: The symbol to be checked for any occurances on the board three times in a column
        :param: board: The game board
        """
        # Check the diagonal from the top left corner to the bottom right
        sum = 0
        for row in range(1, board.size + 1):
            column = row
            sum += board.value(GridCoordinate(row, column))

        if self.__threeInARow(symbol, sum):
            return True

        return False

        # Check the diagonal from the top right corner to the bottom left
        sum = 0
        for column in range(1, board.size + 1):
            row = board.size - column + 1
            sum += board.value(GridCoordinate(row, column))

        if self.__threeInARow(symbol, sum):
            return True

        return False

    def __scanBoard(self, symbol: Cell.Mark, board: Board) -> bool:
        """
        Scans the board and returns whether a given mark has been seen three consecutive times

        :param: symbol: The symbol to be checked for any occurances on the board three consecutive times
        :param: board: The game board
        """
        return self.__scanRows(symbol, board) or self.__scanColumns(symbol, board) or self.__scanDiagonals(symbol, board)

    def hasPlayerWon(self, player: Player, board: Board)-> bool:
        """"
        Scans the board and return whether a given player has won

        :param player: The player whose marking will be checked to see if it won on the gameBoard
        :param board: The current gameplay board
        :return: Returns whether the player has won or not
        """

        return self.__scanBoard(player.symbol, board)


