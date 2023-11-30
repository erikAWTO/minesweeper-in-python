import tkinter as tk
from tkinter import messagebox
from operator import attrgetter

class HighScore:
    def __init__(self, name, size, time):
        self.name = name
        self.size = size
        self.time = time

def read_highscores_from_file(file_name):
    highscores = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    name, size, time = data
                    rows, cols = map(int, size.split('x'))
                    highscores.append(HighScore(name, (rows, cols), float(time)))
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return highscores

def write_highscores_to_file(file_name, highscores):
    try:
        with open(file_name, 'w') as file:
            for highscore in highscores:
                size = f"{highscore.size[0]}x{highscore.size[1]}"
                file.write(f"{highscore.name},{size},{highscore.time}\n")
    except IOError:
        print(f"Error writing to '{file_name}'.")

def sort_highscores(scores):
    scores.sort(key=lambda x: (-x.size[0], -x.size[1], x.time))

def show_highscores():
    sorted_scores = read_highscores_from_file('highscores.txt')
    sort_highscores(sorted_scores)

    top = tk.Toplevel(root)
    top.title("High Scores")
    
    for i, score in enumerate(sorted_scores, start=1):
        label = tk.Label(top, text=f"{i}. Name: {score.name}, Grid Size: {score.size[0]}x{score.size[1]}, Time: {score.time}")
        label.pack()

root = tk.Tk()
root.title("High Scores")

button = tk.Button(root, text="Show High Scores", command=show_highscores)
button.pack()

root.mainloop()
