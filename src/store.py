from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.ida_star import IDAStarFinder

class store:
    def __init__(self,grid_matrix):
        self.finder = IDAStarFinder(diagonal_movement=DiagonalMovement.never)
        self.grid = Grid(matrix=grid_matrix)
        self.matrix = grid_matrix
    def pathfinder(self,start_node,end_node):
        start = self.grid.node(start_node[1], start_node[0])
        end = self.grid.node(end_node[1], end_node[0])
        path, runs = self.finder.find_path(start, end, self.grid)
        # print(path)
        # print('operations:', runs, 'path length:', len(path))
        # print(self.grid.grid_str(path=path, start=start, end=end))
        return path