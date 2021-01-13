from games import minesweeper
from games import checkers
from games import snake
from games import tetris
import tkinter


def chec():
    checkers.play_checkers()


def tetr():
    tetris.play_tetris()


def snak():
    snake.Snake(10, 10)


def mine():
    minesweeper.play_minesweeper(10, 10, 15)


def quit():
    main_window.quit()


if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.title = "Python Games"

    welcome = tkinter.Label(main_window, text="Python Games", fg="Blue")
    end = tkinter.Button(main_window, text="Quit", command=quit)

    checkers_b = tkinter.Button(main_window, text="Checkers", command=chec)
    tetris_b = tkinter.Button(main_window, text="Tetris", command=tetr)
    snake_b = tkinter.Button(main_window, text="Snake", command=snak)
    minesweeper_b = tkinter.Button(main_window, text="Minesweeper", command=mine)

    checkers_b.grid(row=1, column=0)
    tetris_b.grid(row=1, column=1)
    snake_b.grid(row=1, column=2)
    minesweeper_b.grid(row=1, column=3)
    end.grid(row=1, column=4)

    welcome.grid(row=0, column=1, columnspan=2)

    main_window.mainloop()
