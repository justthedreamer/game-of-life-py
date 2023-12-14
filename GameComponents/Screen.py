import pygame
class Screen:
    def __init__(self, width, height, bg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color.value

    def get_surface(self):
        surface = pygame.display.set_mode((self.width, self.height))
        surface.fill(self.bg_color)
        return surface
