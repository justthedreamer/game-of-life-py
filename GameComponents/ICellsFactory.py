from abc import ABC, abstractmethod


class ICellsFactory(ABC):
    @staticmethod
    def create_cells(game_settings):
        pass
