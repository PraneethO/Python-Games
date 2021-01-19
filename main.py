from games import minesweeper
from games import checkers
from games import snake
from games import tetris
import tkinter


def chec():
    checkers.play_chess()


def tetr():
    tetris.play_tetris()


def snak():
    snake.Snake(int(height_entry.get()), int(width_entry.get()))


def mine():
    minesweeper.play_minesweeper(int(height_entry.get()), int(width_entry.get()), int(bomb_entry.get()))


def quit():
    main_window.quit()


if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.title("Python Games")

    welcome = tkinter.Label(main_window, text="Python Games", fg="Blue")
    end = tkinter.Button(main_window, text="Quit", command=quit)

    checkers_b = tkinter.Button(main_window, text="Checkers", command=chec)
    tetris_b = tkinter.Button(main_window, text="Tetris", command=tetr)
    snake_b = tkinter.Button(main_window, text="Snake", command=snak)
    minesweeper_b = tkinter.Button(main_window, text="Minesweeper", command=mine)

    height_entry = tkinter.Entry(main_window, text='Enter height here.')
    width_entry = tkinter.Entry(main_window, text='Enter width here.')
    bomb_entry = tkinter.Entry(main_window, text='Enter bombs here.')

    height_l = tkinter.Label(main_window, text='Enter height here...')
    width_l = tkinter.Label(main_window, text='Enter width here...')
    bomb_l = tkinter.Label(main_window, text='Enter bomb here...')

    checkers_b.grid(row=1, column=1)
    tetris_b.grid(row=1, column=2)
    snake_b.grid(row=1, column=3)
    minesweeper_b.grid(row=1, column=4)
    end.grid(row=1, column=8)

    height_l.grid(row=2, column=0, columnspan=3)
    width_l.grid(row=3, column=0, columnspan=3)
    bomb_l.grid(row=4, column=0, columnspan=3)

    height_entry.grid(row=3, column=4, columnspan=4)
    width_entry.grid(row=2, column=4, columnspan=4)
    bomb_entry.grid(row=4, column=4, columnspan=4)

    welcome.grid(row=0, column=1, columnspan=2)

    main_window.mainloop()
