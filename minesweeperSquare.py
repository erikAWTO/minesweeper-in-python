class Square:
    def __init__(self, mine, flag, revealed, adjacent_mines):
        self.__mine = mine
        self.__flag = flag
        self.__revealed = revealed
        self.__adjacent_mines = adjacent_mines

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