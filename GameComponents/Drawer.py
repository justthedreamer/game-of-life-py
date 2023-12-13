import pygame
from Model.CellState import CellState
from GameComponents.Enum.Color import Color


class Drawer:
    @staticmethod
    def draw_grid(surface, grid):
        for y in range(grid.columns):
            for x in range(grid.rows):
                cell = pygame.Rect(x * grid.cell_size, y * grid.cell_size, grid.cell_size, grid.cell_size)
                pygame.draw.rect(surface, grid.color, cell, 1)

    @staticmethod
    def draw_cells(surface, grid, cells):

        for cell in cells:
            item = pygame.Rect(cell.index_x * grid.cell_size, cell.index_y * grid.cell_size, grid.cell_size,
                               grid.cell_size)

            if cell.state == CellState.Alive:
                pygame.draw.rect(surface, Color.ROSE_QUARTZ.value, item)
            elif cell.state == CellState.Dead:
                pygame.draw.rect(surface, Color.BLACK.value, item)

    @staticmethod
    def draw_button(surface, button):
        pygame.draw.rect(surface, button.bg_color, (button.position_x, button.position_y, button.width, button.height))
        font = pygame.font.Font(None, 36)
        text = font.render(button.text, True, button.font_color)
        text_rect = text.get_rect(
            center=(button.position_x + button.width // 2, button.position_y + button.height // 2))
        surface.blit(text, text_rect)

    @staticmethod
    def draw_buttons(surface, buttons_collection):
        for button in buttons_collection:
            Drawer.draw_button(surface, button)
