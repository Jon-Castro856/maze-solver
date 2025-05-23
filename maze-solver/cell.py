from line import Line
from point import Point
class Cell:
    def __init__(self, window=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        self._win = window
        self.visited = False


    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, color="white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, color="white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, color="white")
        if self.has_bot_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, color="white")

    
    def draw_move(self, to_cell, undo=False):
        center_x = self._x1 + ((self._x2 - self._x1) // 2)
        center_y = self._y1 + ((self._y2 - self._y1) // 2)
        target_x = to_cell._x1 + ((to_cell._x2 - to_cell._x1) // 2)
        target_y = to_cell._y1 + ((to_cell._y2 - to_cell._y1) // 2)
        line = Line(Point(center_x, center_y), Point(target_x, target_y))
        if undo == False:
            self._win.draw_line(line, color="red")
        else:
            self._win.draw_line(line, color="grey")