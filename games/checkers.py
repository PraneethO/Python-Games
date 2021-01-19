import tkinter


class pawn:
    def __init__(self, master, color, coord, cell_list):
        self.pawn = tkinter.Canvas(master, height=70, width=70, bg=cell_list[coord]['bg'])
        self.pawn.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            self.img = tkinter.PhotoImage(file=r'img(GIF)/blackp.gif')
            master.img = self.img
        else:
            self.img = tkinter.PhotoImage(file=r'img(GIF)/whitep.gif')
            master.img = self.img

        self.pawn.create_image((35, 35), image=self.img)


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

        pawn_list = {}

        for item in range(8):
            pawn_list[(1, item)] = pawn(self.window, 'B', (1, item), self.board_cells)

        self.window.mainloop()


play_chess()
