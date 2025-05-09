from line import Line
from point import Point
class Cell:
    def __init__(self, p1, p2, window):
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        self._win = window
        self.top_left, self.bot_right = self.find_corners(self._x1, self._x2, self._y1, self._y2)

    def draw(self, top_left, bot_right,):
        top_right = Point(bot_right.x, top_left.y)
        bot_left = Point(top_left.x, bot_right.y)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bot_left))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bot_right))
        if self.has_bot_wall:
            self._win.draw_line(Line(bot_left, bot_right))

    def find_corners(self, x1, x2, y1, y2):
        if x1 < x2:
            l_x = x1
            r_x = x2
        else:
            l_x = x2
            r_x = x1
        if y1 > y2:
            u_y = y1
            b_y = y2
        else:
            u_y = y2
            b_y = y1
        return Point(l_x, u_y), Point(r_x, b_y)