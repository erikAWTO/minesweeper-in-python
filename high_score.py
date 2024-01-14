import tkinter as tk
from tkinter import messagebox

HIGH_SCORE_FILE = "highscores.txt"


class HighScore:
    """
    Represents a high score.

    Attributes:
        name (str): The name of the player.
        size (tuple): The size of the board.
        mines (int): The number of mines.
        time (int): The time it took to complete the game.
    Returns:
        None
    """

    def __init__(self, name, size, mines, time):
        self.name = name
        self.size = size
        self.mines = mines
        self.time = time


def read_high_scores_from_file(file_name):
    """
    Reads the high scores from the given file.
    Args:
        file_name (str): The name of the file.

    Returns:
        list: List of HighScore objects.
    """
    high_scores = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    name, size, mines, time = data
                    rows, cols = map(int, size.split("x"))
                    high_scores.append(
                        HighScore(name, (rows, cols), int(mines), int(time))
                    )
                else:
                    print(f"Invalid format: {line}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return high_scores


def write_high_scores_to_file(file_name, high_scores):
    """
    Writes the high scores to the given file.
    Args:
        file_name (str): The name of the file.
        highscores (list): List of HighScore objects.
    Returns:
        None
    """
    try:
        with open(file_name, "w") as file:
            for high_score in high_scores:
                size = f"{high_score.size[0]}x{high_score.size[1]}"
                file.write(
                    f"{high_score.name},{size},{high_score.mines},{high_score.time}\n"
                )
    except IOError:
        print(f"Error writing to '{file_name}'.")


def sort_high_scores(scores):
    """
    Sorts the high scores. Based on size, time and name (alphabetical order).
    Args:
        scores (list): List of HighScore objects.
    Returns:
        None
    """
    scores.sort(key=lambda x: (-x.size[0], -x.size[1], -x.mines, x.time))


def show_high_scores(root):
    """
    Shows the high scores.
    Args:
        root (tk.Tk): The root window.
    Returns:
        None
    """
    sorted_scores = read_high_scores_from_file("highscores.txt")
    sort_high_scores(sorted_scores)

    top = tk.Toplevel(root)
    top.title("High Scores")

    tk.Label(top, text="Topp 10").pack(padx=20, pady=10)

    for i, score in enumerate(sorted_scores[:10], start=1):
        label = tk.Label(
            top,
            text=f"{i}. Spelare: {score.name}, Storlek: {score.size[0]}x{score.size[1]}, Minor: {score.mines}, Tid: {score.time}",
        )
        label.pack(padx=20, pady=10)
