from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html
from tkinter import (
    messagebox,
)  # 3rd party: https://docs.python.org/3/library/tkinter.messagebox.html

import utils  # Local module
import high_score  # Local module
from board import Board  # Local module


def start_new_game():
    """
    Starts a new game.
    Args:
        None
    Returns:
        None
    """
    # Retrieve values from Spinboxes
    rows = int(rows_spinbox.get())
    cols = int(cols_spinbox.get())
    mines = int(mines_spinbox.get())
    if utils.validate_board_size(rows, cols, mines):
        game = Board(game_frame, rows, cols, mines)
    else:
        invalid_board_size()


def invalid_board_size():
    """
    Shows a message box if the board size is invalid.
    Args:
        None
    Returns:
        None
    """
    messagebox.showerror(
        "Invalid board size",
        f"Min rader/kolumner - {utils.MIN_ROWS}x{utils.MIN_COLUMNS} \nMax rader/kolumner - {utils.MAX_ROWS}x{utils.MAX_COLUMNS}\nMin minor - {utils.MIN_MINES} \nMax minor - 1/4 av totala rutor",
    )


def show_info():
    """
    Shows information about the game.
    Args:
        None
    Returns:
        None
    """
    info_frame = Toplevel(left_frame, width=300, height=100)
    info_frame.title("Info")
    info_text = Label(
        info_frame,
        text=f"Min rader/kolumner - {utils.MIN_ROWS}x{utils.MIN_COLUMNS} \nMax rader/kolumner - {utils.MAX_ROWS}x{utils.MAX_COLUMNS}\nMin minor - {utils.MIN_MINES} \nMax minor - 1/4 av totala rutor",
    )
    info_text.place(relx=0.5, rely=0.5, anchor="center")


root = Tk()
root.title("Minröj")
root.geometry(f"{utils.SCREEN_WIDTH}x{utils.SCREEN_HEIGHT}")
root.resizable(False, False)

integer_validation = root.register(utils.validate_integer_input)
board_size_validation = root.register(utils.validate_board_size)

# Set default values for rows and columns
DEFAULT_ROWS = StringVar(root, utils.DEFAULT_ROWS)
DEFAULT_COLUMNS = StringVar(root, utils.DEFAULT_COLUMNS)
DEFAULT_MINES = StringVar(root, utils.DEFAULT_MINES)

# Top frame
top_frame = Frame(
    root,
    bg=utils.GREY1,
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(15),
)
top_frame.place(x=utils.screen_width_prcnt(15), y=0)

time_label = Label(
    top_frame, text="Tid", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY1
)
time_label.place(relx=0.5, rely=0.4, anchor="center")

current_time_label = Label(
    top_frame, text="0", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY1
)
current_time_label.place(relx=0.5, rely=0.7, anchor="center")

# Left frame
left_frame = Frame(
    root,
    bg=utils.GREY2,
    width=utils.screen_width_prcnt(15),
    height=utils.screen_height_prcnt(100),
)
left_frame.place(x=0, y=0)

main_label = Label(
    left_frame, text="MINRÖJ", font=("Helvetica", 28), fg=utils.BLUE, bg=utils.GREY2
)
main_label.place(relx=0.5, rely=0.085, anchor="center")

rows_label = Label(
    left_frame, text="Rader", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY2
)
rows_label.place(relx=0.5, rely=0.3, anchor="center")
rows_spinbox = Spinbox(
    left_frame,
    font=("Helvetica", 14),
    width=10,
    from_=utils.MIN_ROWS,
    to=utils.MAX_ROWS,
    textvariable=DEFAULT_ROWS,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
rows_spinbox.place(relx=0.5, rely=0.35, anchor="center")

cols_label = Label(
    left_frame, text="Kolumner", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY2
)
cols_label.place(relx=0.5, rely=0.45, anchor="center")
cols_spinbox = Spinbox(
    left_frame,
    font=("Helvetica", 14),
    width=10,
    from_=utils.MIN_COLUMNS,
    to=utils.MAX_COLUMNS,
    textvariable=DEFAULT_COLUMNS,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
cols_spinbox.place(relx=0.5, rely=0.50, anchor="center")

mines_label = Label(
    left_frame, text="Minor", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY2
)
mines_label.place(relx=0.5, rely=0.6, anchor="center")
mines_spinbox = Spinbox(
    left_frame,
    font=("Helvetica", 14),
    width=10,
    from_=utils.MIN_MINES,
    to=utils.MAX_MINES,
    textvariable=DEFAULT_MINES,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
mines_spinbox.place(relx=0.5, rely=0.65, anchor="center")

# Create buttons for starting the game, showing high scores and showing info
start_button = Button(
    left_frame, width=20, text="Starta", command=lambda: start_new_game()
)
start_button.place(relx=0.5, rely=0.85, anchor="center")


high_scores_button = Button(
    left_frame,
    width=20,
    text="High scores",
    command=lambda: high_score.show_high_scores(root),
)
high_scores_button.place(relx=0.5, rely=0.9, anchor="center")

info_button = Button(left_frame, width=20, text="Info", command=lambda: show_info())
info_button.place(relx=0.5, rely=0.95, anchor="center")

# Game frame
game_frame = Frame(
    root,
    bg=utils.GREY3,
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(85),
)
game_frame.place(x=utils.screen_width_prcnt(15), y=utils.screen_height_prcnt(15))

root.mainloop()
