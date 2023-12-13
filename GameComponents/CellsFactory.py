import numpy as np
from Model.ICellsFactory import ICellsFactory
from Model.Cell import Cell
class CellsFactory(ICellsFactory):
    @staticmethod
    def get_state():
        return np.random.choice([0, 1], p=[0.8, 0.2])

    def create_cells(self, n_cells_x, n_cells_y, size):
        cells = []
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                cells.append(Cell(self.get_state(), size, x, y))
        if cells is not None:
            for cell in cells:
                cell.set_neighbors(cells, n_cells_x, n_cells_y)
        return cells
