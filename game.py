import random
import utils
from tkinter import *
from square import *


class Game:
    """A mine field containing a list of Square objects and metods for it."""

    def __init__(self, parent, rows, cols, mines):
        # make a list of lists of squares
        self.__board = []
        self.__rows = rows
        self.__cols = cols
        self.__mines = mines
        self.__flags = 0
        self.__revealed_squares = 0
        self.__game_won = False

    def __str__(self):
        """Returns a string representation of the mine field."""
        pass

    def place_mines(self):
        """Places the mines on the board."""
        pass

    def is_game_won(self):
        """Checks if the game is won."""
        pass

    def flood_fill(self):
        """Flood fills the board."""
        pass


# Function to validate input as integers
def validate_integer_input(action, value_if_allowed):
    if action == "1":  # action=1, text is being inserted
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return True


game_window = Tk()
game_window.title("Minröj")
game_window.configure(bg="grey")
game_window.geometry(f"{utils.SCREEN_WIDTH}x{utils.SCREEN_HEIGHT}")

top_frame = Frame(
    game_window,
    bg="red",
    width=utils.SCREEN_WIDTH,
    height=utils.screen_height_prcnt(15),
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    game_window,
    bg="blue",
    width=utils.screen_width_prcnt(15),
    height=utils.screen_height_prcnt(85)
)
left_frame.place(x=0, y=utils.screen_height_prcnt(15))


game_frame = Frame(
    game_window,
    bg="green",
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(85),
)
game_frame.place(x=utils.screen_width_prcnt(15), y=utils.screen_height_prcnt(15))

for rows in range(utils.DEFAULT_ROWS):
    for cols in range(utils.DEFAULT_COLUMNS):
        square = Square(row=rows, column=cols)
        square.create_btn_object(game_frame)
        square.btn_object.grid(row=rows, column=cols)

game_window.mainloop()

