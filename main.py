import time  # Built-in module: https://docs.python.org/3/library/time.html

from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html
from tkinter import (
    messagebox,
)  # 3rd party: https://docs.python.org/3/library/tkinter.messagebox.html

import utils  # Local module
import high_score  # Local module
from board import Board  # Local module

current_game = None


def start_new_game():
    """
    Starts a new game.
    Args:
        None
    Returns:
        None
    """
    global current_game

    # Retrieve values from Spinboxes
    rows = int(rows_spinbox.get())
    cols = int(cols_spinbox.get())
    mines = int(mines_spinbox.get())
    if Board.validate_board_size(rows, cols, mines):
        current_game = Board(game_frame, rows, cols, mines)
    else:
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
    info_frame = Toplevel(left_frame)
    info_frame.title("Info")
    info_text = Label(
        info_frame,
        text=f"Min rader/kolumner - {utils.MIN_ROWS}x{utils.MIN_COLUMNS} \nMax rader/kolumner - {utils.MAX_ROWS}x{utils.MAX_COLUMNS}\nMin minor - {utils.MIN_MINES} \nMax minor - 1/4 av totala rutor\n\nStarta spelet och klicka på en valfri ruta (vänsterklick).\nSiffrorna indikerar hur många minor som omger den aktuella rutan. Använd logiskt tänkande för att undvika minor.\nAnvänd högerklick för att markera misstänkta rutor med flaggor\nFortsätt avslöja och flagga rutor tills alla tomma rutor är avslöjade utan att stöta på en mina.\nOm du träffar på en mina, är spelet över.\nNär du framgångsrikt har avslöjat alla tomma rutor, har du vunnit spelet.",
    )
    info_text.pack(padx=20, pady=10)


def update_time_label():
    """
    Updates the time label.
    Args:
        None
    Returns:
        None
    """
    root.after(1000, update_time_label)

    if current_game is None or current_game.game_over or current_game.first_click:
        return

    current_time = int(time.time() - current_game.start_time)
    current_time_label.config(text=str(current_time))


root = Tk()
root.title("Minröj")
root.geometry(f"{utils.SCREEN_WIDTH}x{utils.SCREEN_HEIGHT}")
root.resizable(False, False)

validate_integer = root.register(utils.validate_integer_input)

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

Label(
    top_frame, text="Tid", font=("Helvetica", 14), fg=utils.BLUE, bg=utils.GREY1
).place(relx=0.5, rely=0.4, anchor="center")

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
    validate="key",  # On user input
    validatecommand=(
        validate_integer,
        "%d",
        "%P",
    ),  # %d = type of action, %P = value of the entry if the edit is allowed
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
    validate="key",  # On user input
    validatecommand=(
        validate_integer,
        "%d",
        "%P",
    ),  # %d = type of action, %P = value of the entry if the edit is allowed
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
    validate="key",  # On user input
    validatecommand=(
        validate_integer,
        "%d",
        "%P",
    ),  # %d = type of action, %P = value of the entry if the edit is allowed
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

root.after(1000, update_time_label)  # Update time label every second
root.mainloop()
