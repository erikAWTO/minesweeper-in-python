import utils
from tkinter import *


class Square:
    """
    Represents a square in the Minesweeper board.

    Attributes:
        row (int): The row index of the square.
        col (int): The column index of the square.
        mine (bool): Indicates if the square contains a mine.
        flag (bool): Indicates if the square has been flagged.
        revealed (bool): Indicates if the square has been revealed.
        adjacent_mines (int): The number of adjacent squares containing mines.
        btn_object (Button): The button object associated with the square.

    Methods:
        create_btn_object(parent): Creates a button object for the square.
        left_click_handler(event): Handles left-click event on the square.
        right_click_handler(event): Handles right-click event on the square.
        reveal_mine(): Reveals the mine in the square.
        reveal_square(): Reveals the square.
    """

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
            width=3,
            height=1,
            borderwidth=1,
            fg="white",
            bg=utils.GREY2,
            font="Helvetica 12 bold",
        )
        btn.bind("<Button-1>", self.left_click_handler)
        btn.bind("<Button-3>", self.right_click_handler)
        self.btn_object = btn

    def left_click_handler(self, event):
        """
        Handles left-click event on the square.

        If the square contains a mine, it reveals the mine.
        Otherwise, it reveals the square.

        Args:
            event: The event object triggered by the left-click.

        Returns:
            None
        """

        if self.mine == True:
            self.reveal_mine()
        else:
            self.reveal_square()

    def right_click_handler(self, event):
        """
        Handles right-click event on the square.

        Flags the square with a 'P' character on the button.

        Args:
            event: The event object triggered by the right-click.

        Returns:
            None
        """
        if not self.revealed:
            if self.flag == True:
                self.flag = False
                self.btn_object["bg"] = utils.GREY2
            elif self.flag == False:
                self.flag = True
                self.btn_object["bg"] = "yellow"

    def reveal_mine(self):
        """
        Reveals the mine in the square.

        Changes the button background color to red to indicate a revealed mine.

        Returns:
            None
        """
        self.btn_object.unbind("<Button-1>")
        self.btn_object.unbind("<Button-3>")

        self.revealed = True
        self.btn_object["bg"] = "red"

    def reveal_square(self):
        """
        Reveals the square.

        Changes the button background color and text to show the revealed square.

        If the square has adjacent mines, it displays the number of adjacent mines.

        Returns:
            None
        """
        self.btn_object.unbind("<Button-1>")
        self.btn_object.unbind("<Button-3>")

        self.revealed = True
        self.btn_object["bg"] = utils.GREY0
        if not self.adjacent_mines == 0:
            self.btn_object["text"] = self.adjacent_mines
