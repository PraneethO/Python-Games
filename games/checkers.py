import tkinter


class pieces:
    def __init__(self):
        pass


class pawn:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.coord = coord
        self.bg_colors = bg_colors
        self.color = color
        self.cell_list = cell_list
        self.pawn = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.pawn.grid(row=(coord[0]), column=(coord[1]))
        self.pawn.bind("<Button-1>", self.highlight_update)

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackp.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whitep.gif')
            master.img = self.img

        self.pawn.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def highlight_update(self, event):
        if self.coord[0] == 1:
            # It can move 2 places
            if self.color == 'B':
                if self.cell_list[(self.coord[0] + 2, self.coord[1])].piece or (
                        self.cell_list[(self.coord[0] + 1, self.coord[1])].piece):
                    pass
                else:
                    for item in self.cell_list:
                        self.cell_list[item]['bg'] = self.cell_list[item].og_bg

                    for item in self.pieces_list:
                        self.pieces_list[item].change_bg(self.cell_list[item]['bg'])

                    if self.cell_list[(self.coord[0] + 2, self.coord[1])]['bg'] == '#B0FCC3':
                        self.cell_list[(self.coord[0] + 2, self.coord[1])]['bg'] = self.cell_list[
                            (self.coord[0] + 2, self.coord[1])].og_bg
                        self.cell_list[(self.coord[0] + 1, self.coord[1])]['bg'] = self.cell_list[
                            (self.coord[0] + 1, self.coord[1])].og_bg
                        self.pawn['bg'] = self.bg_colors[self.coord]
                    else:
                        self.cell_list[(self.coord[0] + 2, self.coord[1])].highlight()
                        self.cell_list[(self.coord[0] + 1, self.coord[1])].highlight()
                        self.pawn['bg'] = '#B0FCC3'

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.pawn['bg'] = color

    def move(self, coord):
        self.pawn.grid(row=coord[0], column=coord[1])

    def get_bg(self):
        return self.pawn['bg']


class bishop:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.bishop = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.bishop.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackb.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiteb.gif')
            master.img = self.img

        self.bishop.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.bishop['bg'] = color

    def get_bg(self):
        return self.bishop['bg']


class knight:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.knight = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.knight.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackn.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiten.gif')
            master.img = self.img

        self.knight.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.knight['bg'] = color

    def get_bg(self):
        return self.knight['bg']


class rook:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.rook = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.rook.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackr.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiter.gif')
            master.img = self.img

        self.rook.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.rook['bg'] = color

    def get_bg(self):
        return self.rook['bg']


class king:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.king = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.king.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackk.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whitek.gif')
            master.img = self.img

        self.king.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.king['bg'] = color

    def get_bg(self):
        return self.king['bg']


class queen:
    def __init__(self, master, color, coord, cell_list, bg_colors):
        self.queen = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.queen.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/blackq.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(master=master, file=r'img(GIF)/whiteq.gif')
            master.img = self.img

        self.queen.create_image((38, 38), image=self.img)
        self.pieces_list = []

    def get_pieces(self, pieces_list):
        self.pieces_list = pieces_list

    def change_bg(self, color):
        self.queen['bg'] = color

    def get_bg(self):
        return self.queen['bg']


class square(tkinter.Canvas):
    def __init__(self, master, row, column, piece=False, bg='green'):
        self.og_bg = bg
        tkinter.Canvas.__init__(self, master, bg=bg, height=70, width=70)
        self.grid(row=row, column=column)
        self.coord = (row, column)

        self.bind("<Button-2>", self.analyze)
        self.bind("<Button-1>", self.move)

        self.piece = piece
        self.black_pieces = []
        self.white_pieces = []

    def highlight(self):
        self['bg'] = '#B0FCC3'

    def analyze(self, event):
        if self['bg'] == 'brown1':
            self['bg'] = self.og_bg
        else:
            self['bg'] = 'brown1'

    def get_piece(self):
        return self.piece

    def move(self, event):
        if self['bg'] == '#B0FCC3':
            for item in self.black_pieces:
                if self.black_pieces[item].get_bg() == '#B0FCC3':
                    self.black_pieces[item].move(self.coord)

    def get_pieces(self, black_pieces, white_pieces):
        self.black_pieces = black_pieces
        self.white_pieces = white_pieces


class board:
    def __init__(self, window):
        self.windowh = window

        self.cells = {}
        self.bg_colors = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = square(self.windowh, row, column)
                    self.bg_colors[(row, column)] = 'green'
                else:
                    self.cells[(row, column)] = square(self.windowh, row, column, bg='white')
                    self.bg_colors[(row, column)] = 'white'
                counter += 1
            counter -= 1

    def get_cells(self):
        return self.cells

    def get_bg(self):
        return self.bg_colors


class play_chess:
    def __init__(self):
        self.window = tkinter.Tk()
        self.board = board(self.window)

        self.board_cells = self.board.get_cells()
        self.bg_colors = self.board.get_bg()

        self.window.title("Chess")

        self.black_pieces = {}
        self.white_pieces = {}

        self.create_pieces()

        self.window.mainloop()

    def create_pieces(self):
        for item in range(8):
            self.black_pieces[(1, item)] = pawn(self.window, 'B', (1, item), self.board_cells, self.bg_colors)
            self.white_pieces[(6, item)] = pawn(self.window, 'W', (6, item), self.board_cells, self.bg_colors)

        self.black_pieces[(0, 2)] = bishop(self.window, 'B', (0, 2), self.board_cells, self.bg_colors)
        self.black_pieces[(0, 5)] = bishop(self.window, 'B', (0, 5), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 2)] = bishop(self.window, 'W', (7, 2), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 5)] = bishop(self.window, 'W', (7, 5), self.board_cells, self.bg_colors)

        self.black_pieces[(0, 1)] = knight(self.window, 'B', (0, 1), self.board_cells, self.bg_colors)
        self.black_pieces[(0, 6)] = knight(self.window, 'B', (0, 6), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 1)] = knight(self.window, 'W', (7, 1), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 6)] = knight(self.window, 'W', (7, 6), self.board_cells, self.bg_colors)

        self.black_pieces[(0, 0)] = rook(self.window, 'B', (0, 0), self.board_cells, self.bg_colors)
        self.black_pieces[(0, 7)] = rook(self.window, 'B', (0, 7), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 0)] = rook(self.window, 'W', (7, 0), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 7)] = rook(self.window, 'W', (7, 7), self.board_cells, self.bg_colors)

        self.black_pieces[(0, 4)] = king(self.window, 'B', (0, 4), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 4)] = king(self.window, 'W', (7, 4), self.board_cells, self.bg_colors)

        self.black_pieces[(0, 3)] = queen(self.window, 'B', (0, 3), self.board_cells, self.bg_colors)
        self.white_pieces[(7, 3)] = queen(self.window, 'W', (7, 3), self.board_cells, self.bg_colors)

        for item in self.black_pieces:
            self.board_cells[item].piece = True
            self.black_pieces[item].get_pieces(self.black_pieces)
        for item in self.white_pieces:
            self.board_cells[item].piece = True
            self.white_pieces[item].get_pieces(self.white_pieces)

        for item in self.board_cells:
            self.board_cells[item].get_pieces(self.black_pieces, self.white_pieces)

