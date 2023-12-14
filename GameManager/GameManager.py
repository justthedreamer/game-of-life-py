import pygame
from enum import Enum
import numpy as np
import time
import threading
from abc import ABC, abstractmethod

from GameSettings.GameSettings import GameSettings
from GameBuilder.GameBuilder import GameBuilder
from GameController.GameController import GameController
from Event.EventHandler import EventHandler
from GameComponents.CellsFactory import CellsFactory
from Event.CustomEvent import CustomEvent

from GameComponents.Enum.Color import Color
class GameManager:
    def __init__(self):
        self.game_settings = GameSettings()
        self.game_builder = GameBuilder(self.game_settings)
        self.game_controller = GameController(self.game_builder)
        self.event_handler = EventHandler()
        self.game_state = True

    def apply_custom_settings(self, game_settings):
        self.game_builder.apply_settings(game_settings)

    def run(self):
        self.game_controller.init_game()
        while self.game_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_controller.real_time_run_state = False
                    self.game_state = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.event_handler.mouse_button_down_handler(
                        CustomEvent(event, self.game_builder.event_components, self.game_controller))



