"""This module contains the Game class. The Game class is responsible for creating the game board and handling game logic."""

import random  # in-built module

from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html

from square import Square  # Local module


class Game:
    """
    Represents a Minesweeper game.

    Attributes:
        rows (int): The number of rows in the game board.
        cols (int): The number of columns in the game board.
        mines (int): The number of mines in the game.
        flags (int): The number of flags placed on the game board.
        revealed_squares (int): The number of squares revealed on the game board.
        is_won (bool): Indicates whether the game is won or not.
        first_click (bool): Indicates whether the first click has been made or not.
        first_click_square (Square): The first-clicked square object.
        board (list): A list of lists representing the game board.
        frame (Frame): The frame that holds the game buttons.

    Methods:
        generate_buttons(): Generates the game buttons.
        in_bounds(x, y): Checks if the given coordinates are within the game board.
        calculate_adjacent_mines(x, y): Calculates the number of adjacent mines for a given square.
        set_adjacent_mines(): Sets the number of adjacent mines for each square.
        place_mines(): Places mines on the game board.
        reveal_all_squares(): Reveals all squares on the game board.
        is_game_won(): Checks if the game is won.
        flood_fill(): Flood fills the game board.
    """

    def __init__(self, frame, rows, cols, mines):
        """
        Initialize a Minesweeper game.

        Args:
            frame (object): The frame object representing the game window.
            rows (int): The number of rows in the game board.
            cols (int): The number of columns in the game board.
            mines (int): The number of mines to be placed on the game board.

        Attributes:
            rows (int): The number of rows in the game board.
            cols (int): The number of columns in the game board.
            mines (int): The number of mines to be placed on the game board.
            flags (int): The number of flagged squares on the game board.
            revealed_squares (int): The number of revealed squares on the game board.
            is_won (bool): Indicates whether the game has been won or not.
            first_click (bool): Indicates whether the first click has been made or not.
            first_click_square (object): The square object representing the first clicked square.
            board (list): A list of lists representing the game board.
            frame (object): The frame object representing the game window.
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flags = 0
        self.revealed_squares = 0
        self.is_won = False
        self.first_click = True
        self.first_click_square = None

        # make a list of lists of squares
        self.board = [[Square() for _ in range(cols)] for _ in range(rows)]
        self.frame = frame
        self.generate_buttons()
        self.place_mines()
        # self.reveal_all_squares()

    def generate_buttons(self):
        """
        Generates buttons for each square on the game board.
        Each button is associated with a Square object and has event handlers for left-click.
        The buttons are placed in a frame and centered in the game frame.

        Returns:
            None
        """
        # Create a frame to hold the buttons
        button_frame = Frame(self.frame)

        for i in range(self.rows):
            for j in range(self.cols):
                square = Square(row=i, col=j)
                self.board[i][j] = square
                square.create_btn_object(button_frame)
                square.btn_object.bind("<Button-1>", square.left_click_handler)
                square.btn_object.grid(row=i, column=j, padx=0, pady=0)

        # Place the button frame in the center of the game_frame
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

    def in_bounds(self, x, y):
        """
        Check if the given coordinates (x, y) are within the bounds of the game grid.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return 0 <= x < self.rows and 0 <= y < self.cols

    def calculate_adjacent_mines(self, x, y):
        """
        Calculates the number of adjacent mines to a given cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            int: The total number of adjacent mines.
        """
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                adjacent_x = x + x_offset
                adjacent_y = y + y_offset
                if (
                    self.in_bounds(adjacent_x, adjacent_y)
                    and self.board[adjacent_x][adjacent_y].mine == True
                ):
                    total_mines += 1
        return total_mines

    def set_adjacent_mines(self):
        """
        Sets the number of adjacent mines for each cell on the board.

        Returns:
            None
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].adjacent_mines = self.calculate_adjacent_mines(i, j)

    def place_mines(self):
        """
        Randomly places mines on the game board.

        This method randomly selects cells on the game board and sets them as mines until the desired number of mines is reached.

        Args:
            None

        Returns:
            None
        """
        placed_mines = 0
        while placed_mines < self.mines:
            row = random.randrange(0, self.rows)
            col = random.randrange(0, self.cols)
            if not self.board[row][col].mine:
                self.board[row][col].mine = True
                placed_mines += 1
        self.set_adjacent_mines()

    def reveal_all_squares(self):
        """
        Reveals all the squares on the game board that are not flagged or already revealed.

        Returns:
            None
        """
        for i in range(self.rows):
            for j in range(self.cols):
                square = self.board[i][j]
                if not square.revealed and not square.flag:
                    square.left_click_handler(None)  # Simulate left click

    def is_game_won(self):
        """
        Check if the game is won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        if self.revealed_squares == self.rows * self.cols - self.mines:
            self.is_won = True
            return True

    def flood_fill(self):
        pass
