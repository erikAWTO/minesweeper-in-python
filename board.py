import random  # Python Standard Library: https://docs.python.org/3/library/random.html

from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html
from tkinter import (
    messagebox,
)  # 3rd party: https://docs.python.org/3/library/tkinter.html

from square import Square  # Local module


class Board:
    """
    Represents a Minesweeper game board.

    The Board class is responsible for creating and managing the game board.
    It handles the placement of mines, generation of buttons, and event handling.

    Attributes:
        frame (Frame): The frame where the board is placed.
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.
        mines (int): The number of mines in the board.
        grid (list): A 2D list representing the board grid.
        first_click (bool): Flag to indicate if the first click has been made.
        first_click_adjacents (list): List of adjacent squares to the first click.

    Methods:
        __init__(self, frame, rows, cols, mines): Initializes a Board object.
        place_buttons(self): Generates buttons for each square on the game board.
        place_mines(self): Randomly places mines on the game board.
        right_click_handler(self, event): Handles the right-click event on a square button.
        left_click_handler(self, event): Handles the left-click event on a square button.
        reveal_mines(self): Reveals all the mines on the game board.
        game_over(self): Handles the game over condition.
        game_won(self): Handles the game won condition.
        first_move(self, row, col): Handles the first move of the game.
        in_bounds(self, x, y): Checks if the given coordinates are within the bounds of the game grid.
        count_adjacent_mines(self, row, col): Calculates the number of adjacent mines to a given cell.
        set_adjacent_mines(self): Sets the number of adjacent mines for each square on the game board.
        flood_fill(self, row, col): Performs flood fill algorithm to reveal adjacent squares with no adjacent mines.

    Returns:
        None
    """

    def __init__(self, frame, rows, cols, mines):
        """
        Initializes a Board object.

        Args:
            frame (Frame): The frame where the board will be placed.
            rows (int): The number of rows in the board.
            cols (int): The number of columns in the board.
            mines (int): The number of mines in the board.

        Attributes:
            frame (Frame): The frame where the board is placed.
            rows (int): The number of rows in the board.
            cols (int): The number of columns in the board.
            mines (int): The number of mines in the board.
            flags (int): The number of flags placed on the board.
            grid (list): A 2D list representing the board grid.
            first_click (bool): Flag to indicate if the first click has been made.
            first_click_adjacents (list): List of adjacent squares to the first click.

        Returns:
            None
        """
        self.frame = frame
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flags = 0
        self.game_over = False
        self.game_won = False
        self.grid = [[Square() for _ in range(cols)] for _ in range(rows)]

        self.first_click = True
        self.first_click_adjacents = []

        self.place_buttons()

    def place_buttons(self):
        """
        Generates buttons for each square on the game board.
        Each button is associated with a Square object and has event handlers for left-click and right-click.
        The buttons are placed in a frame and centered in the game frame.

        Args:
            None

        Returns:
            None
        """
        # Create a frame to hold the buttons
        button_frame = Frame(self.frame)

        for i in range(self.rows):
            for j in range(self.cols):
                square = Square(row=i, col=j)
                self.grid[i][j] = square
                square.create_btn_object(button_frame)
                square.btn_object.bind("<Button-1>", self.left_click_handler)
                square.btn_object.bind("<Button-3>", self.right_click_handler)
                square.btn_object.grid(row=i, column=j, padx=0, pady=0)

        # Place the button frame in the center of the game_frame
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

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
            if (
                not self.grid[row][col].mine
                and (row, col) not in self.first_click_adjacents
            ):
                self.grid[row][col].mine = True
                placed_mines += 1

    def right_click_handler(self, event):
        """
        Handles the right-click event on a square button.
        Toggles the flag on the square.

        Args:
            event: The right-click event object

        Returns:
            None
        """
        btn = event.widget
        row = btn.grid_info()["row"]
        col = btn.grid_info()["column"]

        square = self.grid[row][col]
        square.toggle_flag()
        if square.flag:
            self.flags += 1
        else:
            self.flags -= 1

    def left_click_handler(self, event):
        """
        Event handler for left-click on a square button.
        Reveals the square and performs necessary actions based on the square's properties.

        Args:
            event: The event object representing the left-click event.

        Returns:
            None
        """
        btn = event.widget
        row = btn.grid_info()["row"]
        col = btn.grid_info()["column"]

        square = self.grid[row][col]

        if self.first_click:
            self.first_click = False
            self.first_move(row, col)
            self.place_mines()
            self.set_adjacent_mines()

        if square.mine:
            self.reveal_mines()
            self.display_game_over()
        else:
            self.flood_fill(row, col)
            self.check_game_won()

    def reveal_mines(self):
        """
        Reveals all the mines on the game board.

        Args:
            None

        Returns:
            None
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j].mine:
                    self.grid[i][j].reveal_mine()

    def first_move(self, row, col):
        """
        Determines the adjacent cells of the first move in the Minesweeper game.

        Args:
            row (int): The row index of the first move.
            col (int): The column index of the first move.

        Returns:
            None

        """
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                adjacent_row = row + row_offset
                adjacent_col = col + col_offset
                if self.in_bounds(adjacent_row, adjacent_col):
                    self.first_click_adjacents.append((adjacent_row, adjacent_col))

    def in_bounds(self, row, col):
        """
        Check if the given coordinates (row, col) are within the bounds of the game grid.

        Args:
            row (int): The row-coordinate.
            col (int): The col-coordinate.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols

    def count_adjacent_mines(self, row, col):
        """
        Calculates the number of adjacent mines to a given cell.

        Args:
            row (int): The row-coordinate.
            col (int): The col-coordinate.

        Returns:
            int: The total number of adjacent mines.
        """
        total_mines = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                adjacent_row = row + row_offset
                adjacent_col = col + col_offset
                if (
                    self.in_bounds(adjacent_row, adjacent_col)
                    and self.grid[adjacent_row][adjacent_col].mine
                ):
                    total_mines += 1
        return total_mines

    def set_adjacent_mines(self):
        """
        Sets the number of adjacent mines for each cell in the grid.

        Args:
            None

        Returns:
            None
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.grid[i][j].mine:
                    self.grid[i][j].adjacent_mines = self.count_adjacent_mines(i, j)

    def flood_fill(self, row, col):
        """
        Recursively reveals adjacent squares until reaching squares with adjacent mines.

        Args:
            row (int): The row index of the square to start the flood fill from.
            col (int): The column index of the square to start the flood fill from.

        Returns:
            None
        """
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                adjacent_row = row + row_offset
                adjacent_col = col + col_offset

                if self.in_bounds(adjacent_row, adjacent_col):
                    if (
                        not self.grid[adjacent_row][adjacent_col].revealed
                        and not self.grid[adjacent_row][adjacent_col].mine
                    ):
                        self.grid[adjacent_row][adjacent_col].reveal_square()

                        if self.grid[adjacent_row][adjacent_col].adjacent_mines == 0:
                            self.flood_fill(adjacent_row, adjacent_col)

    def display_game_over(self):
        """
        Unbinds the left and right mouse button events for all squares in the grid and displays a game over message box.
        Args:
            None

        Returns:
            None
        """
        for all in self.grid:
            for square in all:
                square.btn_object.unbind("<Button-1>")
                square.btn_object.unbind("<Button-3>")
        messagebox.showinfo("Game over", "Game over")

    def check_game_won(self):
        """
        Checks if the game has been won by counting the number of revealed squares.
        If the number of revealed squares is equal to the total number of squares minus the number of mines,
        the game is considered won.

        Args:
            None

        Returns:
            None
        """
        total_revealed = 0
        for all in self.grid:
            for square in all:
                if square.revealed:
                    total_revealed += 1
        if total_revealed == self.rows * self.cols - self.mines:
            square.btn_object.unbind("<Button-1>")
            square.btn_object.unbind("<Button-3>")
            messagebox.showinfo("Game Won", "Game Won")
