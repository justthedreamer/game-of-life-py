import pygame
from GameComponents.Enum.CellState import CellState


class Renderer:

    @staticmethod
    def draw_grid(game_settings,game_builder):
        grid = game_builder.grid
        surface = game_builder.surface
        grid_color = game_settings.grid_color
        for y in range(grid.columns):
            for x in range(grid.rows):
                cell = pygame.Rect(x * grid.cell_size, y * grid.cell_size, grid.cell_size, grid.cell_size)
                pygame.draw.rect(surface, grid_color.value, cell, 1)

    @staticmethod
    def draw_cells(game_settings,game_builder):
        cells = game_builder.cells
        surface = game_builder.surface

        alive_cell_color = game_settings.cell_color.value
        dead_cell_color = game_settings.screen_bg_color.value
        cell_size = game_settings.cell_size

        for cell in cells:
            item = pygame.Rect(cell.index_x * cell_size, cell.index_y * cell_size, cell_size,
                               cell_size)
            if cell.state == CellState.Alive:
                pygame.draw.rect(surface, alive_cell_color, item)
            elif cell.state == CellState.Dead:
                pygame.draw.rect(surface, dead_cell_color, item)

    @staticmethod
    def draw_button(surface, button):
        pygame.draw.rect(surface, button.bg_color, (button.position_x, button.position_y, button.width, button.height))
        font = pygame.font.Font(None, 36)
        text = font.render(button.text, True, button.font_color)
        text_rect = text.get_rect(
            center=(button.position_x + button.width // 2, button.position_y + button.height // 2))
        surface.blit(text, text_rect)

    @staticmethod
    def draw_buttons(game_builder):
        buttons_collection = game_builder.buttons
        surface = game_builder.surface
        for button in buttons_collection:
            Renderer.draw_button(surface, button)
    @staticmethod
    def draw_message(game_builder,text,color):
        pass





