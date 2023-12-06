"""The main file for the game. This file is responsible for creating the game window and starting the game."""
from tkinter import *  # 3rd party: https://docs.python.org/3/library/tkinter.html

import utils  # Local module
from game import Game  # Local module


def start_new_game():
    """
    Starts a new game.

    Returns:
         None
    """
    game = Game(game_frame, 12, 12, 48)


root = Tk()
root.title("Minröj")
root.geometry(f"{utils.SCREEN_WIDTH}x{utils.SCREEN_HEIGHT}")
root.resizable(False, False)

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
    bg=utils.GREY2,
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
    bg=utils.GREY3,
    width=utils.screen_width_prcnt(85),
    height=utils.screen_height_prcnt(85),
)
game_frame.place(x=utils.screen_width_prcnt(15), y=utils.screen_height_prcnt(15))

start_new_game()

root.mainloop()
