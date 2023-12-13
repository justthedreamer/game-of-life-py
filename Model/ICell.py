from abc import ABC, abstractmethod


class ICell(ABC):
    @abstractmethod
    def set_neighbors(self, cells_collection, n_cells_x, n_cells_y):
        pass

    @abstractmethod
    def get_neighbors(self):
        pass
