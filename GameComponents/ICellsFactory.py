from abc import ABC, abstractmethod


class ICellsFactory(ABC):
    @staticmethod
    def create_cells(game_settings):
        pass

    @staticmethod
    def create_empty_board(game_settings):
        pass

    @staticmethod
    def create_custom_board(n_cells_x, n_cells_y, cell_size, cells_as_binary_arr):
        pass