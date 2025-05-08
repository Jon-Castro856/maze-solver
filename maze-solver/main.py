from window import Window
from point import Point
from line import Line
win = Window(800, 600)
start = Point(50, 50)
end = Point(100, 100)
line = Line(start, end)
win.draw_line(line, "black")
win.wait_for_close()