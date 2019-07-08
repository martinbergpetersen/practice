from enum import Enum
import random


class MazeLocation:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class Stack:
    def __init__(self):
        self._container = []

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


class Maze:
    def __init__(self,
                 rows=10,
                 columns=10,
                 sparseness=0.2,
                 start=MazeLocation(0, 0),
                 goal=MazeLocation(9, 9)):
        self._rows = rows,
        self._columns = columns,
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
        if (maze_location.row + 1 < self._rows and
                self._grid[maze_location.row + 1][maze_location.column] !=
                Cell.BLOCKED):

            maze_locations.append(
                MazeLocation(maze_location.row + 1, maze_location.column))

        if (maze_location.row - 1 >= 0 and
                self._grid[maze_location.row - 1][maze_location.column] !=
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

    def __str__(self):
        out = ''
        for row in self._grid:
            out += ''.join([c.value for c in row]) + '\n'
        return out
