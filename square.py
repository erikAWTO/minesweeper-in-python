import random
from tkinter import *


class Square:
    def __init__(
        self, row=0, col=0, mine=False, flag=False, revealed=False, adjacent_mines=0
    ):
        self.__row = row
        self.__col = col
        self.__mine = mine
        self.__flag = flag
        self.__revealed = revealed
        self.__adjacent_mines = adjacent_mines
        self.btn_object = None

    def create_btn_object(self, parent):
        btn = Button(parent, width=6, height=2, borderwidth=1, fg="#007acc", bg="#252526")
        btn.bind("<Button-1>", self.btn_left_click)
        btn.bind("<Button-3>", self.btn_right_click)
        self.btn_object = btn

    def btn_left_click(self, event):
        if self.is_mine():
            self.reveal_mine()
        else:
            self.reveal_square()

    def btn_right_click(self, event):
        print(event)
        print("Right click")
        self.set_flag()
        self.btn_object["text"] = "P"

    def reveal_mine(self):
        self.btn_object["bg"] = "red"

    def reveal_square(self):
        self.btn_object["bg"] = "#3e3e42"

    def set_mine(self, mine=True):
        self.__mine = True

    def set_flag(self):
        self.__flag = True

    def set_revealed(self):
        self.__revealed = True

    def set_adjacent_mines(self, adjacent_mines):
        self.__adjacent_mines = adjacent_mines

    def is_mine(self):
        return self.__mine

    def is_flag(self):
        return self.__flag

    def is_revealed(self):
        return self.__revealed

    def get_adjacent_mines(self):
        return self.__adjacent_mines

    def reset(self):
        self.__mine = False
        self.__flag = False
        self.__revealed = False
        self.__adjacent_mines = 0
