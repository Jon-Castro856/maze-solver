from window import Window
from point import Point
from line import Line
from cell import Cell
win = Window(800, 600)
cell = Cell(Point(50, 100), Point(100, 50), win)
nu_cell = Cell(Point(200, 250), Point(400, 450), win)
nu_cell.has_bot_wall = False
nu_cell.has_top_wall = False
nu_cell.draw(nu_cell.top_left, nu_cell.bot_right)
cell.draw(cell.top_left, cell.bot_right)
win.wait_for_close()