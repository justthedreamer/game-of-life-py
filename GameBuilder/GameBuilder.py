from GameComponents.Screen import Screen
from GameComponents.Button import Button
from GameComponents.Grid import Grid
from GameComponents.Enum.Color import Color
from Event.EventType import EventType
from GameComponents.CellsFactory import CellsFactory


class GameBuilder:
    def __init__(self, game_settings):

        self.screen = Screen(game_settings.screen_width, game_settings.screen_height, game_settings.screen_bg_color)
        self.surface = self.screen.get_surface()
        self.cells_factory = CellsFactory()
        self.cells = self.cells_factory.create_cells(game_settings)
        self.buttons = [
            Button("Next Generation", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 10,
                   EventType.NEXT_GENERATION),
            Button("Start/Stop", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 70,
                   EventType.START_STOP),
            Button("Load", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 130, EventType.LOAD),
            Button("Save", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 190, EventType.SAVE),
            Button("Clear board", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 250,
                   EventType.CLEAR_BOARD),
            Button("Random", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 310,
                   EventType.RANDOM)
        ]
        self.event_components = [self.buttons, self.cells]
        self.grid = Grid(game_settings.n_cells_x, game_settings.n_cells_y, game_settings.cell_size,
                         game_settings.grid_color)

    def update_event_componentes(self):
        self.event_components = [self.buttons, self.cells]

    def set_cells(self, cells):
        self.cells = cells
        self.update_event_componentes()

