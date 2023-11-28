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