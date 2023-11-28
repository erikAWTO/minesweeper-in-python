from tkinter import *
from tkinter.font import Font


def start_game():
    # Retrieve values from the input fields
    rows = int(rows_spinbox.get())
    cols = int(cols_spinbox.get())
    mines = int(mines_spinbox.get())

    # Here, you can start the Minesweeper game with the chosen parameters
    # For demonstration purposes, print the selected values
    print(f"Starting Minesweeper with {rows} rows, {cols} columns, and {mines} mines.")


def show_high_scores():
    # Display high scores or implement the functionality to show high scoresArialenty
    # For now, just print a message
    print("Showing High Scores")


# Create the main window
root = Tk()
root.title("Minröj")
root.geometry("300x300")

# Set the default value for SpinBoxes
row_value = StringVar(root)
row_value.set("8")
column_value = StringVar(root)
column_value.set("8")
mine_value = StringVar(root)
mine_value.set("10")

# Create labels and spinboxes for grid size and mines
title_label = Label(root, text="MINRÖJ", font=("Arial", 28))
title_label.pack()

rows_label = Label(root, text="Rader:")
rows_label.pack()
rows_spinbox = Spinbox(root, font=("Arial", 14), from_=2, to=12, textvariable=row_value)
rows_spinbox.pack()

cols_label = Label(root, text="Kolumner:")
cols_label.pack()
cols_spinbox = Spinbox(
    root, font=("Arial", 14), from_=2, to=12, textvariable=column_value
)
cols_spinbox.pack()

mines_label = Label(root, text="Minor:")
mines_label.pack()
mines_spinbox = Spinbox(root, font=("Arial", 14), from_=2, to=12, textvariable=mine_value)
mines_spinbox.pack(pady=(0, 10))

# Create buttons for starting the game and showing high scores
start_button = Button(root, width=20, text="Start Game", command=start_game)
start_button.pack(pady=(0, 10))

high_scores_button = Button(
    root, width=20, text="Show High Scores", command=show_high_scores
)
high_scores_button.pack()

root.mainloop()