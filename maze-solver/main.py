from window import Window
from maze import Maze
win = Window(800, 600)
num_rows = 22
num_cols = 30
maze = Maze(15, 20, num_rows, num_cols, 25, 25, win)
maze.solve()
win.wait_for_close()