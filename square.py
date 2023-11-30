import random
from tkinter import *


class Square:
    def __init__(
        self, row=0, column=0, mine=False, flag=False, revealed=False, adjacent_mines=0
    ):
        self.__row = row
        self.__column = column
        self.__mine = mine
        self.__flag = flag
        self.__revealed = revealed
        self.__adjacent_mines = adjacent_mines
        self.btn_object = None

    def create_btn_object(self, parent):
        btn = Button(parent, text=f"{self.__row},{self.__column}", width=12, height=4)
        btn.bind("<Button-1>", self.btn_left_click)
        btn.bind("<Button-3>", self.btn_right_click)
        self.btn_object = btn

    def btn_left_click(self, event):
        print(event)
        print("Left click")
        self.set_revealed()
        self.btn_object["text"] = "X"

    def btn_right_click(self, event):
        print(event)
        print("Right click")
        self.set_flag()
        self.btn_object["text"] = "P"

    def __str__(self):
        if self.__revealed:
            if self.__mine:
                return "M"
            else:
                return str(self.__adjacent_mines)
        elif self.__flag:
            return "F"
        else:
            return " "

    def set_mine(self):
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
