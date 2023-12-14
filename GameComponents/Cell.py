from GameComponents.ICell import ICell
from GameComponents.Enum.CellState import CellState
from Event.IEventComponent import IEventComponent
from Event.EventType import EventType
class Cell(ICell,IEventComponent):
    def __init__(self, state, size, index_x, index_y):
        self.state = state
        self.size = size
        self.index_x = index_x
        self.index_y = index_y
        self.neighbours = []

    def set_neighbors(self, cells_collection, n_cells_x, n_cells_y):
        self.neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x = self.index_x + i
                new_y = self.index_y + j

                if 0 <= new_x < n_cells_x and 0 <= new_y < n_cells_y and (i, j) != (0, 0):
                    self.neighbours.append(cells_collection[new_x + new_y * n_cells_x])

                elif (i, j) != (0, 0):
                    wrapped_x = (new_x + n_cells_x) % n_cells_x
                    wrapped_y = (new_y + n_cells_y) % n_cells_y
                    self.neighbours.append(cells_collection[wrapped_x + wrapped_y * n_cells_x])

    def get_neighbors(self):
        return self.neighbours

    def get_alive_neighbors(self):
        neighbors = self.get_neighbors()
        count = 0
        for neighbor in neighbors:
            if neighbor.state == CellState.Alive: count += 1
        return count

    def get_event_area(self):
        return [[self.index_x * self.size, self.index_x * self.size + self.size], [self.index_y * self.size, self.index_y * self.size + self.size]]

    def get_event_type(self):
        return EventType.DRAW_CELL

