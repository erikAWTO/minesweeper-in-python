import random
import utils
from tkinter import *
from square import *


class Game:
    """A mine field containing a list of Square objects and metods for it."""

    def __init__(self, frame, rows, cols, mines):
        self.__rows = rows
        self.__cols = cols
        self.__mines = mines
        self.__flags = 0
        self.revealed_squares = 0
        self.is_won = False

        # make a list of lists of squares
        self.board = [[Square() for _ in range(cols)] for _ in range(rows)]
        self.frame = frame
        self.__generate_buttons()

    def __generate_buttons(self):
        # Create a frame to hold the buttons
        button_frame = Frame(
            self.frame, bg="black"
        )  # Set background color for button frame

        for i in range(self.__rows):
            for j in range(self.__cols):
                square = Square(row=i, col=j)
                self.board[i][j] = square
                square.create_btn_object(button_frame)
                square.btn_object.config(width=8, height=3)  # Set button dimensions
                square.btn_object.grid(row=i, column=j, padx=0, pady=0)

        # Place the button frame in the center of the game_frame
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

    def place_mines(self, first_click_row, first_click_col):
        placed_mines = 0
        while placed_mines < self.__mines:
            row = random.randrange(0, self.__rows)
            col = random.randrange(0, self.__cols)
            if not self.board[row][col].is_mine() and not (
                row == first_click_row and col == first_click_col
            ):
                self.board[row][col].set_mine(True)
                placed_mines += 1

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


root = Tk()
root.title("Minröj")
root.configure()
root.geometry(f"{utils.SCREEN_WIDTH}x{utils.SCREEN_HEIGHT}")

top_frame = Frame(
    root,
    bg="#2d2d30",
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(15),
)
top_frame.place(x=utils.screen_width_prcnt(15), y=0)

mine_label = Label(
    top_frame, text="Minor: 0", font=("Helvetica", 14), fg="#007acc", bg="#2d2d30"
)
mine_label.place(relx=0.5, rely=0.25, anchor="center")
flag_label = Label(
    top_frame, text="Flaggor: 0", font=("Helvetica", 14), fg="#007acc", bg="#2d2d30"
)
flag_label.place(relx=0.5, rely=0.5, anchor="center")
time_label = Label(
    top_frame, text="Tid: 0", font=("Helvetica", 14), fg="#007acc", bg="#2d2d30"
)
time_label.place(relx=0.5, rely=0.75, anchor="center")

left_frame = Frame(
    root,
    bg="#252526",
    width=utils.screen_width_prcnt(15),
    height=utils.screen_height_prcnt(100),
)
left_frame.place(x=0, y=0)

main_label = Label(
    left_frame, text="MINRÖJ", font=("Helvetica", 28), fg="#007acc", bg="#252526"
)
main_label.place(relx=0.5, rely=0.085, anchor="center")

game_frame = Frame(
    root,
    bg="#1e1e1e",
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(85),
)
game_frame.place(x=utils.screen_width_prcnt(15), y=utils.screen_height_prcnt(15))

game = Game(game_frame, 12, 12, 64)
game.place_mines(0, 0)

root.mainloop()
