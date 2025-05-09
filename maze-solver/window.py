from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver .2")
        self.c = Canvas(self.__root, bg="white", height=height, width=width)
        self.c.pack(fill=BOTH, expand=1)
        self.run_state = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.run_state = True
        while self.run_state:
            self.redraw()

    def close(self):
        self.run_state = False
        

    def draw_line(self, line, color="black"):
        line.draw(self.c, color)