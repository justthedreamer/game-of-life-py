class Grid:
    def __init__(self, rows, columns, cell_size, color):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.color = color.value
        self.width = rows * cell_size
        self.height = columns * cell_size
