import tkinter


class pawn:
    def __init__(self, master, color, coord):
        pawn = tkinter.Canvas(master, height=64, width=64)
        pawn.grid(row=(coord[0]), column=(coord[1]))

        if color == 'B':
            img = tkinter.PhotoImage(file=r'img(GIF)/blackp.gif')
            master.img = img
        else:
            img = tkinter.PhotoImage(file=r'img(GIF)/whitep.gif')
            master.img = img

        pawn.create_image((35, 35), image=img)


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
        self.windowh = tkinter.Tk()
        self.board = board(self.windowh)

        self.board_cells = self.board.get_cells()

        self.windowh.title("Chess")

        pawn(self.windowh, 'B', (1, 1))

        self.windowh.mainloop()


play_chess()
