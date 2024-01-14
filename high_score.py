import tkinter as tk
from tkinter import messagebox

HIGH_SCORE_FILE = "highscores.txt"


class HighScore:
    def __init__(self, name, size, mines, time):
        self.name = name
        self.size = size
        self.mines = mines
        self.time = time


def read_high_scores_from_file(file_name):
    highscores = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    name, size, mines, time = data
                    rows, cols = map(int, size.split("x"))
                    highscores.append(
                        HighScore(name, (rows, cols), int(mines), int(time))
                    )
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return highscores


def write_high_scores_to_file(file_name, highscores):
    try:
        with open(file_name, "w") as file:
            for highscore in highscores:
                size = f"{highscore.size[0]}x{highscore.size[1]}"
                file.write(
                    f"{highscore.name},{size},{highscore.mines},{highscore.time}\n"
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
