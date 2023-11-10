import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.mine_label = tk.Label(self.frame, text="Mines: {}".format(self.mines))
        self.mine_label.pack()

        self.grid_frame = tk.Frame(self.frame)
        self.grid_frame.pack()

        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.grid_frame, width=2, height=1, command=lambda row=row, col=col: self.click(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def reset(self):
        self.game_over = False
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines()
        self.update_buttons()

    def place_mines(self):
        mines = 0
        while mines < self.mines:
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines += 1

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != -1:
                    count = 0
                    for r in range(row-1, row+2):
                        for c in range(col-1, col+2):
                            if r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.board[r][c] == -1:
                                count += 1
                    self.board[row][col] = count

    def update_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="*", state="disabled")
                elif self.board[row][col] == 0:
                    self.buttons[row][col].config(text="", state="normal")
                else:
                    self.buttons[row][col].config(text=str(self.board[row][col]), state="disabled")

    def click(self, row, col):
        if self.game_over:
            return

        if self.board[row][col] == -1:
            self.buttons[row][col].config(text="*", state="disabled")
            self.game_over = True
            tk.messagebox.showinfo("Game Over", "You lose!")
        elif self.board[row][col] == 0:
            self.clear_zeros(row, col)
        else:
            self.buttons[row][col].config(text=str(self.board[row][col]), state="disabled")

        if self.check_win():
            self.game_over = True
            tk.Message.bbox.showinfo("Game Over", "You win!")

    def clear_zeros(self, row, col):
        if self.board[row][col] != 0 or self.buttons[row][col]["state"] == "disabled":
            return

        self.buttons[row][col].config(text="", state="disabled")

        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r >= 0 and r < self.rows and c >= 0 and c < self.cols:
                    self.clear_zeros(r, c)

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != -1 and self.buttons[row][col]["state"] != "disabled":
                    return False
        return True

root = tk.Tk()
root.title("Minesweeper")
game = Minesweeper(root, 10, 10, 10)
root.mainloop()
