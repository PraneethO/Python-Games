import tkinter

class play_chess:
    class pawn(play_chess):
        pass


class pawn:
    def __init__(self, master, color, coord_obj):
        if color == 'B':
            #pawn = tkinter.Canvas(master, width=50, height=50)

            img = tkinter.PhotoImage(master=coord_obj, file="Images/test.gif")

            image = coord_obj.create_image(10, 10, anchor=tkinter.NW, image=img)

            #pawn.grid(row=coord[0], column=coord[1])
        #canvas = tkinter.Canvas(master, height=50, width=50)


class board:
    def __init__(self, window):
        self.windowh = window

        self.cells = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = tkinter.Canvas(self.windowh, bg='green', height=50, width=50)
                    self.cells[(row, column)].grid(row=row, column=column)
                else:
                    self.cells[(row, column)] = tkinter.Canvas(self.windowh, height=50, width=50)
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


        self.windowh.mainloop()
