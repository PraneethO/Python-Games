import tkinter


class square(tkinter.Label):
    def __init__(self, window, coord, bg, checker=False):
        tkinter.Label.__init__(self, window, text='', height=1, width=2, relief='raised', bg=bg)
        self.coord = coord
        self.checker = checker


class play_checkers:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Checkers")

        self.cells = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = square(self.window, (row, column), 'green')
                else:
                    self.cells[(row, column)] = square(self.window, (row, column), 'white')
                self.cells[(row, column)].grid(row=row, column=column)
                counter += 1
            counter -= 1
        self.window.mainloop()


