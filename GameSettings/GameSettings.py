from GameComponents.Enum.Color import Color


class GameSettings:
    def __init__(self):
        self.n_cells_x = 50
        self.n_cells_y = 50
        self.cell_size = 15
        self.cell_color = Color.ROSE_QUARTZ
        self.screen_height = 800
        self.screen_width = 1000
        self.screen_bg_color = Color.BLUE_GRAY
        self.grid_color = Color.BLACK
        self.tick_rate = .1

    def use_custom_settings(self, n_cells_x, n_cells_y, cell_size, cell_color, screen_width, screen_height,
                            screen_bg_color, grid_color, tick_rate):
        self.cell_color = cell_color
        self.grid_color = grid_color
        self.screen_bg_color = screen_bg_color
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.cell_size = cell_size
        self.n_cells_y = n_cells_y
        self.n_cells_x = n_cells_x
        self.tick_rate = tick_rate

    def set_cell_color(self, color):
        self.cell_color = color

    def set_grid_color(self, color):
        self.grid_color = color

    def off_grid(self):
        self.grid_color = self.screen_bg_color
