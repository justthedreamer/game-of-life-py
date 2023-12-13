from Event.EventType import EventType
from Event.CustomEvent import CustomEvent
class EventHandler:
    @staticmethod
    def mouse_button_down_handler(custom_event):
            event_type = custom_event.get_event_type()
            sender = custom_event.sender
            if event_type == EventType.NEXT_GENERATION:
                sender.next_generation()
            if event_type == EventType.START_STOP:
                sender.start_stop()