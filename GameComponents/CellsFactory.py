import numpy as np
from GameComponents.Interfaces.ICellsFactory import ICellsFactory
from GameComponents.Cell import Cell


class CellsFactory(ICellsFactory):
    @staticmethod
    def get_state():
        return np.random.choice([0, 1], p=[0.8, 0.2])

    @staticmethod
    def create_cells(game_settings):
        n_cells_x = game_settings.n_cells_x
        n_cells_y = game_settings.n_cells_y
        size = game_settings.cell_size

        cells = []
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                cells.append(Cell(CellsFactory.get_state(), size, x, y))
        if cells is not None:
            for cell in cells:
                cell.set_neighbors(cells, n_cells_x, n_cells_y)
        return cells

    @staticmethod
    def create_empty_board(game_settings):
        n_cells_x = game_settings.n_cells_x
        n_cells_y = game_settings.n_cells_y
        size = game_settings.cell_size

        cells = []
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                cells.append(Cell(0, size, x, y))
        if cells is not None:
            for cell in cells:
                cell.set_neighbors(cells, n_cells_x, n_cells_y)
        return cells

    @staticmethod
    def create_custom_board(n_cells_x, n_cells_y,cell_size, cells_as_binary_arr):
        cells = []
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                cells.append(Cell(cells_as_binary_arr[y][x], cell_size, x, y))

        if cells is not None:
            for cell in cells:
                cell.set_neighbors(cells, n_cells_x, n_cells_y)

        return cells

