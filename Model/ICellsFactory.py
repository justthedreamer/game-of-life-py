from abc import ABC, abstractmethod


class ICellsFactory(ABC):
    @abstractmethod
    def create_cells(self, n_cells_x, n_cells_y, cell_size):
        pass
