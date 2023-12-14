from Event.EventType import EventType
from Event.CustomEvent import CustomEvent
from Event.Interfaces.ICustomEvent import ICustomEvent
class EventHandler:
    @staticmethod
    def mouse_button_down_handler(custom_event : ICustomEvent):
        event_type = custom_event.get_event_type()
        controller = custom_event.controller
        if event_type == EventType.NEXT_GENERATION:
            controller.next_generation()
        if event_type == EventType.START_STOP:
            controller.start_stop()
        if event_type == EventType.CLEAR_BOARD:
            controller.clear_board()
        if event_type == EventType.SAVE:
            controller.save_to_file()
        if event_type == EventType.LOAD:
            controller.load_from_file()
        if event_type == EventType.RANDOM:
            controller.new_random_board()
        if event_type == EventType.DRAW_CELL:
            cell = custom_event.get_event_component()
            controller.toggle_cell_event(cell)
