import tkinter
from tkinter import messagebox
import random


class mine_cell(tkinter.Label):
    def __init__(self, master, coord, number, cells, numBombs, bomb_counter):
        tkinter.Label.__init__(self, master, height=1, width=2, text='', bg='white', font=('Arial', 24),
                               relief='raised')
        self.color_map = colormap = ['black', 'blue', 'darkgreen', 'red', 'purple', 'maroon', 'cyan', 'black',
                                     'dim gray']
        self.coord = coord
        self.number = number
        self.master = master
        self.cells = cells
        self.bomb_good = False
        self.numBombs = numBombs
        self.bomb_counter = bomb_counter
        self.bolea = False
        self.bind('<Button-3>', self.bomb_click)
        self.bind('<Button-1>', self.number_click)
        self.show()
        self.actual_num = 'c'
        self.expose = False

    def bomb_click(self, event):
        self['text'] = '*'
        self.bomb_good = True
        bomb_number = self.numBombs
        for item in self.cells:
            if self.cells[item].bomb_good:
                bomb_number -= 1
        self.bomb_counter['text'] = bomb_number
        bomb_number = self.numBombs
        if self.number == 'bomb':
            self.expose = True
        self.check_win()

    def number_click(self, event):
        if self.number == 'bomb':
            tkinter.messagebox.showerror('Minesweeper', 'KABOOM! You lose.', parent=self.master)
            self['bg'] = 'red'
            self['text'] = '*'
            self.show_bomb()
        else:
            self.expose = True
            if self.actual_num == 0:
                self['bg'] = 'light grey'
            else:
                self['fg'] = self.color_map[int(self.actual_num)]
                self['text'] = self.actual_num
            self['bg'] = 'light grey'
            self.auto_expose()
            self.check_win()
        self['relief'] = 'sunken'

    def number_recursion(self):
        self.expose = True
        if self.actual_num == 0:
            self['bg'] = 'light grey'
        else:
            self['fg'] = self.color_map[int(self.actual_num)]
            self['text'] = self.actual_num
        self.bolea = True
        self['relief'] = 'sunken'
        self.auto_expose()
        self['bg'] = 'light grey'

    def show(self):
        self.grid(row=self.coord[0], column=self.coord[1])

    def change_number(self, new_num):
        self.number = new_num

    def change_numberV2(self, new_num):
        self.actual_num = new_num

    def get_number(self):
        return self.number

    def show_bomb(self):
        for index in self.cells:
            if self.cells[index].get_number() == 'bomb':
                for index in self.cells:
                    if self.cells[index].get_number() == 'bomb':
                        self.cells[index]['bg'] = 'red'
                        self.cells[index]['text'] = '*'

    def get_coord(self):
        return self.coord

    def cuz_why_not_lol(self, new_list):
        self.cells = new_list

    def auto_expose(self):
        try:
            if self.cells[(self.coord[0], self.coord[1] + 1)].actual_num == 0 and self.cells[
                (self.coord[0], self.coord[1] + 1)].bolea != True and self.cells[
                (self.coord[0], self.coord[1] + 1)].get_number() != 'bomb':
                self.cells[(self.coord[0], self.coord[1] + 1)].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0], self.coord[1] - 1)].actual_num == 0 and self.cells[
                (self.coord[0], self.coord[1] - 1)].bolea != True and self.cells[
                (self.coord[0], self.coord[1] - 1)].get_number() != 'bomb':
                self.cells[(self.coord[0], self.coord[1] - 1)].number_recursion()
        except KeyError:
            pass

        try:
            if self.cells[(self.coord[0] + 1, self.coord[1])].actual_num == 0 and self.cells[
                (self.coord[0] + 1, self.coord[1])].bolea != True and self.cells[
                (self.coord[0] + 1, self.coord[1])].get_number() != 'bomb':
                self.cells[(self.coord[0] + 1, self.coord[1])].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0] - 1, self.coord[1])].actual_num == 0 and self.cells[
                (self.coord[0] - 1, self.coord[1])].bolea != True and self.cells[
                (self.coord[0] - 1, self.coord[1])].get_number() != 'bomb':
                self.cells[(self.coord[0] - 1, self.coord[1])].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0] - 1, self.coord[1] - 1)].actual_num == 0 and self.cells[
                (self.coord[0] - 1, self.coord[1] - 1)].bolea != True and self.cells[
                (self.coord[0] - 1, self.coord[1] - 1)].get_number() != 'bomb':
                self.cells[(self.coord[0] - 1, self.coord[1] - 1)].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0] + 1, self.coord[1] + 1)].actual_num == 0 and self.cells[
                (self.coord[0] + 1, self.coord[1] + 1)].bolea != True and self.cells[
                (self.coord[0] + 1, self.coord[1] + 1)].get_number() != 'bomb':
                self.cells[(self.coord[0] + 1, self.coord[1] + 1)].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0] - 1, self.coord[1] + 1)].actual_num == 0 and self.cells[
                (self.coord[0] - 1, self.coord[1] + 1)].bolea != True and self.cells[
                (self.coord[0] - 1, self.coord[1] + 1)].get_number() != 'bomb':
                self.cells[(self.coord[0] - 1, self.coord[1] + 1)].number_recursion()
        except KeyError:
            pass
        try:
            if self.cells[(self.coord[0] + 1, self.coord[1] - 1)].actual_num == 0 and self.cells[
                (self.coord[0] + 1, self.coord[1] - 1)].bolea != True and self.cells[
                (self.coord[0] + 1, self.coord[1] - 1)].get_number() != 'bomb':
                self.cells[(self.coord[0] + 1, self.coord[1] - 1)].number_recursion()
        except KeyError:
            pass

    def check_win(self):
        x = 0
        for item in self.cells:
            if self.cells[item].exposed():
                x += 1
        if x == len(self.cells):
            tkinter.messagebox.showerror('Minesweeper', 'Congratulations! You win!', parent=self.master)

    def exposed(self):
        return self.expose


class play_minesweeper:
    def __init__(self, height, width, numBombs):
        self.window = tkinter.Tk()
        self.width = width
        self.height = height
        self.numBombs = numBombs
        self.cells = {}
        self.bomb_counter = tkinter.Label(self.window, text=numBombs, font=('Arial', 24))
        self.bomb_counter.grid(row=self.height + 1, column=int(self.width / 2) - 1)
        for row in range(self.width):
            for column in range(self.height):
                coords = (row, column)
                self.cells[coords] = mine_cell(self.window, coords, 10, self.cells, numBombs, self.bomb_counter)
        for item in self.cells:
            self.cells[item].cuz_why_not_lol(self.cells)
        self.set_bomb()
        self.set_numbers()
        self.window.mainloop()

    def set_bomb(self):
        for bomb in range(self.numBombs):
            row = random.randrange(self.width)
            column = random.randrange(self.height)
            while self.cells[(row, column)].number == 'bomb':
                row = random.randrange(self.width)
                column = random.randrange(self.height)
            self.cells[(row, column)].change_number('bomb')

    def set_numbers(self):
        for item in self.cells:
            total = 0
            try:
                below_number = self.cells[(item[0] - 1, item[1])]
                if below_number.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                above_number = self.cells[(item[0] + 1, item[1])]
                if above_number.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                right_number = self.cells[(item[0], item[1] + 1)]
                if right_number.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                left_number = self.cells[(item[0], item[1] - 1)]
                if left_number.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                upper_r = self.cells[(item[0] - 1, item[1] + 1)]
                if upper_r.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                upper_l = self.cells[(item[0] - 1, item[1] - 1)]
                if upper_l.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                lower_r = self.cells[(item[0] + 1, item[1] + 1)]
                if lower_r.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            try:
                lower_l = self.cells[(item[0] + 1, item[1] - 1)]
                if lower_l.get_number() == 'bomb':
                    total += 1
            except KeyError:
                pass
            self.cells[item].change_numberV2(total)
