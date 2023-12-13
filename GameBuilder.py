import pygame
from enum import Enum
import numpy as np
import time
import threading
from abc import ABC, abstractmethod

from GameComponents.Renderer import Renderer
from GameComponents.Screen import Screen
from GameComponents.Button import Button
from GameComponents.Grid import Grid
from GameComponents.CellsFactory import CellsFactory
from GameComponents.Enum.Color import Color
from Model.ICellsFactory import ICellsFactory
from Model.ICell import ICell
from Model.Cell import Cell
from Model.CellState import CellState
from Event.IEventComponent import IEventComponent
from Event.EventType import EventType
from Event.EventHandler import EventHandler
from Event.CustomEvent import CustomEvent


class GameBuilder:
    def __init__(self):
        pygame.init()
        self.n_cells_x = 25
        self.n_cells_y = 25
        self.cell_size = 20
        self.screen = Screen(1000, 800, (0x2E, 0x34, 0x40))
        self.surface = self.screen.get_surface()
        self.grid = Grid(self.n_cells_x, self.n_cells_y, self.cell_size, Color.STEEL_BLUE)
        self.cellsFactory = CellsFactory()
        self.cells = self.cellsFactory.create_cells(self.n_cells_x, self.n_cells_y, self.cell_size)
        self.renderer = Renderer()
        self.running = True
        self.buttons = [
            Button("Next Generation", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 10,
                   EventType.NEXT_GENERATION),
            Button("Start/Stop", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 70,
                   EventType.START_STOP),
            Button("Load", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 130, EventType.LOAD),
            Button("Save", 200, 50, 18, Color.WHITE, Color.DARK_GRAY, (self.screen.width - 210), 190, EventType.SAVE)
        ]
        self.event_handler = EventHandler()
        self.event_components = [self.buttons]
        self.thread = None
        self.tick_rate = 1
        self.real_time_run_state = False

    def next_generation(self):
        cells = self.cells
        new_generation = []

        for cell in self.cells:
            alive_neighbours = cell.get_alive_neighbors()

            if cell.state == CellState.Dead:
                if alive_neighbours == 3:
                    new_generation.append(Cell(CellState.Alive, self.cell_size, cell.index_x, cell.index_y))
                else:
                    new_generation.append(Cell(CellState.Dead, self.cell_size, cell.index_x, cell.index_y))
            elif cell.state == CellState.Alive:
                if alive_neighbours < 2:
                    new_generation.append(Cell(CellState.Dead, self.cell_size, cell.index_x, cell.index_y))
                elif alive_neighbours > 3:
                    new_generation.append(Cell(CellState.Dead, self.cell_size, cell.index_x, cell.index_y))
                elif alive_neighbours == 3 or alive_neighbours == 2:
                    new_generation.append(Cell(CellState.Alive, self.cell_size, cell.index_x, cell.index_y))

        for cell in new_generation:
            cell.set_neighbors(new_generation, self.n_cells_x, self.n_cells_y)

        self.cells = new_generation

    def real_time_run(self, ticks):
        while self.real_time_run_state:
            self.next_generation()
            self.update_game()
            time.sleep(ticks)

    def start_stop(self):
        self.real_time_run_state = not self.real_time_run_state
        if self.real_time_run_state:
            self.thread = threading.Thread(target=self.real_time_run, args=(.1,))
            self.thread.start()
        else:
            self.thread.join()

    def update_game(self):
        self.renderer.draw_cells(self.surface, self.grid, self.cells)
        self.renderer.draw_grid(self.surface, self.grid)
        pygame.display.flip()

    def build(self):
        self.renderer.draw_buttons(self.surface, self.buttons)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.event_handler.mouse_button_down_handler(CustomEvent(event, self.event_components, self))

            self.update_game()


gameBuilder = GameBuilder()
gameBuilder.build()
gameBuilder.run()
