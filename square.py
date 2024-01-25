from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html
from tkmacosx import Button  # 3rd party, macos fix

import utils  # Local module


class Square:
    def __init__(
        self, row=0, col=0, mine=False, flag=False, revealed=False, adjacent_mines=0
    ):
        """
        Initialize a Square object.

        Args:
            row (int): The row index of the square.
            col (int): The column index of the square.
            mine (bool): Whether the square contains a mine.
            flag (bool): Whether the square is flagged.
            revealed (bool): Whether the square is revealed.
            adjacent_mines (int): The number of adjacent mines.

        Returns:
            None
        """
        self.row = row
        self.col = col
        self.mine = mine
        self.flag = flag
        self.revealed = revealed
        self.adjacent_mines = adjacent_mines
        self.btn_object = None

    def create_btn_object(self, parent):
        """
        Create a button object with specified properties and bind left and right click handlers.

        Args:
            parent: The parent widget to which the button object will be added.

        Returns:
            None
        """
        btn = Button(
            parent,
            borderless=1,
            fg="white",
            bg=utils.GREY2,
            font="Helvetica 12 bold",
        )
        self.btn_object = btn

    def reveal_mine(self):
        """
        Reveals the mine in the square.

        Returns:
            None
        """
        self.revealed = True
        self.btn_object["bg"] = "red"
        self.btn_object.unbind("<Button-1>")
        self.btn_object.unbind("<Button-3>")

    def reveal_square(self):
        """
        Reveals the square.

        Returns:
            None
        """
        self.revealed = True
        self.btn_object["bg"] = utils.GREY1

        if self.adjacent_mines > 0:
            self.btn_object["text"] = self.adjacent_mines

        self.btn_object.unbind("<Button-1>")
        self.btn_object.unbind("<Button-3>")

    def toggle_flag(self):
        """
        Toggles the flag on the square.

        Returns:
            None
        """
        if not self.revealed:
            if self.flag:
                self.flag = False
                self.btn_object["bg"] = utils.GREY2
            elif not self.flag:
                self.flag = True
                self.btn_object["bg"] = "yellow"
