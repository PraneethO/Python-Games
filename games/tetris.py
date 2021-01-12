import tkinter
import random


class square(tkinter.Label):
    def __init__(self, master, coord):
        tkinter.Label.__init__(self, master, height=1, width=2, text='', bg='grey', font=('Arial', 24), relief='flat')
        self.coord = coord


class block:
    def __init__(self):
        i_Block = []
        j_Block = []
        l_Block = []
        o_Block = []
        s_Block = []
        t_Block = []
        z_Block = []

        block_map = [i_Block, j_Block, l_Block, o_Block, s_Block, t_Block, z_Block]

        rando = random.randint(0, len(block_map) - 1)
        self.item = block_map[rando]

    def detect_collision(self):
        pass

    def get_item(self):
        return self.item


class play_tetris:
    def __init__(self, width, height):
        self.window = tkinter.Tk()
        self.window.title("Tetris")
        self.speed = 1000

        self.cells = {}

        self.height = height
        self.width = width

        self.block_list = [0]

        self.current_block = block()
        self.block_list.append(self.current_block)
        print(self.current_block.get_item())

        for row in range(self.width):
            for column in range(self.height):
                self.cells[(row, column)] = square(self.window, (row, column))
                self.cells[(row, column)].grid(row=row, column=column)
        self.move()
        self.window.mainloop()

    def move(self):
        pass
        self.window.after(self.speed, self.move)


