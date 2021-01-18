import tkinter


class pawn:
    def __init__(self, label_obj, color):
        if color == "B":
            img = tkinter.PhotoImage(file="Images/Black_Pawn.gif")
            label_obj.configure(image=img)



class play_checkers:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Checkers")

        self.cells = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = tkinter.Label(self.window, height=1, width=2, bg='green')
                    self.cells[(row, column)].grid(row=row, column=column)
                else:
                    self.cells[(row, column)] = tkinter.Label(self.window, height=1, width=2)
                    self.cells[(row, column)].grid(row=row, column=column)
                counter += 1
            counter -= 1

        pawn(self.cells[(1, 1)], "B")

        self.window.mainloop()
