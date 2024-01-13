from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MIN_ROWS = 2
MIN_COLUMNS = 2
MIN_MINES = 2
MAX_ROWS = 12
MAX_COLUMNS = 12
MAX_MINES = 12

DEFAULT_ROWS = 8
DEFAULT_COLUMNS = 8
DEFAULT_MINES = 10

GREY0 = "#606060"
GREY1 = "#2d2d30"
GREY2 = "#252526"
GREY3 = "#1e1e1e"
BLUE = "#007acc"


def validate_integer_input(action, value_if_allowed):
    """
    Validates if the input value is an integer.

    Args:
        action (str): The action being performed. Only "1" is considered for validation.
        value_if_allowed (str): The value being inserted.

    Returns:
        bool: True if the value is a valid integer, False otherwise.
    """
    if action == "1":  # action = 1, text is being inserted
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return True


def validate_board_size(rows, columns, mines):
    """
    Validates the board size.

    Args:
        rows (int): The number of rows.
        columns (int): The number of columns.
        mines (int): The number of mines.

    Returns:
        bool: True if the board size is valid, False otherwise.
    """
    return (
        MIN_ROWS <= rows <= MAX_ROWS
        and MIN_COLUMNS <= columns <= MAX_COLUMNS
        and MIN_MINES <= mines <= MAX_MINES
        and mines
        <= round(
            (rows * columns) / 4
        )  # Mines can't be more than 1/4 of the total number of squares
    )


def screen_width_prcnt(percentage):
    """
    Calculates the width of the screen in pixels based on the given percentage.

    Args:
        percentage (int): The percentage of the screen width to calculate.

    Returns:
        int: The calculated width of the screen in pixels.
    """
    return int(SCREEN_WIDTH * percentage / 100)


def screen_height_prcnt(percentage):
    """
    Calculates the screen height based on the given percentage.

    Args:
        percentage (int): The percentage of the screen height to calculate.

    Returns:
        int: The calculated screen height.

    """
    return int(SCREEN_HEIGHT * percentage / 100)
