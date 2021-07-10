import tkinter

class play_chess_:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.pieces_dic = {}

        self.create_board()
    
    def create_board(self):
        for x in range(8):
            for y in range(8):
                self.pieces_dic[(x, y)] = tkinter.Canvas(self.main_window, height=70, width=70).grid(row=y, column=x)

game = play_chess_()

    