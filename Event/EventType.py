from enum import Enum

class EventType(Enum):
    DRAW_CELL = 0
    NEXT_GENERATION = 1
    START_STOP = 2
    LOAD = 3
    SAVE = 4

