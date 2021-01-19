import tkinter


class pawn:
    def __init__(self, master, color, coord, cell_list):
        self.pawn = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.pawn.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackp.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whitep.gif')
            master.img = self.img

        self.pawn.create_image((38, 38), image=self.img)


class bishop:
    def __init__(self, master, color, coord, cell_list):
        self.bishop = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.bishop.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackb.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiteb.gif')
            master.img = self.img

        self.bishop.create_image((38, 38), image=self.img)


class knight:
    def __init__(self, master, color, coord, cell_list):
        self.knight = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.knight.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackn.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiten.gif')
            master.img = self.img

        self.knight.create_image((38, 38), image=self.img)


class rook:
    def __init__(self, master, color, coord, cell_list):
        self.rook = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.rook.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackr.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiter.gif')
            master.img = self.img

        self.rook.create_image((38, 38), image=self.img)


class king:
    def __init__(self, master, color, coord, cell_list):
        self.king = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.king.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackk.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whitek.gif')
            master.img = self.img

        self.king.create_image((38, 38), image=self.img)


class queen:
    def __init__(self, master, color, coord, cell_list):
        self.queen = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.queen.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackq.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiteq.gif')
            master.img = self.img

        self.queen.create_image((38, 38), image=self.img)


class board:
    def __init__(self, window):
        self.windowh = window

        self.cells = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = tkinter.Canvas(self.windowh, bg='green', height=70, width=70)
                    self.cells[(row, column)].grid(row=row, column=column)
                else:
                    self.cells[(row, column)] = tkinter.Canvas(self.windowh, height=70, width=70)
                    self.cells[(row, column)].grid(row=row, column=column)
                counter += 1
            counter -= 1

    def get_cells(self):
        return self.cells


class play_chess:
    def __init__(self):
        self.window = tkinter.Tk()
        self.board = board(self.window)

        self.board_cells = self.board.get_cells()

        self.window.title("Chess")

        self.black_pieces = {}
        self.white_pieces = {}

        self.create_pieces()

        self.window.mainloop()

    def create_pieces(self):
        for item in range(8):
            self.black_pieces[(1, item)] = pawn(self.window, 'B', (1, item), self.board_cells)
            self.white_pieces[(6, item)] = pawn(self.window, 'W', (6, item), self.board_cells)

        self.black_pieces[(0, 2)] = bishop(self.window, 'B', (0, 2), self.board_cells)
        self.black_pieces[(0, 5)] = bishop(self.window, 'B', (0, 5), self.board_cells)
        self.white_pieces[(7, 2)] = bishop(self.window, 'W', (7, 2), self.board_cells)
        self.white_pieces[(7, 5)] = bishop(self.window, 'W', (7, 5), self.board_cells)

        self.black_pieces[(0, 1)] = knight(self.window, 'B', (0, 1), self.board_cells)
        self.black_pieces[(0, 6)] = knight(self.window, 'B', (0, 6), self.board_cells)
        self.white_pieces[(7, 1)] = knight(self.window, 'W', (7, 1), self.board_cells)
        self.white_pieces[(7, 6)] = knight(self.window, 'W', (7, 6), self.board_cells)

        self.black_pieces[(0, 0)] = rook(self.window, 'B', (0, 0), self.board_cells)
        self.black_pieces[(0, 7)] = rook(self.window, 'B', (0, 7), self.board_cells)
        self.white_pieces[(7, 0)] = rook(self.window, 'W', (7, 0), self.board_cells)
        self.white_pieces[(7, 7)] = rook(self.window, 'W', (7, 7), self.board_cells)

        self.black_pieces[(0, 4)] = king(self.window, 'B', (0, 4), self.board_cells)
        self.white_pieces[(7, 4)] = king(self.window, 'W', (7, 4), self.board_cells)

        self.black_pieces[(0, 3)] = queen(self.window, 'B', (0, 3), self.board_cells)
        self.white_pieces[(7, 3)] = queen(self.window, 'W', (7, 3), self.board_cells)

