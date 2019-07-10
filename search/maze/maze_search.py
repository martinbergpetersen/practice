from enum import Enum
import random
from generic_search import (breadth_first_serach, depth_first_search,
                            node_to_path)


class MazeLocation:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        if self.row != other.row:
            return False
        if self.column != other.column:
            return False
        return True

    def __hash__(self):
        return hash((self.row, self.column))


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class Maze:
    def __init__(self,
                 rows=10,
                 columns=10,
                 sparseness=0.2,
                 start=MazeLocation(0, 0),
                 goal=MazeLocation(9, 9)):
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        self._grid = [[Cell.EMPTY for c in range(columns)]
                      for r in range(rows)]
        self._randomly_filled(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_filled(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def is_goal(self, maze_location):
        return maze_location == self.goal

    def successors(self, maze_location):
        maze_locations = []
        if (maze_location.row + 1 < self._rows
                and self._grid[maze_location.row + 1][maze_location.column] !=
                Cell.BLOCKED):

            maze_locations.append(
                MazeLocation(maze_location.row + 1, maze_location.column))

        if (maze_location.row - 1 >= 0
                and self._grid[maze_location.row - 1][maze_location.column] !=
                Cell.BLOCKED):

            maze_locations.append(
                MazeLocation(maze_location.row - 1, maze_location.column))

        if maze_location.column + 1 < self._columns and self._grid[
                maze_location.row][maze_location.column + 1] != Cell.BLOCKED:

            maze_locations.append(
                MazeLocation(maze_location.row, maze_location.column + 1))

        if maze_location.column - 1 >= 0 and self._grid[maze_location.row][
                maze_location.column - 1] != Cell.BLOCKED:

            maze_locations.append(
                MazeLocation(maze_location.row, maze_location.column - 1))

        return maze_locations

    def mark(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self):
        out = ''
        for row in self._grid:
            out += ''.join([c.value for c in row]) + '\n'
        return out


def run():
    ma = Maze()
    solution1 = depth_first_search(ma.start, ma.is_goal, ma.successors)
    print('*'*10)
    print('SOLUTION1')
    print('*'*10)
    print('')
    if solution1 is None:
        print(ma)
        print("No solution number 1")
    else:
        path = node_to_path(solution1)
        ma.mark(path)
        print(ma)
        ma.clear(path)
    print('')
    print('*'*10)
    print('SOLUTION2')
    print('*'*10)
    print('')
    solution2 = breadth_first_serach(ma.start, ma.is_goal, ma.successors)
    if solution2 is None:
        print(ma)
        print('No solution for number 2')
    else:
        path = node_to_path(solution2)
        ma.mark(path)
        print(ma)
        ma.clear(path)
