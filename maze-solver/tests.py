import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_location(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(800, 600, num_rows, num_cols, 10, 10)
        self.assertEqual(m1.x1, 800)
        self.assertEqual(m1.y1, 600)
    
    def test_wall_breaker(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(800, 600, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        start = m1._cells[0][0]
        end = m1._cells[-1][-1]

        self.assertEqual(start.has_left_wall, False)
        self.assertEqual(end.has_right_wall, False)

if __name__ == "__main__":
    unittest.main()