from tkinter import *

# Define constants for the minimum and maximum values for the grid size and number of mines
MIN_ROWS = 2
MIN_COLUMNS = 2
MIN_MINES = 2
MAX_ROWS = 12
MAX_COLUMNS = 12
MAX_MINES = 20

root = Tk()  # Define the root variable

# Define variables for the default values of the input fields
DEFAULT_ROWS = StringVar(root)
DEFAULT_MINES = StringVar(root)
DEFAULT_COLUMNS = StringVar(root)
DEFAULT_ROWS.set(8)
DEFAULT_COLUMNS.set(8)
DEFAULT_MINES.set(10)


def start_game():
    # Retrieve values from the input fields
    rows = int(rows_spinbox.get())
    cols = int(cols_spinbox.get())
    mines = int(mines_spinbox.get())

    # Here, you can start the Minesweeper game with the chosen parameters
    # For demonstration purposes, print the selected values
    print(f"Starting Minesweeper with {rows} rows, {cols} columns, and {mines} mines.")
    root.destroy()
    # open_game_window()


def show_high_scores():
    # Display high scores or implement the functionality to show high scores
    # For now, just empty
    # Create a new toplevel window (popup)
    message_window = Toplevel(root)
    message_window.title("Message")

    # Message label
    message_label = Label(message_window, text="High Scores")
    message_label.pack(padx=20, pady=10)

    # Close button
    close_button = Button(message_window, text="Close", command=message_window.destroy)
    close_button.pack(pady=10)

    # Set the window size
    message_window.geometry("300x300")


# Function to validate input as integers
def validate_integer_input(action, value_if_allowed):
    if action == "1":  # action=1, text is being inserted
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return True


def validate_input(action, value_if_allowed):
    # Check if the input is empty and mines are fewer than squares
    pass


# Create a validation command for integer input
integer_validation = root.register(validate_integer_input)

# Style the main window
root.title("Minröj")
root.geometry("300x300")

# Create labels and spinboxes for grid size and mines
title_label = Label(root, text="MINRÖJ", font=("Arial", 28))
title_label.pack()

rows_label = Label(root, text="Rader:")
rows_label.pack()
rows_spinbox = Spinbox(
    root,
    font=("Arial", 14),
    from_=MIN_ROWS,
    to=MAX_ROWS,
    textvariable=DEFAULT_ROWS,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
rows_spinbox.pack()

cols_label = Label(root, text="Kolumner:")
cols_label.pack()
cols_spinbox = Spinbox(
    root,
    font=("Arial", 14),
    from_=MIN_COLUMNS,
    to=MAX_COLUMNS,
    width=5,
    textvariable=DEFAULT_COLUMNS,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
cols_spinbox.pack()

mines_label = Label(root, text="Minor:")
mines_label.pack()
mines_spinbox = Spinbox(
    root,
    font=("Arial", 14),
    from_=MIN_MINES,
    to=MAX_MINES,
    textvariable=DEFAULT_MINES,
    validate="key",
    validatecommand=(integer_validation, "%d", "%P"),
)
mines_spinbox.pack(pady=(0, 10))

# Create buttons for starting the game and showing high scores
start_button = Button(root, width=20, text="Start Game", command=start_game)
start_button.pack(pady=(0, 10))

high_scores_button = Button(
    root, width=20, text="Show High Scores", command=show_high_scores
)
high_scores_button.pack()

root.mainloop()
