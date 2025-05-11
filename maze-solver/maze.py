import time
import random
from cell import Cell
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = True
        if self.seed:
            random.seed()
            
        self._create_cells()
        self._break_walls(i=0, j=0)
        self._reset_visit()
        

    def _create_cells(self):
        self._cells = []
        for i in range(0, self.num_cols):
            self._cells.append([])
        for node in self._cells:
            for i in range(0, self.num_rows):
                node.append(Cell(self._win))

        self._break_entrance_and_exit()
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        if i == 0 and j == 0:
            cell.draw(self.x1, self.y1, (self.x1+self.cell_size_x), (self.y1+self.cell_size_y))
            self._animate()
        else:
            x = self.x1 + (i * self.cell_size_x)
            y = self.y1 + (j * self.cell_size_y)
            cell.draw(x, y, (x+self.cell_size_x), (y+self.cell_size_y))
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[-1][-1]
        start.has_left_wall = False
        end.has_right_wall = False
    
    def _break_walls(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            print("comparing neighbors")
            neighbors = []
            if i != 0:
                if j != 0:
                    neighbor = self._cells[i][j-1]
                    if neighbor.visited == False:
                        print("unvisited neighbor, adding to list")
                        neighbors.append((i, j-1))

                neighbor = self._cells[i-1][j]
                if neighbor.visited == False:
                    print("unvisited neighbor, adding to list")
                    neighbors.append((i-1, j))

            if i != len(self._cells) - 1:
                if j != len(self._cells[i]) - 1:
                    neighbor = self._cells[i][j+1]
                    if neighbor.visited == False:
                        print("unvisited neighbor, adding to list")
                        neighbors.append((i, j+1))
                
                neighbor = self._cells[i+1][j]
                if neighbor.visited == False:
                    print("unvisited neighbor, adding to list")
                    neighbors.append((i+1, j))

            if len(neighbors) == 0:
                print("no valid neighbors")
                self._draw_cell(i, j)
                return
            
            print(f"neighbor contains: {neighbors}")
            if len(neighbors) > 1:
                print("picking a random direction")
                direction = random.randrange(len(neighbors))
                print(f"selected {direction}")
            else:
                direction = 0
            new_i, new_j = neighbors[direction]
            print(f"selected direction is {neighbors[direction]}")
            if new_i > i:
                print("moving to the right")
                cell.has_right_wall = False
                new_cell = self._cells[new_i][j]
                new_cell.has_left_wall = False
                self._break_walls(new_i, j)
            
            elif new_i < i:
                print("moving to the left")
                cell.has_left_wall = False
                new_cell = self._cells[new_i][j]
                new_cell.has_right_wall = False
                self._break_walls(new_i, j)
            
            elif new_j > j:
                print("moving down")
                cell.has_bot_wall = False
                new_cell = self._cells[i][new_j]
                new_cell.has_top_wall = False
                self._break_walls(i, new_j)

            elif new_j < j:
                print("moving up")
                cell.has_top_wall = False
                new_cell = self._cells[i][new_j]
                new_cell.has_bot_wall = False
                self._break_walls(i, new_j)

    def _reset_visit(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        print(f"current location is [{i},{j}]")
        current_cell.visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            print("found the end!")
            return True
        
        if i > 0 and not current_cell.has_left_wall and not self._cells[i-1][j].visited:
            current_cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            current_cell.draw_move(self._cells[i-1][j], undo=True)

        if j > 0 and not current_cell.has_top_wall and not self._cells[i][j-1].visited:
            current_cell.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            current_cell.draw_move(self._cells[i][j-1], undo=True)
        
        if i < len(self._cells)-1 and not current_cell.has_right_wall and not self._cells[i+1][j].visited:
            current_cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            current_cell.draw_move(self._cells[i+1][j], undo=True)
        
        if j < len(self._cells)-1 and not current_cell.has_bot_wall and not self._cells[i][j+1].visited:
            current_cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            current_cell.draw_move(self._cells[i][j+1], undo=True)

        return False

