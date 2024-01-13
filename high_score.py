import tkinter as tk
from tkinter import messagebox


class HighScore:
    def __init__(self, name, size, time):
        self.name = name
        self.size = size
        self.time = time


def read_high_scores_from_file(file_name):
    highscores = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    name, size, time = data
                    rows, cols = map(int, size.split("x"))
                    highscores.append(HighScore(name, (rows, cols), float(time)))
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return highscores


def write_high_scores_to_file(file_name, highscores):
    try:
        with open(file_name, "w") as file:
            for highscore in highscores:
                size = f"{highscore.size[0]}x{highscore.size[1]}"
                file.write(f"{highscore.name},{size},{highscore.time}\n")
    except IOError:
        print(f"Error writing to '{file_name}'.")


def sort_high_scores(scores):
    scores.sort(key=lambda x: (-x.size[0], -x.size[1], x.time))


def show_high_scores(root):
    sorted_scores = read_high_scores_from_file("highscores.txt")
    sort_high_scores(sorted_scores)

    top = tk.Toplevel(root)
    top.title("High Scores")

    for i, score in enumerate(sorted_scores, start=1):
        label = tk.Label(
            top,
            text=f"{i}. Spelare: {score.name}, Storlek: {score.size[0]}x{score.size[1]}, Tid: {score.time}",
        )
        label.pack()
