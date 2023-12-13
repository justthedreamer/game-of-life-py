from Event.EventType import EventType
from Event.ICustomEvent import ICustomEvent

class CustomEvent(ICustomEvent):
    def __init__(self, event, event_components, sender):
        self.event = event
        self.event_components = event_components
        self.sender = sender

    def get_event_type(self):
        event_pos_x, event_pos_y = self.event.pos[0], self.event.pos[1]
        for items in self.event_components:
            for component in items:
                event_area = component.get_event_area()
                if (
                        event_pos_x >= event_area[0][0] and event_pos_x <= event_area[0][1] and
                        event_area[1][0] <= event_pos_y <= event_area[1][1]
                ):
                    return component.get_event_type()
