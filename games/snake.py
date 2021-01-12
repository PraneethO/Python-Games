import tkinter
import random





# Class for charachteristics of each square
class cell(tkinter.Label):
    def __init__(self, master, coords, velocity='0', cherry=False):
        tkinter.Label.__init__(self, master, height=1, width=2, text='', bg='grey', font=('Arial', 24), relief='flat')

        self.coords = coords
        self.cherry = cherry
        self.velocity = velocity

    # Returns if square is a cherry
    def get_cherry(self):
        return self.cherry

    # Changes velocity of square
    def change_v(self, new_dir):
        self.velocity = new_dir


# Main class to play game
class Snake:
    def __init__(self, width, height):
        self.window = tkinter.Tk()

        self.window.title("Snake!")
        self.width = width
        self.height = height
        self.direction = 'Right'
        self.size = 2
        self.snake = []

        self.cells = {}

        # Creates window of squares for the game to be played in
        for row in range(width):
            for column in range(height):
                coords = (row, column)
                self.cells[coords] = cell(self.window, coords)
                self.cells[coords].grid(row=row, column=column)

        # Initializes Listeners
        self.window.bind("<Left>", self.turn_left)
        self.window.bind("<Right>", self.turn_right)
        self.window.bind("<Up>", self.turn_up)
        self.window.bind("<Down>", self.turn_down)

        # Creates first random cherry
        self.new_cherry()
        # Creates snake
        self.create_snake()
        # Starts snake movement on timer (in-class)
        self.move()
        self.window.mainloop()

    # Initially creates snake with self.size as length
    def create_snake(self):
        for item in range(0, self.size):
            self.cells[(0, item)]['bg'] = 'light green'
            self.snake.append((0, item))

    # Turns the turtle left on command
    def turn_left(self, event):
        self.direction = 'Left'
        self.vertex = self.snake[len(self.snake) - 1]

    # Turns the turtle right on command
    def turn_right(self, event):
        self.direction = 'Right'
        self.vertex = self.snake[len(self.snake) - 1]

    # Turns the turtle up on command
    def turn_up(self, event):
        self.direction = 'Up'
        self.vertex = self.snake[len(self.snake) - 1]

    # Turns the turtle down on command
    def turn_down(self, event):
        self.direction = 'Down'
        self.vertex = self.snake[len(self.snake) - 1]

    # Moves the turtle periodically (0.25 seconds)
    def move(self):

        try:
            # Old Code


            for n in range(1):

                for item in self.snake:
                    self.cells[item]['bg'] = 'grey'

                if self.direction == 'Right':
                    itera = 0
                    for item in self.snake:
                        self.snake[itera] = (item[0],item[1]+1)
                        itera += 1

                if self.direction == 'Left':
                    itera = 0
                    for item in self.snake:
                        self.snake[itera] = (item[0],item[1]-1)
                        itera += 1

                if self.direction == 'Down':
                    itera = 0
                    for item in self.snake:
                        self.snake[itera] = (item[0]+1,item[1])
                        itera += 1

                if self.direction == 'Up':
                    itera = 0
                    for item in self.snake:
                        self.snake[itera] = (item[0]-1,item[1])
                        itera += 1


                for item in self.snake:
                    self.cells[item]['bg'] = 'light green'


            # New Code (Maybe?)

            self.check_cherry()

        except KeyError:
            print("You Lost!")
            self.window.destroy()
            return ''

        self.window.after(100, self.move)

    # Checks if the head of the snake is on a cherry
    def check_cherry(self):
        self.cells[self.snake[len(self.snake) - 1]]['bg'] = 'blue'
        if self.cells[self.snake[len(self.snake) - 1]].get_cherry():
            self.cells[(self.row, self.column)].cherry = False
            self.cells[(self.row, self.column)]['bg'] = 'grey'
            self.size += 1
            print(self.size)
            self.new_cherry()

    # Makes a new random cherry when the old one is eaten
    def new_cherry(self):
        self.row = random.randint(0, self.width - 1)
        self.column = random.randint(0, self.height - 1)

        # Keeps on getting random numbers until it doesn't interfere with the snake
        while self.cells[(self.row, self.column)]['bg'] == 'light green':
            row = random.randint(0, self.width - 1)
            column = random.randint(0, self.height - 1)

        self.cells[(self.row, self.column)]['bg'] = 'dark red'
        self.cells[(self.row, self.column)].cherry = True
