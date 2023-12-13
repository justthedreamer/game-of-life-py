from abc import ABC,abstractmethod
class ICustomEvent(ABC):
    def get_event_type(self):
        pass