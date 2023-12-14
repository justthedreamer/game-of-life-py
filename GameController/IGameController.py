from abc import ABC, abstractmethod


class IGameController(ABC):

    @abstractmethod
    def next_generation(self):
        pass

    @abstractmethod
    def start_stop(self):
        pass

    @abstractmethod
    def load_file(self, path):
        pass

    @abstractmethod
    def save_to_file(self, path):
        pass
