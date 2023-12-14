from Event.Interfaces.ICustomEvent import ICustomEvent
from GameController.Interfaces import IGameController

class CustomEvent(ICustomEvent):
    def __init__(self, event, event_components : ICustomEvent, controller : IGameController):
        self.event = event
        self.event_components = event_components
        self.controller = controller

    def get_event_type(self):
        event_pos_x, event_pos_y = self.event.pos[0], self.event.pos[1]
        for components in self.event_components:
            for component in components:
                event_area = component.get_event_area()
                if (
                        event_pos_x >= event_area[0][0] and event_pos_x <= event_area[0][1] and
                        event_area[1][0] <= event_pos_y <= event_area[1][1]
                ):
                    return component.get_event_type()

    def get_event_component(self):
        event_pos_x, event_pos_y = self.event.pos[0], self.event.pos[1]
        for components in self.event_components:
            for component in components:
                event_area = component.get_event_area()
                if (
                        event_pos_x >= event_area[0][0] and event_pos_x <= event_area[0][1] and
                        event_area[1][0] <= event_pos_y <= event_area[1][1]
                ):
                    return component
