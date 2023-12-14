from abc import ABC, abstractmethod

class IEventComponent(ABC):
    @abstractmethod
    def get_event_area(self):
        pass

    @abstractmethod
    def get_event_type(self):
        pass


