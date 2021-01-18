import tkinter

class pawn:
    def __init__(self, canvas_obj, color):
        if color == "B":
            black_pawn_img = tkinter.PhotoImage(file="Images/Black_Pawn.gif")
            canvas_obj.create_image(50, 10, image=black_pawn_img, anchor=tkinter.NW)


class play_checkers:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Checkers")

        self.cells = {}

        counter = 0
        for row in range(8):
            for column in range(8):
                if counter % 2 == 1:
                    self.cells[(row, column)] = tkinter.Canvas(self.window, height=50, width=50, bg="green")
                else:
                    self.cells[(row, column)] = tkinter.Canvas(self.window, height=50, width=50, bg="white")
                self.cells[(row, column)].grid(row=row, column=column)
                counter += 1
            counter -= 1

        pawn(self.cells[(1, 1)], "B")

        self.window.mainloop()
