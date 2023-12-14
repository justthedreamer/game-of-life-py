class Grid:
    def __init__(self, game_settings):
        self.rows = game_settings.n_cells_x
        self.columns = game_settings.n_cells_y
        self.cell_size = game_settings.cell_size
        self.color = game_settings.grid_color.value
        self.width = self.rows * self.cell_size
        self.height = self.color * self.cell_size
